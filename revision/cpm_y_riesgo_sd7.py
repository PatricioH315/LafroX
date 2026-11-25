"""Calcula el CPM lógico y escenarios PERT del SD7 sin reemplazar la carta nivelada."""

import argparse
from datetime import timedelta
import json
import math
from pathlib import Path
import random
import statistics

import numpy as np
from scipy.stats import beta as beta_dist, norm

from edt_cpm_20261117 import (
    CAL, CAPS, END, MONTHS, ORDER, ROOT, START, TABLES, after, allowed_cut, build, capacity,
    endpoints, period, rank, references, rows, schedule, topological,
)

# Supuestos de la simulación ampliada (T-15, sección 5.4).
CORRELACION_ESFUERZO = 0.5      # mismo equipo y mismas tasas: los desvíos de esfuerzo no son independientes
PROBABILIDAD_OBSERVACION = 0.30  # acta con al menos una observación bloqueante (art. 18.3)
SUBSANACION_DIAS = {'H1': 5, 'H7': 5, 'H12': 5}  # entrega por incrementos (T-17, 2.3 y 2.4)
SUBSANACION_DIAS_BASE = 10       # BA, art. 18.3
HITOS_SIN_REVISION = ('H6', 'H11')  # inicios contractuales de marcha blanca


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


def passes(network, days_by_package=None, delays=None, backward=True):
    order, outgoing, releases, limits, durations = network
    days_by_package = days_by_package or {}
    delays = delays or {}
    early, late = releases.copy(), limits.copy()

    def advance(a, b, lag, value):
        if a[0] == b[0] and a[1] == 'start' and b[1] == 'finish':
            days = days_by_package.get(a[0], durations[a[0]])
            civil_window = {'8.1.4': 8 * 7, '2.7.3': 6 * 7}.get(a[0])
            if civil_window is not None:
                return max(value + days - 1, rank(CAL[value] + timedelta(days=civil_window - 1)))
            return value + days - 1
        return value + lag + delays.get(b, 0)

    for source in order:
        if source[0] in ('CUT:H7', 'CUT:H12'):
            early[source] = rank(allowed_cut(CAL[early[source] - 1]))
        for target, lag in outgoing[source]:
            early[target] = max(early[target], advance(source, target, lag, early[source]))
    if not backward:
        return early, None
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


def simulate(network, packages, estimates, milestones, samples, seed,
             rho=0.0, observation=0.0):
    """Muestrea el esfuerzo con beta PERT correlacionada (cópula normal, rho) y,
    con probabilidad `observation`, una subsanación en cada acta revisada por el CLIENTE."""
    rng = np.random.default_rng(seed)
    codes, lower, spread, alpha, beta_, capacity_ = [], [], [], [], [], []
    for code, pkg in packages.items():
        lo, mode, up = map(float, estimates[code][-4:-1])
        if not 0 <= lo <= mode <= up:
            raise ValueError(f'Estimación PERT inválida: {code}')
        if up == lo:
            continue
        scale = up - lo
        codes.append(code)
        lower.append(lo)
        spread.append(scale)
        alpha.append(1 + 4 * (mode - lo) / scale)
        beta_.append(1 + 4 * (up - mode) / scale)
        capacity_.append(6.4 * pkg['peak'])
    common = rng.standard_normal((samples, 1))
    own = rng.standard_normal((samples, len(codes)))
    quantiles = norm.cdf(math.sqrt(rho) * common + math.sqrt(1 - rho) * own)
    effort = np.array(lower) + np.array(spread) * beta_dist.ppf(quantiles, alpha, beta_)
    days = np.maximum(1, np.ceil(effort / np.array(capacity_))).astype(int)
    reviewed = [h for h in ORDER if h not in HITOS_SIN_REVISION]
    observed = rng.random((samples, len(reviewed))) < observation
    results = {h: [] for h in ORDER}
    flags = {h: [] for h in reviewed}
    for i in range(samples):
        sampled = dict(zip(codes, days[i].tolist()))
        delays = {('ACT:' + h, 'start'): SUBSANACION_DIAS.get(h, SUBSANACION_DIAS_BASE)
                  for j, h in enumerate(reviewed) if observed[i, j]}
        early, _ = passes(network, sampled, delays, backward=False)
        for h in ORDER:
            key = ('REG:' if milestones[h]['produccion'] else 'ACT:') + h
            results[h].append(early[key, 'start'])
        for j, h in enumerate(reviewed):
            flags[h].append(bool(observed[i, j]))
    summary = {}
    for h, values in results.items():
        limit = rank(milestones[h]['limite'])
        ok = [x <= limit for x in values]
        hit = [o for o, f in zip(ok, flags.get(h, [])) if f]
        summary[h] = {
            'probabilidad': sum(ok) / samples,
            'si_se_observa': sum(hit) / len(hit) if hit else None,
            'p50': CAL[round(statistics.median(values))],
            'p90': CAL[sorted(values)[math.ceil(samples * .9) - 1]],
        }
    return summary


def breaking_overrun(network, packages, estimates, milestones, step=5, ceiling=200):
    """Primer sobreesfuerzo uniforme (en % sobre M, en pasos de `step`) que deja cada hito fuera de plazo."""
    found = {}
    for pct in range(0, ceiling + 1, step):
        factor = 1 + pct / 100
        days = {code: max(1, math.ceil(float(estimates[code][-3]) * factor / (6.4 * pkg['peak'])))
                for code, pkg in packages.items()}
        early, _ = passes(network, days, backward=False)
        for h in ORDER:
            key = ('REG:' if milestones[h]['produccion'] else 'ACT:') + h, 'start'
            if h not in found and early[key] > rank(milestones[h]['limite']):
                found[h] = pct
        if len(found) == len(ORDER):
            break
    return {h: found.get(h) for h in ORDER}


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
          'Fechas tempranas, tardías y niveladas de los 171 paquetes con entregable. Fuente: cálculo propio de fechas a partir de las dependencias entre paquetes del Anexo 7.B del Subdocumento 7.',
          'tab_T15_cpm_detalle', 'L{1.6cm} Y Y Y Y C{1.6cm} Y Y',
          ('EDT', 'Inicio temprano', 'Fin temprano', 'Inicio tardío', 'Fin tardío', 'Holgura hábil',
           'Inicio nivelado', 'Fin nivelado'), records, landscape=True)

    def pct(value):
        return '—' if value is None else f'{value:.1%}'.replace('.', ',').replace('%', r'\%')

    records = []
    for h in ORDER:
        effort = result['pert_solo_esfuerzo'][h]
        row = result['pert_con_revision'][h]
        effects = result['sensibilidad_dias'][h]
        stress, delay = max(effects.items(), key=lambda item: item[1])
        overrun = result['sobreesfuerzo_de_quiebre'][h]
        overrun_text = rf'+{overrun} \%' if overrun is not None else '—'
        records.append((h, pct(effort['probabilidad']), pct(row['probabilidad']), pct(row['si_se_observa']),
                        dmy(row['p90']), overrun_text,
                        f'{stress} (+{delay} d.h.)' if delay else 'Sin desplazamiento'))
    samples = f"{result['muestras']:,}".replace(',', '.')
    table('tab_T15_pert_hitos.tex',
          f'Probabilidad de cumplir el plazo de cada hito. Fuente: cálculo propio mediante simulación de {samples} muestras sobre las dependencias del Anexo 7.B del Subdocumento 7.',
          'tab:T15-pert-hitos', 'L{0.8cm} C{1.35cm} C{1.75cm} C{1.6cm} L{1.75cm} C{1.75cm} Y',
          ('Hito', 'Solo esfuerzo', 'Con revisión del CLIENTE', 'Si el acta se observa', 'Percentil 90',
           'Exceso que agota el margen', 'Mayor efecto de los tres escenarios'), records)

    records = [(h, dmy(r['nominal']), dmy(r['subsanacion_10']), dmy(r['limite']), r['margen'],
                dmy(r['ultimo_ingreso_con_subsanacion']))
               for h, r in result['subsanacion'].items()]
    table('tab_T15_subsanacion.tex',
          'Escenario con diez días hábiles adicionales de subsanación. Fuente: cálculo propio a partir del calendario nominal y los plazos de revisión del artículo 18 de las Bases Administrativas.',
          'tab:T15-subsanacion', 'L{0.85cm} Y Y Y L{1.5cm} Y',
          ('Hito', 'Nominal', 'Con subsanación', 'Límite contractual', 'Margen hábil', 'Último ingreso viable'), records)


def minimum_family_capacity(packages, role):
    max_peak = sum(package['peak'] for package in packages.values() if package['role'] == role)
    for cap in range(1, max_peak + 1):
        try:
            capacity(packages, role, cap)
        except ValueError:
            continue
        return cap
    raise ValueError(f'No se pudo distribuir el esfuerzo de {role} en las ventanas declaradas.')


def recovery_options(tasks, current_packages, milestones, scenarios):
    # Alternativa de cálculo. Su activación exige redistribuir las HH de marzo a
    # febrero y aprobar la disponibilidad de Jefatura/PMO y Calidad.
    h1_finish = scenarios['H1']['ultimo_ingreso_con_subsanacion']
    affected = ('1.2.2', '1.2.3', '1.2.4', '2.1.3')
    duration = max(tasks[code]['work'] for code in affected)
    h1_start = CAL[rank(h1_finish) - duration + 1]
    candidate = build(package_windows=dict.fromkeys(affected, (h1_start, h1_finish)))
    new_tasks, edges, fixed, packages, new_milestones, estimates, _ = candidate
    schedule(new_tasks, edges, fixed, packages, new_milestones, estimates)
    capacity(packages, 'CAL', CAPS['CAL'])
    h1_act = new_milestones['H1']['acta']
    corrected = after(h1_act, 10)
    assert corrected <= milestones['H1']['limite']

    h12_last = scenarios['H12']['ultimo_ingreso_con_subsanacion']
    h12_close = h12_last - timedelta(days=1)
    h12_act = after(h12_last, 10)
    h12_cut_after_correction = allowed_cut(after(h12_act, 10))
    return {
        'H1': {'paquetes': affected, 'inicio': h1_start, 'entrega': h1_finish,
               'acta': h1_act, 'acta_con_subsanacion': corrected,
               'margen_habil': rank(milestones['H1']['limite']) - rank(corrected),
               'minimo_agregado_jp_carta_actual': minimum_family_capacity(current_packages, 'JP'),
               'minimo_agregado_jp_alternativa': minimum_family_capacity(packages, 'JP'),
               'hh_de_paquetes_afectados_por_familia': {
                   role: sum(float(packages[code]['hh']) for code in affected if packages[code]['role'] == role)
                   for role in ('JP', 'CAL')}},
        'H7': {'entrega': milestones['H7']['entrega'], 'margen_habil': scenarios['H7']['margen']},
        'H12': {'ultimo_ingreso': h12_last, 'inicio_evidencia_continua': h12_close - timedelta(days=27),
                'ultimo_cierre_de_evidencia': h12_close,
                'cierres_publicados': {key: tasks[key]['finish'] for key in ('EVID:H12', '9.5.4', '6.8.6')},
                'acta_nominal_condicionada': h12_act,
                'corte_con_subsanacion_condicionado': h12_cut_after_correction,
                'margen_habil_condicionado': rank(milestones['H12']['limite']) - rank(h12_cut_after_correction),
                'traspaso_termina_antes_del_ingreso': tasks['9.5.4']['finish'] <= h12_close,
                '686_disponible_al_ingreso': tasks['6.8.6']['finish'] < h12_last,
                '686_disponible_antes_de_firmar': tasks['6.8.6']['finish'] < h12_act},
    }


def pert_basis(packages, estimates):
    modules = {cells[0] for cells in rows(TABLES / 'tab_T15_tamano.tex')}
    risks = (ROOT / TABLES / 'tab_T15_pert_riesgo.tex').read_text(encoding='utf-8')
    specific = modules | {
        code for line in risks.splitlines() if line.lstrip()[:1].isdigit()
        for code in references(line.split('&', 1)[0].strip().replace(' a ', '–'))
    }
    if specific - packages.keys():
        raise ValueError('Los fundamentos PERT citan paquetes ausentes de la carta.')
    fixed = {code for code in packages if estimates[code][-4] == estimates[code][-2]}
    return {'con_fundamento_especifico': sorted(specific),
            'sin_variacion_de_esfuerzo_en_la_base': sorted(fixed - specific),
            'pendientes_de_fundamento_individual': sorted(packages.keys() - specific - fixed)}


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
        'supuestos_simulacion': {
            'correlacion_esfuerzo': CORRELACION_ESFUERZO,
            'probabilidad_observacion': PROBABILIDAD_OBSERVACION,
            'subsanacion_dias': {h: SUBSANACION_DIAS.get(h, SUBSANACION_DIAS_BASE)
                                 for h in ORDER if h not in HITOS_SIN_REVISION},
        },
        'pert_solo_esfuerzo': simulate(sensitivity_network, packages, estimates, milestones, args.samples, 7,
                                       rho=CORRELACION_ESFUERZO),
        'pert_con_revision': simulate(sensitivity_network, packages, estimates, milestones, args.samples, 7,
                                      rho=CORRELACION_ESFUERZO, observation=PROBABILIDAD_OBSERVACION),
        'sobreesfuerzo_de_quiebre': breaking_overrun(sensitivity_network, packages, estimates, milestones),
        'sensibilidad_dias': impacts,
        'alternativas_subsanacion': recovery_options(tasks, packages, milestones, scenarios),
        'fundamento_pert': pert_basis(packages, estimates),
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
