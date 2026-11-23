"""Valida la red y genera las tablas CPM y los datos de la carta del SD7."""
from pathlib import Path
from datetime import date, timedelta
from decimal import Decimal
from collections import defaultdict, deque
from bisect import bisect_left, bisect_right
import argparse
import calendar, json, math, re

ROOT = Path(__file__).resolve().parents[1]

def rows(relative):
    text = (ROOT / relative).read_text(encoding='utf-8')
    result = []
    for line in text.splitlines():
        if re.match(r'^\s*\d+\.\d+\.\d+\s*&', line):
            result.append([c.strip() for c in line.strip().removesuffix('\\\\').split(' & ')])
    return result

def easter(y):
    a=y%19; b=y//100; c=y%100; d=b//4; e=b%4; f=(b+8)//25
    g=(b-f+1)//3; h=(19*a+b-d-g+15)%30; i=c//4; k=c%4
    l=(32+2*e+2*i-h-k)%7; m=(a+11*h+22*l)//451
    n=h+l-7*m+114
    return date(y,n//31,n%31+1)

def holidays(y):
    result={date(y,m,d) for m,d in [(1,1),(5,1),(5,21),(7,16),(8,15),(9,18),(9,19),(11,1),(12,8),(12,25)]}
    result |= {easter(y)-timedelta(days=2), easter(y)-timedelta(days=1)}
    # Ley 19.668: martes a jueves al lunes anterior; viernes al siguiente.
    for m,d in [(6,29),(10,12)]:
        x=date(y,m,d)
        if x.weekday() in (1,2,3): x-=timedelta(days=x.weekday())
        elif x.weekday()==4: x+=timedelta(days=3)
        result.add(x)
    # Ley 20.299: martes al viernes anterior; miércoles al viernes siguiente.
    x=date(y,10,31)
    if x.weekday()==1:x-=timedelta(days=4)
    elif x.weekday()==2:x+=timedelta(days=2)
    result.add(x)
    if date(y,9,18).weekday()==1:result.add(date(y,9,17))
    if date(y,9,18).weekday()==2:result.add(date(y,9,20))
    if date(y,9,18).weekday()==5:result.add(date(y,9,17))
    if date(y,1,1).weekday()==6:result.add(date(y,1,2))
    solstice={2027:21,2028:20,2029:20,2030:21,2031:21,2032:20}
    result.add(date(y,6,solstice[y]))
    return result

HOLIDAYS=set().union(*(holidays(y) for y in range(2027,2033)))
all_days=[date(2027,1,1)+timedelta(days=n) for n in range((date(2032,12,31)-date(2027,1,1)).days+1)]
CAL=[d for d in all_days if d.weekday()<5 and d not in HOLIDAYS]
def ix(d):return bisect_left(CAL,d)
def parse(s):return date(*map(int,s.split('-')[::-1]))
def clean(s):return s.replace(r'\allowbreak{}','')


START = date(2027, 2, 1)
END = date(2031, 9, 30)
TABLES = Path('formulario-t15/tablas')
ORDER = ('H1', 'H2', 'H3', 'H4', 'H5', 'H6', 'H8', 'H7', 'H9', 'H10', 'H11', 'H12')
MONTHS = dict(zip(ORDER, (2, 4, 6, 10, 12, 13, 14, 16, 17, 18, 19, 21)))
REVIEW = 10
CAPS = {'DES': 33, 'CAL': 13}


def workdays(start, end):
    return ix(end + timedelta(days=1)) - ix(start)


def after(day, count=1):
    return CAL[ix(day + timedelta(days=1)) + count - 1]


def allowed_cut(act):
    cut = after(act)
    while cut.month in (9, 12) or workdays(cut.replace(day=1), cut) < 4:
        cut = after(cut)
    return cut


def period(number):
    month_index = START.year * 12 + START.month + number - 2
    year, zero_month = divmod(month_index, 12)
    return date(year, zero_month + 1, 1), date(year, zero_month + 1, calendar.monthrange(year, zero_month + 1)[1])


def spanish_hh(value):
    return Decimal(value.replace('.', '').replace(',', '.'))


def current_dictionary():
    return {
        cells[0]: (cells[1].replace(r'\allowbreak{}', '').replace(r'\%', '%'), cells[4])
        for index in range(1, 11)
        for cells in rows(f'formulario-t14/tablas/dic_prod_{index}.tex')
    }


def references(text):
    """Códigos EDT de una cláusula, incluidos rangos dentro de una cuenta."""
    for match in re.finditer(r'\d+\.\d+(?:\.\d+)?(?:–\d+\.\d+(?:\.\d+)?)?', text):
        members = match[0].split('–')
        if len(members) == 1:
            yield members[0]
        else:
            prefix, lower = members[0].rsplit('.', 1)
            other, upper = members[1].rsplit('.', 1)
            if prefix != other:
                raise ValueError(f'Rango EDT inválido: {match[0]}')
            yield from (f'{prefix}.{n}' for n in range(int(lower), int(upper) + 1))


def capacity(packages, role, cap):
    """Distribuye centésimas de HH entre días por flujo máximo."""
    graph = defaultdict(dict)
    origin, sink = 'origen', 'destino'

    def connect(a, b, limit):
        graph[a][b] = limit
        graph[b][a] = 0

    demand = 0
    for code, item in packages.items():
        if item['role'] != role:
            continue
        effort = int(item['hh'] * 100)
        demand += effort
        connect(origin, code, effort)
        for day in CAL[ix(item['start']):ix(item['finish'] + timedelta(days=1))]:
            connect(code, day, item['peak'] * 640)
            if sink not in graph[day]:
                connect(day, sink, cap * 640)

    delivered = 0
    while delivered < demand:
        parents = {origin: None}
        queue = deque([origin])
        while queue and sink not in parents:
            a = queue.popleft()
            for b, remaining in graph[a].items():
                if remaining and b not in parents:
                    parents[b] = a
                    queue.append(b)
        if sink not in parents:
            missing = {code: value / 100 for code, value in graph[origin].items() if value}
            raise ValueError(f'{role}: HH sin colocar en su ventana: {missing}')
        path = []
        b = sink
        while b != origin:
            a = parents[b]
            path.append((a, b))
            b = a
        shift = min(graph[a][b] for a, b in path)
        for a, b in path:
            graph[a][b] -= shift
            graph[b][a] += shift
        delivered += shift
    daily = {day.isoformat(): effort / 100 for day, effort in graph[sink].items() if effort}
    return {'tope_personas': cap, 'hh_validadas': delivered / 100,
            'pico_personas_equivalentes': max(daily.values(), default=0) / 6.4, 'hh_diarias': daily}


def build():
    dictionary = current_dictionary()
    estimate = {r[0]: r for r in rows(TABLES / 'tab_T15_2.tex')}
    packages = {}
    for code, role, people, hh, start, finish, preds in rows(TABLES / 'tab_T15_paquetes.tex'):
        if code in packages:
            raise ValueError(f'Fila duplicada: {code}')
        packages[code] = dict(role=role, peak=int(people.split('/')[-1].strip()), hh=spanish_hh(hh),
                              start=parse(start), finish=parse(finish), predicates=clean(preds))
    assert len(dictionary) == len(estimate) == 230 and dictionary.keys() == estimate.keys()
    assert len({code.rsplit('.', 1)[0] for code in dictionary}) == 60 and len(packages) == 171
    assert set(dictionary) == set(packages) | {r[0] for r in rows(TABLES / 'tab_T15_10.tex')}
    assert sum(Decimal(r[-1]) for r in estimate.values()) == Decimal('188123.03')
    baseline = Decimal('203548.62')
    assert sum(Decimal(r[-1]) for r in estimate.values()) + sum(map(Decimal, ('128', '9336', '3072', '2889.59'))) == baseline

    tasks = {}
    edges = {}
    fixed = {}
    def task(key, title, first, last=None, *, work=0, note='', pin=False, kind='event'):
        if key in tasks:
            raise ValueError(f'Tarea duplicada: {key}')
        tasks[key] = dict(name=title, start=first, finish=last if last is not None else first,
                          milestone=last is None, work=work, note=note, kind=kind)
        if pin:
            fixed[key] = first

    def link(a, b, kind='FC', lag=None, reason=''):
        if a == b or a not in tasks or b not in tasks:
            raise ValueError(f'Referencia inválida: {a} → {b} ({reason})')
        delay = int(kind == 'FC') if lag is None else lag
        key = a, b, kind
        if key not in edges or delay > edges[key]['lag']:
            edges[key] = dict(source=a, target=b, kind=kind, lag=delay, reason=reason)

    for code, p in packages.items():
        days = workdays(p['start'], p['finish'])
        minimum = math.ceil(p['hh'] / (Decimal('6.4') * p['peak']))
        assert p['start'] in CAL and p['finish'] in CAL and days >= minimum, (code, days, minimum)
        assert p['hh'] == Decimal(estimate[code][-1]), code
        title, owner = dictionary[code]
        task(code, f'{code} {title}', p['start'], p['finish'], work=minimum, kind='package',
             note=f"{p['hh']} HH · responsable {owner} · ejecución {p['role']} · {p['predicates']}")

    phase = [
        ('DES:E1', 'Etapa 1 · Desarrollo (meses 1 a 12)', START, period(12)[1]),
        ('DES:E2', 'Etapa 2 · Desarrollo (meses 13 a 18)', period(13)[0], period(18)[1]),
        ('9.2.1', '9.2.1 Marcha blanca de la Etapa 1', period(13)[0], period(15)[1]),
        ('9.2.2', '9.2.2 Marcha blanca de la Etapa 2', period(19)[0], period(20)[1]),
        ('9.5.4', '9.5.4 Traspaso al equipo de TI del CLIENTE', period(15)[0], period(20)[1]),
        ('10.5.1', '10.5.1 Traspaso de reversibilidad y acompañamiento de salida', period(55)[0], END),
    ]
    for key, name, first, last in phase:
        task(key, name, first, last, pin=True, kind='phase')
    first, last = (int(month) for month in estimate['2.1.4'][3].split('–'))
    task('2.1.4', '2.1.4 Captura de reglas de ruteo', period(first)[0], period(last)[1], pin=True, kind='phase')

    def event(key, name, date_value, *, pin=False, note=''):
        task(key, name, date_value, pin=pin, note=note)
        return key

    def milestone(h, control, deliver, *, minimum_act=None, fixed_start=False):
        act = deliver if fixed_start else max(after(deliver, REVIEW), minimum_act or deliver)
        event(f'ENT:{h}', f'{h} · Entrega de expediente', deliver, pin=fixed_start)
        if fixed_start:
            event(f'ACT:{h}', f'{h} · Inicio contractual de marcha blanca', act, pin=True)
        else:
            review_end = after(deliver, REVIEW)
            task(f'REV:{h}', f'{h} · Revisión de la Contraparte (10 días hábiles)', after(deliver), review_end, work=REVIEW)
            link(f'ENT:{h}', f'REV:{h}', reason='Art. 18.3: revisión tras la entrega')
            event(f'ACT:{h}', f'{h} · Firma del acta', act, pin=minimum_act is not None)
            link(f'REV:{h}', f'ACT:{h}', lag=0, reason='Firma tras los diez días de revisión')
        return dict(hito=h, entrega=deliver, acta=act, produccion=None, control=control)

    evidence = {
        'H1': ('2.1.3', '1.2.4'),
        'H2': ('2.8.1',),
        'H3': ('3.1.1', '3.1.2', '3.1.3', '3.1.5', '8.7.3'),
        'H4': ('6.1.1',),
        'H5': ('6.7.1',),
        'H8': ('2.8.2',),
        'H9': ('6.1.2',),
        'H10': ('6.7.2',),
    }
    internal = {
        'H2': ('2027-04-26', 'Expediente de arquitectura, seguridad y datos; cierre administrativo posterior'),
        'H4': ('2027-10-20', 'Versiones integradas en QA, informes y pruebas'),
        'H5': ('2027-12-01', 'Pruebas aprobadas de las cuentas 6.2 a 6.6 e informe de certificación 6.7.1'),
        'H8': ('2028-02-24', 'Línea base y diseño detallado; cierre administrativo posterior'),
        'H10': ('2028-06-27', 'Integración y pruebas aprobadas; cierre documental posterior'),
    }
    evidence_inputs = {
        'H2': ('2.2.1', '2.2.2', '2.2.3', '2.3.1', '2.3.3', '2.3.4'),
        'H4': ('3.3.4', '3.3.5', '3.3.6', '5.2.1', '5.2.2', '5.2.3', '5.2.4'),
        'H5': ('6.2.1', '6.2.2', '6.3.1', '6.4.1', '6.5.1', '6.6.1'),
        'H8': ('2.1.2', '2.2.4'),
        'H10': ('6.1.2', '6.2.3', '6.3.2', '6.4.2', '6.5.2', '6.6.2'),
    }
    results = {}
    for h, codes in evidence.items():
        first = max(packages[c]['finish'] for c in codes)
        deliver = date.fromisoformat(internal[h][0]) if h in internal else after(first) if h == 'H3' else first
        control = ' y '.join(codes) if h != 'H3' else '3.1.1–3.1.3, 3.1.5 y 8.7.3'
        results[h] = milestone(h, control, deliver, minimum_act=date(2028, 1, 3) if h == 'H5' else None)
        for code in codes:
            if h in internal:
                stop = event(f'EVID:{h}', f'{h} · Evidencia disponible ({code})', deliver, pin=True, note=internal[h][1])
                link(code, stop, 'CC', reason='Preparación anterior a evidencia')
                link(stop, code, 'CF', lag=0, reason='La evidencia precede el cierre interno')
                link(stop, f'ENT:{h}', 'CC', reason='Evidencia disponible al ingreso')
                for source in evidence_inputs[h]:
                    link(source, stop, reason='Insumo de la evidencia de entrega')
            else:
                link(code, f'ENT:{h}', lag=int(h == 'H3'), reason='Expediente con entregables comprobados')
    # Las aristas de paquete a evidencia y de evidencia al fin del mismo paquete
    # se validan en los extremos (inicio/fin). En .gan se exporta la primera.
    for h, month_number, phase_key, prerequisites in (
        ('H6', 13, '9.2.1', ('ACT:H5', '5.4.5', '9.1.1', '9.1.2')),
        ('H11', 19, '9.2.2', ('ACT:H10', '5.3.1', '9.1.3')),
    ):
        results[h] = milestone(h, 'Inicio contractual fijo', period(month_number)[0], fixed_start=True)
        for key in prerequisites:
            link(key, f'ACT:{h}', reason='D-25 / D-32: prerrequisito de marcha blanca')
        link(f'ENT:{h}', f'ACT:{h}', 'CC', reason='Hito fijo')
        link(f'ACT:{h}', phase_key, 'CC', reason='Inicio de marcha blanca')

    for h, phase_key, accept, ready in (
        ('H7', '9.2.1', '9.4.1', ('9.5.7',)),
        ('H12', '9.2.2', '9.4.2', ('9.4.3', '9.5.4', '9.5.8')),
    ):
        close = tasks[phase_key]['finish']
        event(f'EVID:{h}', f'{h} · Cierre de cuatro semanas de evidencia', close, pin=True)
        result = milestone(h, f'{phase_key} y {accept}', after(close))
        cut = allowed_cut(result['acta'])
        assert (packages[accept]['start'], packages[accept]['finish']) == (result['entrega'], cut)
        result['produccion'] = cut
        results[h] = result
        link(phase_key, f'EVID:{h}', lag=0, reason='Cierre de evidencia de marcha blanca')
        link(f'EVID:{h}', f'ENT:{h}', reason='Ingreso posterior al cierre')
        for key in ready:
            link(key, f'ENT:{h}', reason='Evidencia exigida al ingreso')
        event(f'CUT:{h}', f'{h} · Paso a producción', cut)
        event(f'REG:{h}', f'{h} · Registro de producción y cumplimiento', cut)
        link(f'ACT:{h}', f'CUT:{h}', reason='Corte autorizado fuera de despacho')
        link(f'CUT:{h}', f'REG:{h}', 'CC', reason='Registro del corte en el expediente')
        link(f'ENT:{h}', accept, 'CC', reason='Inicio del seguimiento del expediente')
        link(f'REG:{h}', accept, 'CF', lag=0, reason='Registro al cierre del seguimiento')
    link('6.8.6', 'ACT:H12', reason='Verificación anterior a la firma; confirmar si se exige al ingreso')
    event('CADENAS', 'E2 · Cadenas habilitadas antes de F − 28', date(2028, 8, 31), pin=True)
    link('5.3.2', 'CADENAS', reason='D-51: entrega de integración de cadenas')
    link('CADENAS', 'EVID:H12', reason='D-51: alcance habilitado antes de evidencia final')

    activation = max(after(results['H2']['acta']), date(2027, 5, 12))
    event('QA:3.1.4', '3.1.4 · Habilitación de la cadena para QA', activation)
    link('3.1.4', 'QA:3.1.4', 'CC', reason='Preparación técnica anterior a la activación')
    link('ACT:H2', 'QA:3.1.4', reason='Aprobación de arquitectura, seguridad y datos')
    link('QA:3.1.4', '3.1.4', 'CF', lag=0, reason='Activación antes de cerrar el paquete')
    link('3.1.4', '3.1.1', reason='Cadena operativa para desplegar en Desarrollo y QA')
    event('MONTAJE', '8.4.4 · Rack R01 montado', date(2027, 6, 9), pin=True)
    link('8.4.4', 'MONTAJE', 'CC', reason='Montaje dentro de la ventana del paquete')
    sunday = results['H3']['acta'] + timedelta(days=(6 - results['H3']['acta'].weekday()) % 7 or 7)
    while sunday in HOLIDAYS or sunday.month in (9, 12) or workdays(sunday.replace(day=1), sunday) < 3:
        sunday += timedelta(days=7)
    assert sunday < tasks['9.2.1']['start'] and packages['8.4.4']['finish'] == after(sunday)
    event('ERP', '8.4.4 · Traslado dominical del ERP a R01', sunday, pin=True,
          note='Ventana especial sin cambios de software; respaldo completo verificado.')
    link('MONTAJE', 'ERP', reason='Rack equipado antes de trasladar el servidor')
    link('ACT:H3', 'ERP', reason='SD4 y T-11: traslado después de H3')
    link('ERP', '8.4.4', 'CF', lag=0, reason='Registro posterior al traslado')
    link('8.4.4', 'ACT:H6', reason='Traslado y registro antes de marcha blanca Talca')

    event('KITS', '8.6.4 · Recepción parcial de cuatro kits', date(2027, 9, 30), pin=True)
    link('8.6.4', 'KITS', 'CC', reason='Recepción parcial dentro del suministro')
    link('KITS', '2.7.3', reason='D-37: kits recibidos antes del piloto')
    link('ACT:H4', '2.7.3', reason='D-37: versión integrada y aprobada')
    event('OLA3', 'E1 · Puerta de la ola de reparto', date(2028, 2, 29), pin=True)
    for key in ('2.7.3', '8.6.4', '9.7.1', '9.7.2'):
        link(key, 'OLA3', reason='D-27 / D-38: puertas de la ola de reparto')
    link('OLA3', 'EVID:H7', reason='Olas completas para evidencia final')

    def interface(pred, target):
        p, t = packages[pred], packages[target]
        contracts = CAL[rank(p['start']) + math.ceil(160 / (6.4 * p['peak'])) - 1]
        internal_contracts = CAL[rank(t['start']) + math.ceil(160 / (6.4 * t['peak'])) - 1]
        integration = CAL[rank(t['finish']) - math.ceil(80 / (6.4 * t['peak'])) + 1]
        # Un incremento probado puede alimentar la integración antes del acta del paquete completo.
        delivery = min(p['finish'], CAL[rank(integration) - 1])
        keys = {name: f'{name}:{pred}:{target}' for name in ('CONTRATO', 'CONSTRUCCION', 'INTERFAZ', 'INTEGRACION')}
        event(keys['CONTRATO'], f'{pred} → {target} · Contrato de interfaz disponible', contracts)
        event(keys['CONSTRUCCION'], f'{target} · Construcción dependiente de {pred}', after(max(contracts, internal_contracts)))
        event(keys['INTERFAZ'], f'{pred} → {target} · Incremento para integración', delivery)
        event(keys['INTEGRACION'], f'{target} · Integración con {pred}', integration)
        link(pred, keys['CONTRATO'], 'CC', reason='Preparación del contrato de interfaz')
        link(keys['CONTRATO'], keys['CONSTRUCCION'], reason='Contrato antes de construir')
        link(keys['CONTRATO'], keys['INTERFAZ'], reason='Incremento posterior al contrato')
        link(keys['CONSTRUCCION'], keys['INTEGRACION'], 'CC', reason='Construcción previa a la integración')
        link(keys['INTERFAZ'], keys['INTEGRACION'], reason='Incremento probado antes de integrar')
        link(keys['INTERFAZ'], pred, 'CF', lag=0, reason='Incremento anterior o coincidente con el cierre')
        link(keys['INTEGRACION'], target, 'CF', lag=0, reason='Integración dentro de la ventana de trabajo')

    def dependency(pred, target, clause):
        if pred == '8.4.4' and target.startswith('8.7.'):
            link('MONTAJE', target, reason='D-12: montaje antes de configurar')
        elif pred in ('2.8.1', '2.8.2', '6.7.1', '6.7.2'):
            gate = {'2.8.1': 'H2', '2.8.2': 'H8', '6.7.1': 'H5', '6.7.2': 'H10'}[pred]
            link(f'ACT:{gate}', target, reason='Aprobación formal previa')
        elif '(QA)' in clause:
            link(pred, target, 'FF', lag=0, reason='Integración y entrega en QA')
        elif '(interfaz)' in clause:
            interface(pred, target)
        elif 'por etapa' in clause:
            link(pred, target, 'CC', reason='D-01: preparación por etapa')
            link('ACT:H1', target, 'FF', lag=0, reason='D-01: aprobación antes del cierre')
        elif any(s in clause for s in ('protocolo inicial', 'contrato de evidencia', 'circuito mínimo', 'parámetros aprobados', 'prototipo inicial', 'diseño validado')):
            link(pred, target, 'CC', reason=clause)
            link(pred, target, 'FF', lag=0, reason='Entregable precedente antes del cierre')
        elif re.search(r'\bCC\b', clause):
            link(pred, target, 'CC', reason=clause)
        else:
            link(pred, target, reason=clause)

    for code, p in packages.items():
        if code in ('9.4.1', '9.4.2'):
            continue
        for clause in re.split(r',\s*(?![^()]*\))', p['predicates'].split(';')[0]):
            for pred in references(clause):
                candidates = [pred] if pred in tasks else [k for k in packages if k.startswith(pred + '.')]
                if not candidates:
                    raise ValueError(f'{code}: no se encuentra la predecesora {pred}')
                for predecessor in candidates:
                    if predecessor != code:
                        dependency(predecessor, code, clause)

    cut_e1, cut_e2 = (results[h]['produccion'] for h in ('H7', 'H12'))
    task('9.3.1', '9.3.1 Estabilización y soporte puente E1', cut_e1, period(20)[1], pin=True, kind='phase')
    task('TRANS', 'Mes 21 · Cobertura de transición previa al corte E2', period(21)[0], cut_e2 - timedelta(days=1), pin=True, kind='phase')
    task('9.3.2', '9.3.2 Estabilización de la Etapa 2', cut_e2, period(22)[1], pin=True, kind='phase')
    task('OP', 'Producto 10 · Operación con ambos alcances (meses 21 a 56)', cut_e2, END, pin=True, kind='phase')
    for a, b in (('CUT:H7', '9.3.1'), ('CUT:H12', '9.3.2'), ('CUT:H12', 'OP')):
        link(a, b, 'CC', reason='Inicio simultáneo al corte')
    link('TRANS', 'OP', reason='Continuidad de cobertura del mes 21')
    return tasks, list(edges.values()), fixed, packages, results, estimate, baseline

def rank(day):
    return bisect_right(CAL, day) - 1


def endpoints(edge, tasks):
    a, b, kind = edge['source'], edge['target'], edge['kind']
    a_end = kind in ('FC', 'FF') and not tasks[a]['milestone']
    b_end = kind in ('FF', 'CF') and not tasks[b]['milestone']
    return (a, 'finish' if a_end else 'start'), (b, 'finish' if b_end else 'start')


def topological(nodes, relations):
    degree = dict.fromkeys(nodes, 0)
    following = defaultdict(list)
    for a, b, lag in relations:
        if a not in degree or b not in degree:
            raise ValueError(f'Referencia a un nodo inexistente: {a} → {b}')
        degree[b] += 1
        following[a].append((b, lag))
    queue = deque(k for k in nodes if degree[k] == 0)
    ordered = []
    while queue:
        a = queue.popleft()
        ordered.append(a)
        for b, _ in following[a]:
            degree[b] -= 1
            if degree[b] == 0:
                queue.append(b)
    if len(ordered) != len(nodes):
        raise ValueError(f'Ciclo: {[k for k, value in degree.items() if value]}')
    return ordered, following


def schedule(tasks, edges, fixed, packages, milestones, estimates):
    """Pasadas CPM relativas a las ventanas comprometidas de la carta nivelada."""
    planned = {}
    relations = []
    for key, task in tasks.items():
        planned[key, 'start'] = rank(task['start'])
        if not task['milestone']:
            planned[key, 'finish'] = rank(task['finish'])
            relations.append(((key, 'start'), (key, 'finish'),
                              planned[key, 'finish'] - planned[key, 'start']))
    for edge in edges:
        a, b = endpoints(edge, tasks)
        relations.append((a, b, edge['lag']))
    order, following = topological(planned, relations)
    bad = [
        (a, tasks[a[0]][a[1]].isoformat(), b, tasks[b[0]][b[1]].isoformat(), lag)
        for a, b, lag in relations
        if planned[b] < planned[a] + lag or tasks[b[0]][b[1]] < tasks[a[0]][a[1]]
    ]
    if bad:
        raise ValueError(f'Precedencias incompatibles con la carta nivelada: {bad}')

    latest = dict.fromkeys(planned, rank(END))
    for key, day in fixed.items():
        latest[key, 'start'] = rank(day)
        if (key, 'finish') in latest:
            latest[key, 'finish'] = planned[key, 'finish']
    for key in packages:
        end_month = int(estimates[key][3].split('–')[-1])
        latest[key, 'finish'] = rank(period(end_month)[1])
    for h, result in milestones.items():
        first, end = period(MONTHS[h])
        limit = rank(first if h in ('H6', 'H11') else end)
        result['limite'] = CAL[limit]
        result['margen_firma'] = limit - rank(result['acta'])
        result['margen_corte'] = limit - rank(result['produccion']) if result['produccion'] else None
        result['holgura'] = result['margen_corte'] if result['produccion'] else result['margen_firma']
        latest[f'ACT:{h}', 'start'] = min(latest[f'ACT:{h}', 'start'], limit)
        if result['produccion']:
            latest[f'REG:{h}', 'start'] = min(latest[f'REG:{h}', 'start'], limit)
            result['corte_con_subsanacion_10'] = allowed_cut(after(result['acta'], 10))
            result['holgura_subsanacion_10'] = limit - rank(result['corte_con_subsanacion_10'])
    for a in reversed(order):
        for b, lag in following[a]:
            latest[a] = min(latest[a], latest[b] - lag)
    negative = [(a, value - planned[a]) for a, value in latest.items() if value < planned[a]]
    if negative:
        raise ValueError(f'Ventanas contractuales insuficientes: {negative}')
    detail = {}
    for key in packages:
        detail[key] = dict(inicio=tasks[key]['start'], fin=tasks[key]['finish'],
                           duracion=workdays(tasks[key]['start'], tasks[key]['finish']),
                           minimo=tasks[key]['work'], inicio_tardio=CAL[latest[key, 'start']],
                           fin_tardio=CAL[latest[key, 'finish']],
                           holgura=min(latest[key, side] - planned[key, side] for side in ('start', 'finish')))
    assert all(r['holgura'] >= 0 for r in milestones.values())
    return detail


def replace_rows(source, destination, pattern, records):
    lines = (ROOT / source).read_text(encoding='utf-8').splitlines()
    first = next(i for i, line in enumerate(lines) if re.match(pattern, line))
    last = max(i for i, line in enumerate(lines) if re.match(pattern, line))
    output = ['  ' + ' & '.join(map(str, row)) + ' ' + chr(92) * 2 for row in records]
    destination.write_text('\n'.join(lines[:first] + output + lines[last + 1:]) + '\n', encoding='utf-8')


def export_tables(output, packages, milestones, detail):
    def dmy(day):
        return day.strftime('%d-%m-%Y') if day else '—'

    replace_rows(TABLES / 'tab_T15_7.tex', output / 'tab_T15_7.tex', r'^\s*H\d+\s*&', (
        (h, dmy(m['entrega']), dmy(m['acta']), dmy(m['produccion']), dmy(m['limite']),
         m['margen_firma'], m['margen_corte'] if m['margen_corte'] is not None else '—', m['control'])
        for h in ORDER for m in (milestones[h],)
    ))
    replace_rows(TABLES / 'tab_T15_cpm_detalle.tex', output / 'tab_T15_cpm_detalle.tex', r'^\s*\d+\.\d+\.\d+\s*&', (
        (code, d['duracion'], dmy(d['inicio']), dmy(d['fin']), dmy(d['inicio_tardio']),
         dmy(d['fin_tardio']), d['holgura'], str(packages[code]['hh']).replace('.', ','))
        for code, d in detail.items()
    ))


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--output-dir', type=Path, required=True)
    args = parser.parse_args()
    tasks, edges, fixed, packages, milestones, estimates, baseline = build()
    detail = schedule(tasks, edges, fixed, packages, milestones, estimates)
    resource = {role: capacity(packages, role, limit) for role, limit in CAPS.items()}
    result = dict(linea_base_hh=baseline, paquetes=len(packages), cuentas=60, inventario=len(estimates),
                  hitos=[milestones[h] for h in ORDER], tareas=tasks, relaciones=edges, detalle=detail,
                  capacidad=resource, feriados=sorted(HOLIDAYS))
    args.output_dir.mkdir(parents=True, exist_ok=True)
    export_tables(args.output_dir, packages, milestones, detail)
    (args.output_dir / 'cronograma_sd7.json').write_text(
        json.dumps(result, ensure_ascii=False, indent=2, default=str) + '\n', encoding='utf-8')
    for h in ORDER:
        m = milestones[h]
        print(h, m['entrega'], m['acta'], m['produccion'] or '—', m['holgura'])
    print(f'{len(packages)} paquetes · {len(tasks)} filas en red · {len(edges)} vínculos · {baseline} HH')
    print({role: values['pico_personas_equivalentes'] for role, values in resource.items()})


if __name__ == '__main__':
    main()
