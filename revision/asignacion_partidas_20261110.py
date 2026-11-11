"""Asignación de HH por partida y perfil del T-15 (10-11-2026).

Recupera la asignación por partida publicada antes de d08ff28d (31 perfiles) y la
lleva a los 37 perfiles de tab_T15_perfiles_internos:

1. Reparte cada perfil antiguo entre los nuevos con las proporciones de ese cambio
   (JP a medias con el Analista PMO, Senior/Junior, Líder de Implantación con los
   coordinadores, N2 a back-end en 8.2.1 y a DevOps en 8.2.3, SOC aparte, etc.).
2. Aplica la estimación del 09-11 (aplicar_estimacion_20261109.py): HH nuevas de
   los paquetes de tab_T15_2, jefes de frente y asistentes por plazas (5/23 y 18/23)
   y el Técnico de Redes (29) con las HH internas de las partidas RED más 7/9 de las
   HH DevOps de las instalaciones 6.5.3 a 6.5.6, hasta sus 2.240 HH.
3. Ajusta por IPF las celdas de los grupos cuyos paquetes cambiaron y redondea a
   centésimas con redondeo controlado: cada fila suma la E de tab_T15_2 y cada
   perfil suma las HH de tab_T15_perfiles_internos.

Escribe formulario-t15/tablas/tab_T15_asignacion_partidas.tex y verifica las sumas.
"""
import re
import subprocess
from collections import defaultdict, deque
from fractions import Fraction as Fr
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
T15 = ROOT / 'formulario-t15/tablas'
BS = chr(92)


def num(s):
    return Fr(s.strip().replace('.', '').replace(',', '.'))


def es(x):
    """Número con coma decimal y punto de miles, sin ceros finales."""
    t = f'{float(x):,.2f}'.replace(',', 'X').replace('.', ',').replace('X', '.')
    return t.rstrip('0').rstrip(',') if ',' in t else t


# --- 1. Asignación antigua -------------------------------------------------
old = subprocess.run(['git', 'show', 'd08ff28d^:formulario-t15/tablas/tab_T15_asignacion_perfiles.tex'],
                     cwd=ROOT, capture_output=True, check=True).stdout.decode('utf-8')
rows, index = [], {}
for l in old.split('\n'):
    m = re.match(r'\s*([\d.]+|—) & (.*?) & (\w+) & (\d+)–(\d+) & ([\d.,]+) & (.*?) & (.*?) ' + BS * 2, l)
    if not m:
        continue
    code, desc, fam, a, b, hh, parts, st = m.groups()
    special = code == '—' or desc.startswith(('Puente', 'Restauraciones previas'))
    key = (code, desc)
    if key not in index:
        index[key] = len(rows)
        rows.append(dict(code=code, desc=desc, fam=fam, a=int(a), b=int(b), hh=Fr(0),
                         special=special, cov=st.startswith('Cobertura'), old=defaultdict(Fr)))
    r = rows[index[key]]
    r['hh'] += num(hh)
    for p, v in re.findall(r'(\d\d) \(([\d.,]+)\)', parts):
        r['old'][p] += num(v)
assert sum(r['hh'] for r in rows) == 220023

R23 = (Fr(2, 3), Fr(1, 3))
MAP = {'01': [('01', Fr(1, 2)), ('20', Fr(1, 2))], '20': [('20', 1)], '25': [('20', 1)],
       '02': [('02', 1)], '03': [('03S', R23[0]), ('03J', R23[1])], '04': [('04', 1)],
       '05': [('05', 1)], '06': [('06S', R23[0]), ('06J', R23[1])],
       '11': [('06S', R23[0]), ('06J', R23[1])], '07': [('07S', R23[0]), ('07J', R23[1])],
       '08': [('08S', Fr(1, 2)), ('08J', Fr(1, 2))], '09': [('09S', Fr(3, 5)), ('09J', Fr(2, 5))],
       '10': [('10S', R23[0]), ('10J', R23[1])], '15': [('10S', R23[0]), ('10J', R23[1])],
       '12': [('12S', R23[0]), ('12J', R23[1])], '13': [('13', 1)],
       '14': [('14S', R23[0]), ('14J', R23[1])], '29': [('14S', R23[0]), ('14J', R23[1])],
       '16': [('16', Fr(1, 2)), ('19S', Fr(1, 2))], '19': [('19S', Fr(8, 11)), ('19J', Fr(3, 11))],
       '17': [('17', 1)], '30': [('30', 1)], '21': [('21', Fr(1, 3)), ('32', Fr(2, 3))],
       '22': [('22', 1)], '23': [('23', 1)], '24': [('24', 1)],
       '26': [('26', Fr(5, 23)), ('28', Fr(18, 23))], '27': [('26', Fr(5, 23)), ('28', Fr(18, 23))],
       '28': [('26', Fr(5, 23)), ('28', Fr(18, 23))], '00': [('00', 1)]}
for r in rows:
    cell = defaultdict(Fr)
    for p, v in r['old'].items():
        if p == '18':
            tgt = MAP['09'] if r['code'] == '8.2.1' else MAP['14']
        elif p == '31':
            tgt = [('31O', 1)] if r['code'] == '8.1.5' else [('31E', 1)]
        else:
            tgt = MAP[p]
        for q, f in tgt:
            cell[q] += v * Fr(f)
    r['cell'] = cell


def phase(r):
    """Fracción de implementación de la fila (regla de la tabla de perfiles)."""
    c, a, b = r['code'], r['a'], r['b']
    fi = Fr(max(0, min(b, 20) - a + 1), b - a + 1)
    if c == '8.1.5':  # SOC por calendario: 243 días en los meses 13 a 20
        return Fr(243, 1338)
    if c.startswith('9.1'):
        return Fr(1)
    if c.startswith(('8.', '9.')):
        return Fr(0)
    if r['cls'] == 'R':
        return fi
    return Fr(1)


cls, enew, role = {}, {}, {}
for l in (T15 / 'tab_T15_2.tex').read_text(encoding='utf-8').split('\n'):
    if re.match(r'\s*\d+(\.\d+)+\s*&', l):
        c = [x.strip() for x in l.strip().replace(BS * 2, '').split('&')]
        cls[c[0]], role[c[0]], enew[c[0]] = c[1], c[2], Fr(c[7]).limit_denominator(100)
for r in rows:
    r['cls'] = cls.get(r['code'], 'R' if r['code'] == '—' else '?')
    if r['special']:
        r['cls'] = 'T'
assert len({r['code'] for r in rows if not r['special']}) == 227

# --- perfiles actuales -------------------------------------------------------
prof, order = {}, []
for l in (T15 / 'tab_T15_perfiles_internos.tex').read_text(encoding='utf-8').split('\n'):
    if re.match(r'^\d\d[A-Z]? & ', l):
        c = l.split(' & ')
        prof[c[0]] = dict(name=c[2], impl=num(c[5]), oper=num(c[7].replace(BS * 2, '')))
        order.append(c[0])
prof['00'] = dict(name='Servicios especializados por resultado', impl=Fr(864), oper=Fr(2304, 5))
order.append('00')
assert len(order) == 38

# --- 2. Cambios del 09-11 ------------------------------------------------------
RED = [c for c in role if role[c] == 'RED']
for r in rows:
    if r['code'] in RED and not r['special']:
        mv = r['cell'].pop('14S', 0) + r['cell'].pop('14J', 0)
        r['cell']['29'] += mv
    if r['code'] in ('6.5.3', '6.5.4', '6.5.5', '6.5.6'):
        for q in ('14S', '14J'):
            mv = r['cell'][q] * Fr(7, 9)
            r['cell'][q] -= mv
            r['cell']['29'] += mv
for r in rows:
    if not r['special']:
        r['E'] = enew[r['code']]
    else:
        r['E'] = r['hh']

# Perfiles a los que aplicar_estimacion_20261109.py repartió las diferencias. Los de
# arquitectura, integración, desarrollo y datos se ajustan juntos, porque comparten
# los módulos e integraciones; así cada partida reparte su cambio entre quienes la ejecutan.
GROUPS = {'SRE': ['14S', '14J'], 'IMP': ['21', '32'],
          'TEC': ['02', '12S', '12J', '07S', '07J', '08S', '08J', '09S', '09J', '23', '10S', '10J']}
GROUP_OF = {'SRE': 'SRE', 'IMP': 'IMP', 'ARQ': 'TEC', 'DES': 'TEC', 'DAT': 'TEC'}
target = {p: prof[p]['impl'] + prof[p]['oper'] for p in order}
X = [{p: float(v) for p, v in r['cell'].items() if v} for r in rows]
desig, base = {}, {}
for i, r in enumerate(rows):
    if not r['special'] and r['E'] != r['hh']:
        desig[i] = GROUP_OF[role[r['code']]]
        assert phase(r) == 1, r['code']
for gname, g in GROUPS.items():
    gs = set(g)
    for i in desig:  # si el grupo no participaba en la partida, se siembra por sus HH
        if desig[i] == gname and not any(p in X[i] for p in g):
            w = {p: float(prof[p]['impl']) for p in g}
            for p in g:
                X[i][p] = float(rows[i]['E'] - rows[i]['hh']) * w[p] / sum(w.values())
            base[(i, gname)] = 0.0
    idx = [i for i, r in enumerate(rows) if gs & set(X[i]) and phase(r) == 1]
    fixed = defaultdict(float)
    for i, r in enumerate(rows):
        if i not in idx:
            for p in g:
                fixed[p] += X[i].get(p, 0)
    rt = {i: base.get((i, gname), sum(X[i].get(p, 0) for p in g)) + (float(rows[i]['E'] - rows[i]['hh'])
                                                         if desig.get(i) == gname else 0) for i in idx}
    ct = {p: float(target[p]) - fixed[p] for p in g}
    for _ in range(20000):
        for i in idx:
            s = sum(X[i].get(p, 0) for p in g)
            for p in g:
                if p in X[i]:
                    X[i][p] *= rt[i] / s
        err = 0
        for p in g:
            s = sum(X[i].get(p, 0) for i in idx)
            err = max(err, abs(s - ct[p]))
            for i in idx:
                if p in X[i]:
                    X[i][p] *= ct[p] / s
        if err < 1e-9:
            break
    assert err < 1e-6, (g, err)

# --- 3. Redondeo controlado a centésimas --------------------------------------
cents = [{p: int(v * 100 + 1e-9) for p, v in x.items()} for x in X]
rneed = [round(float(rows[i]['E']) * 100) - sum(cents[i].values()) for i in range(len(rows))]
cneed = {p: round(float(target[p]) * 100) - sum(c.get(p, 0) for c in cents) for p in order}
assert sum(rneed) == sum(cneed.values()) and min(rneed) >= 0 and min(cneed.values()) >= 0
frac = {(i, p): X[i][p] * 100 - cents[i][p] for i in range(len(rows)) for p in X[i]}
# Flujo máximo: fuente -> fila (rneed) -> celda con fracción (1) -> perfil (cneed) -> sumidero
cap = defaultdict(int)
adj = defaultdict(dict)  # dict ordenado: resultado reproducible entre ejecuciones


def edge(u, v, c):
    cap[(u, v)] += c
    adj[u][v] = None
    adj[v][u] = None


for i, n in enumerate(rneed):
    if n:
        edge('S', ('r', i), n)
for (i, p), f in sorted(frac.items(), key=lambda kv: -kv[1]):
    if f > 1e-6:
        edge(('r', i), ('c', p), 1)
for p, n in cneed.items():
    if n:
        edge(('c', p), 'T', n)
flow = 0
while True:
    prev = {'S': None}
    q = deque(['S'])
    while q and 'T' not in prev:
        u = q.popleft()
        for v in adj[u]:
            if v not in prev and cap[(u, v)] > 0:
                prev[v] = u
                q.append(v)
    if 'T' not in prev:
        break
    v = 'T'
    while prev[v] is not None:
        u = prev[v]
        cap[(u, v)] -= 1
        cap[(v, u)] += 1
        v = u
    flow += 1
assert flow == sum(rneed), (flow, sum(rneed))
for (i, p), f in frac.items():
    if f > 1e-6 and cap[(('c', p), ('r', i))] > 0:
        cents[i][p] += 1

# --- verificación --------------------------------------------------------------
tot = defaultdict(int)
io = defaultdict(lambda: [Fr(0), Fr(0)])
for i, r in enumerate(rows):
    assert sum(cents[i].values()) == round(float(r['E']) * 100), r['code']
    assert min(cents[i].values()) >= 0
    fi = phase(r)
    for p, c in cents[i].items():
        tot[p] += c
        io[p][0] += Fr(c, 100) * fi
        io[p][1] += Fr(c, 100) * (1 - fi)
for p in order:
    assert tot[p] == round(float(target[p]) * 100), (p, tot[p], target[p])
    di = float(io[p][0] - prof[p]['impl'])
    assert abs(di) < 0.05, (p, float(io[p][0]), float(prof[p]['impl']))
total = sum(tot.values())
assert total == 21972783, total
TR = ['7.1.1', '7.1.2', '7.1.3', '7.1.4', '7.1.5', '7.1.6', '7.3.1', '7.3.2', '8.5.1']
trn = defaultdict(int)
for i, r in enumerate(rows):
    if r['code'] in TR:
        for p, c in cents[i].items():
            trn[p] += c
print('total HH', es(Fr(total, 100)), '| filas', len(rows))
print('capacitación por perfil', {p: es(Fr(c, 100)) for p, c in trn.items()}, 'total', es(Fr(sum(trn.values()), 100)))
print('implementación por perfil (máx. diferencia):',
      round(max(abs(float(io[p][0] - prof[p]['impl'])) for p in order), 4))

# --- nombres actuales del T-14 -------------------------------------------------
names = {}
for f in sorted((ROOT / 'formulario-t14/tablas').glob('*.tex')):
    for l in f.read_text(encoding='utf-8').split('\n'):
        m = re.match(r'\s*(\d+(?:\.\d+)+) & (.*?) & ', l)
        if m and m.group(1) not in names:
            names[m.group(1)] = m.group(2).strip()

pos = {p: k for k, p in enumerate(order)}
out = []
for i, r in enumerate(rows):
    parts = sorted(((p, c) for p, c in cents[i].items() if c), key=lambda pc: (-pc[1], pos[pc[0]]))
    desc = r['desc'] if r['special'] else names.get(r['code'], r['desc'])
    fam = r['fam'] if r['special'] else role[r['code']]
    out.append(f"  {r['code']} & {desc} & {fam} & {r['a']}–{r['b']} & {es(r['E'])} & "
               + ', '.join(f'{p} ({es(Fr(c, 100))})' for p, c in parts) + ' ' + BS * 2)
head = r'''\paragraph{Asignación por partida}
La Tabla~\ref{tab:T15-asignacion-partidas} asigna las HH de cada partida a los perfiles de la Tabla~\ref{tab:T15-perfiles-internos}. La columna «Perfil y HH» indica el código del perfil y, entre paréntesis, sus HH en la partida; el código 00 identifica los servicios especializados por resultado. Cada fila suma las HH de la partida y cada perfil suma las HH de implementación y de operación de la Tabla~\ref{tab:T15-perfiles-internos}: 218.403,03 HH de los perfiles y 1.324,80 HH de servicios especializados, para un total de 219.727,83 HH. Las fases 8 y 9.2 se cuentan en operación; las partidas recurrentes de las fases 1 a 7 que siguen después del mes 20 se dividen en proporción a sus meses, y el SOC según su calendario.

Por ejemplo, las 5.168 HH de capacitación y certificación (7.1, 7.3 y 8.5.1) se reparten entre el Instructor de Capacitación (@22@ HH), los coordinadores de implantación (@32@ HH), el Analista PMO, documentación y compras (@20@ HH) y el Líder de Implantación (@21@ HH).

\begin{anexohorizontal}
\setlength{\textwidth}{\linewidth}
\renewcommand{\arraystretch}{1.18}
\begin{tablalafrox}{Asignación de HH por partida y perfil. Fuente: elaboración a partir de la EDT del Formulario T-14, las HH de la Tabla~\ref{tab_T15_2} y los perfiles de la Tabla~\ref{tab:T15-perfiles-internos}.}{tab:T15-asignacion-partidas}
{L{1.45cm} Y C{1.3cm} C{1.3cm} R{1.5cm} L{5.2cm}}
{\cab{EDT} & \cab{Partida} & \cab{Familia} & \cab{Meses} & \cab{HH} & \cab{Perfil y HH}}
'''
tail = r'''\end{tablalafrox}
\end{anexohorizontal}
'''
assert set(trn) == {'22', '32', '20', '21'} and sum(trn.values()) == 516800
for p, c in trn.items():
    head = head.replace(f'@{p}@', es(Fr(c, 100)))
(T15 / 'tab_T15_asignacion_partidas.tex').write_text(head + '\n'.join(out) + '\n' + tail, encoding='utf-8')
print('escrito', T15 / 'tab_T15_asignacion_partidas.tex')
