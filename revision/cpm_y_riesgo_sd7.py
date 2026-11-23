"""Calcula el CPM lógico y escenarios PERT del SD7 sin reemplazar la carta nivelada."""

import argparse
from datetime import timedelta
import json
import math
from pathlib import Path
import random
import statistics

from edt_cpm_20261117 import (
    CAL, END, MONTHS, ORDER, START, after, allowed_cut, build, endpoints,
    period, rank, schedule, topological,
)


def make_network(tasks, edges, fixed, packages, milestones, estimates):
    start = rank(START)
    nodes = {(key, side) for key, task in tasks.items()
             for side in (('start',) if task['milestone'] else ('start', 'finish'))}
    relations = []
    for edge in edges:
        source, target = endpoints(edge, tasks)
        lag = edge['lag']
        if target[0].startswith('CONTRATO:'):
            lag = max(lag, math.ceil(160 / (6.4 * packages[source[0]]['peak'])) - 1)
        if source[0].startswith('INTEGRACION:') and target[0] in packages:
            lag = max(lag, math.ceil(80 / (6.4 * packages[target[0]]['peak'])) - 1)
        relations.append((source, target, lag))
    for key in tasks:
        if key.startswith('CONSTRUCCION:'):
            package = key.rsplit(':', 1)[1]
            days = math.ceil(160 / (6.4 * packages[package]['peak']))
            relations.append(((package, 'start'), (key, 'start'), days))
    durations = {}
    for key, task in tasks.items():
        if task['milestone']:
            continue
        days = task['work']
        if task['kind'] == 'phase':
            days = rank(task['finish']) - rank(task['start']) + 1
        durations[key] = max(1, days)
        relations.append(((key, 'start'), (key, 'finish'), durations[key] - 1))
    order, outgoing = topological(nodes, relations)
    releases = dict.fromkeys(nodes, start)
    limits = dict.fromkeys(nodes, rank(END))
    calendar_pins = {
        key: value for key, value in fixed.items()
        if not (key.startswith('EVID:') and key not in ('EVID:H7', 'EVID:H12'))
    }
    for key, day in calendar_pins.items():
        releases[key, 'start'] = limits[key, 'start'] = rank(day)
        if (key, 'finish') in nodes:
            releases[key, 'finish'] = limits[key, 'finish'] = rank(tasks[key]['finish'])
    # EVID:H2/H4/H5/H8/H10 se calcula desde los insumos, sin fijar la fecha publicada.
    for key in packages:
        last_month = int(estimates[key][3].rsplit('–', 1)[-1])
        limits[key, 'finish'] = rank(period(last_month)[1])
    for h in milestones:
        first, last = period(MONTHS[h])
        releases['ACT:' + h, 'start'] = max(releases['ACT:' + h, 'start'], rank(after(first - timedelta(days=1))))
        limits['ACT:' + h, 'start'] = min(limits['ACT:' + h, 'start'], rank(first if h in ('H6', 'H11') else last))
        if ('REG:' + h, 'start') in limits:
            limits['REG:' + h, 'start'] = rank(last)
    return order, outgoing, releases, limits, durations


def passes(network, days_by_package=None):
    order, outgoing, releases, limits, durations = network
    days_by_package = days_by_package or {}
    early, late = releases.copy(), limits.copy()

    def advance(a, b, lag, value):
        if a[0] == b[0] and a[1] == 'start' and b[1] == 'finish':
            days = days_by_package.get(a[0], durations[a[0]])
            civil_window = {'8.1.4': 8 * 7, '2.7.3': 6 * 7}.get(a[0])
            if civil_window is not None:
                return max(value + days - 1, rank(CAL[value] + timedelta(days=civil_window - 1)))
            return value + days - 1
        return value + lag

    for source in order:
        if source[0] in ('CUT:H7', 'CUT:H12'):
            early[source] = rank(allowed_cut(CAL[early[source] - 1]))
        for target, lag in outgoing[source]:
            early[target] = max(early[target], advance(source, target, lag, early[source]))
    for source in reversed(order):
        for target, lag in outgoing[source]:
            candidate = late[target] - (advance(source, target, lag, late[target]) - late[target])
            while advance(source, target, lag, candidate) > late[target]:
                candidate -= 1
            while candidate < late[target] and advance(source, target, lag, candidate + 1) <= late[target]:
                candidate += 1
            late[source] = min(late[source], candidate)
        if source[0] in ('CUT:H7', 'CUT:H12'):
            while rank(allowed_cut(CAL[late[source] - 1])) > late[source]:
                late[source] -= 1
    return early, late


def simulate(network, packages, estimates, milestones, samples, seed):
    rng = random.Random(seed)
    orders = {}
    for code, pkg in packages.items():
        lower, mode, upper = map(float, estimates[code][-4:-1])
        if not 0 <= lower <= mode <= upper:
            raise ValueError(f'Estimación PERT inválida: {code}')
        if upper == lower:
            continue
        scale = upper - lower
        orders[code] = (lower, scale, 1 + 4 * (mode - lower) / scale,
                        1 + 4 * (upper - mode) / scale, 6.4 * pkg['peak'])
    results = {h: [] for h in ORDER}
    with_corrections = dict.fromkeys(('H1', 'H7', 'H12'), 0)
    for _ in range(samples):
        sampled = {code: max(1, math.ceil((lo + spread * rng.betavariate(a, b)) / capacity))
                   for code, (lo, spread, a, b, capacity) in orders.items()}
        early, _ = passes(network, sampled)
        for h in ORDER:
            key = ('REG:' if milestones[h]['produccion'] else 'ACT:') + h
            results[h].append(early[key, 'start'])
        for h in with_corrections:
            correction_end = after(CAL[early['ACT:' + h, 'start']], 10)
            completion = allowed_cut(correction_end) if h != 'H1' else correction_end
            with_corrections[h] += completion <= milestones[h]['limite']
    return {
        h: {
            'probabilidad': sum(x <= rank(milestones[h]['limite']) for x in values) / samples,
            'p50': CAL[round(statistics.median(values))],
            'p90': CAL[sorted(values)[math.ceil(samples * .9) - 1]],
            'con_subsanacion': with_corrections[h] / samples if h in with_corrections else None,
        }
        for h, values in results.items()
    }


def export_tex(directory, result):
    def dmy(day):
        return day.strftime('%d-%m-%Y')

    def table(filename, title, label, widths, headers, records, landscape=False):
        lines = [rf'\begin{{tablalafrox}}{{{title}}}{{{label}}}',
                 '{' + widths + '}',
                 '{' + ' & '.join(r'\cab{' + header + '}' for header in headers) + '}']
        lines.extend('  ' + ' & '.join(map(str, row)) + r' \\' for row in records)
        lines.append(r'\end{tablalafrox}')
        if landscape:
            lines.insert(0, r'\begin{anexohorizontal}\setlength{\textwidth}{\linewidth}')
            lines.append(r'\end{anexohorizontal}')
        (directory / filename).write_text('\n'.join(lines) + '\n', encoding='utf-8')

    records = [(code, dmy(row['inicio_temprano']), dmy(row['fin_temprano']),
                dmy(row['inicio_tardio']), dmy(row['fin_tardio']), row['holgura'],
                dmy(row['inicio_nivelado']), dmy(row['fin_nivelado']))
               for code, row in result['base'].items()]
    table('tab_T15_cpm_detalle.tex',
          'Fechas tempranas, tardías y niveladas de los 171 paquetes con entregable. Fuente: red de las secciones 5.1 y 6.1.',
          'tab_T15_cpm_detalle', 'L{1.6cm} Y Y Y Y C{1.6cm} Y Y',
          ('EDT', 'Inicio temprano', 'Fin temprano', 'Inicio tardío', 'Fin tardío', 'Holgura hábil',
           'Inicio nivelado', 'Fin nivelado'), records, landscape=True)

    records = []
    for h in ORDER:
        row = result['pert_logico_sin_nivelacion'][h]
        effects = result['sensibilidad_dias'][h]
        stress, delay = max(effects.items(), key=lambda item: item[1])
        nominal = f"{row['probabilidad']:.1%}".replace('.', ',').replace('%', r'\%')
        correction = row['con_subsanacion']
        correction_text = '—' if correction is None else f'{correction:.1%}'.replace('.', ',').replace('%', r'\%')
        records.append((h, nominal, correction_text, dmy(row['p50']),
                        dmy(row['p90']), f'{stress} (+{delay} d.h.)' if delay else 'Sin desplazamiento'))
    table('tab_T15_pert_hitos.tex',
          f"Sensibilidad de los hitos. Fuente: simulación lógica con {result['muestras']} muestras y semilla {result['semilla']}.",
          'tab:T15-pert-hitos', 'L{0.85cm} L{1.6cm} L{2.0cm} L{1.9cm} L{1.9cm} Y',
          ('Hito', 'En plazo', 'Con subsanación', 'Mediana', 'Percentil 90', 'Mayor efecto de los tres escenarios'), records)

    records = [(h, dmy(r['nominal']), dmy(r['subsanacion_10']), dmy(r['limite']), r['margen'],
                dmy(r['ultimo_ingreso_con_subsanacion']))
               for h, r in result['subsanacion'].items()]
    table('tab_T15_subsanacion.tex',
          'Escenario con diez días hábiles adicionales de subsanación. Fuente: calendario nominal y restricciones de corte de la sección 5.1.',
          'tab:T15-subsanacion', 'L{0.85cm} Y Y Y L{1.5cm} Y',
          ('Hito', 'Nominal', 'Con subsanación', 'Límite contractual', 'Margen hábil', 'Último ingreso viable'), records)


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--output-dir', required=True, type=Path)
    parser.add_argument('--samples', type=int, default=10000)
    args = parser.parse_args()
    if args.samples < 1:
        parser.error('--samples debe ser positivo')
    tasks, edges, fixed, packages, milestones, estimates, _ = build()
    nominal = schedule(tasks, edges, fixed, packages, milestones, estimates)
    network = make_network(tasks, edges, fixed, packages, milestones, estimates)
    early, late = passes(network)
    order, outgoing, releases, limits, durations = network
    scenario_releases = releases.copy()
    for key in (*packages, *(key for key in tasks if key.startswith('EVID:'))):
        node = (key, 'start')
        scenario_releases[node] = max(scenario_releases[node], rank(tasks[key]['start']))
    sensitivity_network = order, outgoing, scenario_releases, limits, durations
    scenario_early, _ = passes(sensitivity_network)
    stresses = {
        'Integraciones y migración': ('5.2.', '5.3.', '5.4.'),
        'Pruebas de certificación': ('6.2.', '6.3.', '6.4.', '6.5.', '6.6.'),
        'Infraestructura y cadena de frío': ('8.1.', '8.2.', '8.3.', '8.4.', '8.6.', '8.7.', '2.7.'),
    }
    impacts = {h: {} for h in ORDER}
    for group, prefixes in stresses.items():
        worst = {code: math.ceil(float(estimates[code][-2]) / (6.4 * pkg['peak']))
                 for code, pkg in packages.items() if code.startswith(prefixes)}
        stressed, _ = passes(sensitivity_network, worst)
        for h in ORDER:
            event = ('REG:' if milestones[h]['produccion'] else 'ACT:') + h, 'start'
            impacts[h][group] = stressed[event] - scenario_early[event]
    details = {}
    for code in packages:
        details[code] = {
            'duracion': network[-1][code],
            'inicio_temprano': CAL[early[code, 'start']],
            'fin_temprano': CAL[early[code, 'finish']],
            'inicio_tardio': CAL[late[code, 'start']],
            'fin_tardio': CAL[late[code, 'finish']],
            'holgura': min(late[code, side] - early[code, side] for side in ('start', 'finish')),
            'inicio_nivelado': nominal[code]['inicio'],
            'fin_nivelado': nominal[code]['fin'],
        }
    scenarios = {}
    for h in ('H1', 'H7', 'H12'):
        row = milestones[h]
        end = after(row['acta'], 10)
        completion = allowed_cut(end) if row['produccion'] else end
        latest_submission = rank(row['limite'])
        while True:
            revised_act = after(CAL[latest_submission], 20)
            revised_completion = allowed_cut(revised_act) if row['produccion'] else revised_act
            if revised_completion <= row['limite']:
                break
            latest_submission -= 1
        scenarios[h] = {
            'nominal': row['produccion'] or row['acta'],
            'subsanacion_10': completion,
            'limite': row['limite'],
            'margen': rank(row['limite']) - rank(completion),
            'ultimo_ingreso_con_subsanacion': CAL[latest_submission],
        }
    result = {
        'base': details, 'subsanacion': scenarios, 'muestras': args.samples, 'semilla': 7,
        'pert_logico_sin_nivelacion': simulate(sensitivity_network, packages, estimates, milestones, args.samples, 7),
        'sensibilidad_dias': impacts,
    }
    assert len(details) == 171 and len(estimates) - len(details) == 59
    args.output_dir.mkdir(parents=True, exist_ok=True)
    export_tex(args.output_dir, result)
    (args.output_dir / 'cpm-pert-sd7.json').write_text(
        json.dumps(result, ensure_ascii=False, indent=2, default=str) + '\n', encoding='utf-8')
    print(json.dumps(scenarios, default=str))
    print('Paquetes con holgura logica negativa:', sum(r['holgura'] < 0 for r in details.values()))


if __name__ == '__main__':
    main()
