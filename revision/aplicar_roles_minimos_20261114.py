"""Roles mínimos de BTT 19.2 en el T-15 (14-11-2026).

Lee revision/roles_minimos_20261114.json y:
1. Traspasa HH dentro de las partidas (el total de cada partida no cambia):
   JP <- Analista PMO; Líder de Desarrollo <- Arquitecto Junior e Ing. de Integración Junior
   (diseño, meses 1-4); Líder Funcional <- Analistas Funcionales, QA de aceptación (3.8.2, 3.9.2),
   Jefes de Frente y la mitad del Coordinador en olas y marcha blanca; Líder de Operación <- la
   mitad de DevOps en las partidas SRE de Operación; permanencia con el subordinado del rol.
2. Agrega las HH que no reemplazan trabajo de otro perfil como líneas explícitas, igual que
   el soporte puente y la reserva protegida (las 227 partidas y sus O/M/P no cambian).
3. Actualiza la tabla de perfiles, su conciliación por fase y la curva mensual por etapa.
Jornada completa = 128 HH programables por mes (sección 4.1).
"""
import json
import re
from collections import defaultdict
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
T = ROOT / 'formulario-t15/tablas'
BS = chr(92)
D = json.loads((ROOT / 'revision/roles_minimos_20261114.json').read_text(encoding='utf-8'))


def num(s):
    return float(s.strip().replace('.', '').replace(',', '.'))


def es(x, dec=2):
    t = f'{x:,.{dec}f}'.replace(',', 'X').replace('.', ',').replace('X', '.')
    return t.rstrip('0').rstrip(',') if ',' in t else t


def es2(x):
    return f'{x:,.2f}'.replace(',', 'X').replace('.', ',').replace('X', '.')


# --- 1. Tabla de asignación por partida ---------------------------------------
p = T / 'tab_T15_asignacion_partidas.tex'
lines = p.read_text(encoding='utf-8').split('\n')
rx = re.compile(r'(\s*([\d.]+|—) & (.*?) & ([A-Z]+) & (\d+)–(\d+) & ([\d.,]+) & )(.*?) ' + BS * 4 + r'$')
perf_order = []
for l in (T / 'tab_T15_perfiles_internos.tex').read_text(encoding='utf-8').split('\n'):
    m = re.match(r'^(\d\d[A-Z]?) & ', l)
    if m:
        perf_order.append(m.group(1))
perf_order.append('00')
pos = {c: k for k, c in enumerate(perf_order)}

mv = defaultdict(lambda: defaultdict(int))   # (code, desc) -> perfil -> centésimas
for code, desc, src, dst, v in D['moves']:
    c = round(v * 100)
    mv[(code, desc)][src] -= c
    mv[(code, desc)][dst] += c
seen = set()
for k, l in enumerate(lines):
    m = rx.match(l)
    if not m:
        continue
    key = (m.group(2), m.group(3))
    if key not in mv or key in seen:
        continue
    seen.add(key)
    cents = defaultdict(int)
    for q, v in re.findall(r'(\w+) \(([\d.,]+)\)', m.group(8)):
        cents[q] += round(num(v) * 100)
    tot = sum(cents.values())
    for q, c in mv[key].items():
        cents[q] += c
    assert sum(cents.values()) == tot and min(cents.values()) >= 0, key
    parts = sorted(((q, c) for q, c in cents.items() if c), key=lambda qc: (-qc[1], pos[qc[0]]))
    lines[k] = m.group(1) + ', '.join(f'{q} ({es(c / 100)})' for q, c in parts) + ' ' + BS * 2
assert seen == set(mv), set(mv) - seen

newm = defaultdict(dict)
for L, m_, v in D['newm']:
    newm[L][m_] = newm[L].get(m_, 0) + v
SPECIAL = [  # (perfil, familia, descripción)
    ('04', 'DES', 'Dedicación completa del Líder de Desarrollo'),
    ('05', 'ARQ', 'Dedicación completa del Líder Funcional'),
    ('24', 'SRE', 'Gerencia del servicio y permanencia del Líder de Operación / SRE'),
    ('23', 'DAT', 'Permanencia del Líder de Datos'),
    ('16', 'CAL', 'Permanencia del Líder de Calidad y Pruebas'),
]
assert set(newm) == {s[0] for s in SPECIAL}, set(newm)
NEWROWS, newtot = [], {}
for q, fam, desc in SPECIAL:
    ms = sorted(newm[q])
    hh = round(sum(newm[q].values()), 2)
    newtot[q] = hh
    NEWROWS.append(f'  — & {desc} & {fam} & {ms[0]}–{ms[-1]} & {es(hh)} & {q} ({es(hh)}) ' + BS * 2)
end = next(k for k, l in enumerate(lines) if l.startswith(BS + 'end{tablalafrox}'))
if not any('Dedicación completa del Líder de Desarrollo' in l for l in lines):
    lines[end:end] = NEWROWS
NEW = round(sum(newtot.values()), 2)
OLD_P, OLD_T = 197894.23, 199219.03
txt = '\n'.join(lines)
txt = txt.replace(f'{es2(OLD_P)} HH de los perfiles y 1.324,80 HH de servicios especializados, para un total de {es2(OLD_T)} HH',
                  f'{es2(OLD_P + NEW)} HH de los perfiles y 1.324,80 HH de servicios especializados, para un total de {es2(OLD_T + NEW)} HH')
p.write_text(txt, encoding='utf-8')

# --- 2. Tabla de perfiles -------------------------------------------------------
dimp, dop = defaultdict(float), defaultdict(float)
rows = {}
for l in lines:
    m = rx.match(l)
    if m:
        rows[(m.group(2), m.group(3))] = (int(m.group(5)), int(m.group(6)))


def fase_impl(code, a, b):
    if code.startswith('9.1'):
        return 1.0
    if code.startswith(('8.', '9.')):
        return 0.0
    return max(0, min(b, 20) - a + 1) / (b - a + 1)


for code, desc, src, dst, v in D['moves']:
    a, b = rows[(code, desc)]
    fi = 1.0 if code == '—' else fase_impl(code, a, b)
    for q, s in ((src, -1), (dst, 1)):
        dimp[q] += s * v * fi
        dop[q] += s * v * (1 - fi)
for q, mm in newm.items():
    for m_, v in mm.items():
        (dimp if m_ <= 20 else dop)[q] += v

pp = T / 'tab_T15_perfiles_internos.tex'
pl = pp.read_text(encoding='utf-8').split('\n')
ti = to = 0.0
for k, l in enumerate(pl):
    m = re.match(r'^(\d\d[A-Z]?) & ', l)
    if not m:
        continue
    c = l.split(' & ')
    q = m.group(1)
    hi, ho = num(c[5]), num(c[7].replace(BS * 2, ''))
    if abs(dimp[q]) > 1e-9 or abs(dop[q]) > 1e-9:
        hi, ho = round(hi + dimp[q], 2), round(ho + dop[q], 2)
        c[5], c[6] = es(hi), es(hi / 8, 4)
        c[7] = es(ho)
        c[8] = es(ho / 8, 4) + ' ' + BS * 2
        pl[k] = ' & '.join(c)
    ti += hi
    to += ho
ti, to = round(ti, 2), round(to, 2)
for k, l in enumerate(pl):
    if 'Total de perfiles' in l:
        c = [x.strip() for x in l.split('&')]
        c[5] = BS + 'textbf{' + es2(ti) + '}'
        c[6] = BS + 'textbf{' + es2(ti / 8) + '}'
        c[7] = BS + 'textbf{' + es2(to) + '}'
        c[8] = BS + 'textbf{' + es(to / 8, 3) + '} ' + BS * 2
        pl[k] = ' ' + ' & '.join(c)
ptxt = '\n'.join(pl)
OI, OO = 90048.83, 107845.40
ni, no = ti + 864, to + 460.80
new_impl_month = sum(v for mm in newm.values() for m_, v in mm.items() if m_ <= 20)
new_op_month = sum(v for mm in newm.values() for m_, v in mm.items() if m_ > 20)
rep = {
    f'Los perfiles aportan {es2(OI)} HH de implementación y {es2(OO)} HH de operación':
        f'Los perfiles aportan {es2(ti)} HH de implementación y {es2(to)} HH de operación',
    f'HH_{{implem.}}&={es2(OI)}+864=90.912,83': f'HH_{{implem.}}&={es2(ti)}+864={es2(ni)}',
    f'HH_{{oper.}}&={es2(OO)}+460,80=108.306,20': f'HH_{{oper.}}&={es2(to)}+460,80={es2(no)}',
    'HH_{proyecto}&=90.912,83+108.306,20=199.219,03': f'HH_{{proyecto}}&={es2(ni)}+{es2(no)}={es2(ni + no)}',
    '(90.809,86 y 108.409,17 HH en el resumen por etapa), con el mismo total de 199.219,03 HH':
        f'({es2(90809.86 + new_impl_month)} y {es2(108409.17 + new_op_month)} HH en el resumen por etapa), con el mismo total de {es2(ni + no)} HH',
    'En jornadas equivalentes son 11.364,10 de implementación y 13.538,275 de operación: 24.902,38 en total':
        f'En jornadas equivalentes son {es2(ni / 8)} de implementación y {es(no / 8, 3)} de operación: {es2((ni + no) / 8)} en total',
}
for a_, b_ in rep.items():
    assert a_ in ptxt, a_
    ptxt = ptxt.replace(a_, b_)
pp.write_text(ptxt, encoding='utf-8')
assert abs(ni + no - (OLD_T + NEW)) < 0.02, (ni + no, OLD_T + NEW)

# --- 3. Curva mensual por etapa (tab_T15_4) -------------------------------------
STAGE = {}  # mes -> índice de columna (0 = E1 desarrollo ... 6 = E2 cierre)
for m_ in range(1, 13):
    STAGE[m_] = 0
for m_ in range(13, 16):
    STAGE[m_] = 1      # E1 marcha blanca
for m_ in range(16, 19):
    STAGE[m_] = 4      # E1 producción y estabilización
for m_ in range(19, 21):
    STAGE[m_] = 3      # E2 marcha blanca
for m_ in range(21, 57):
    STAGE[m_] = 5      # Operación
add = defaultdict(float)
for mm in newm.values():
    for m_, v in mm.items():
        add[m_] += v
p4 = T / 'tab_T15_4.tex'
out = []
for l in p4.read_text(encoding='utf-8').split('\n'):
    m = re.match(r'^\s*(\d+) & (.*) ' + BS * 4 + '$', l)
    if m and add.get(int(m.group(1))):
        mm_ = int(m.group(1))
        v = [float(x) for x in m.group(2).split(' & ')]
        v[STAGE[mm_]] += add[mm_]
        v[-1] = sum(v[:-1])
        l = f'  {mm_} & ' + ' & '.join(f'{x:.2f}' for x in v) + ' ' + BS * 2
    out.append(l)
p4.write_text('\n'.join(out), encoding='utf-8')
print('HH nuevas', es2(NEW), '| perfiles', es2(ti), es2(to), '| proyecto', es2(ni + no))
print('impl por mes', es2(new_impl_month), 'op por mes', es2(new_op_month))
