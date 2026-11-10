"""Aplica la estimación de módulos y la regla PERT por tipo al T-15 (09-11-2026).

1. tab_T15_2: O/M/P/E de los 15 módulos (estimacion_modulos_20261109.py),
   rangos por clase (E = M) y rangos propios de los paquetes con riesgo identificado.
2. tab_T15_paquetes: HH y personas promedio de los paquetes cuyo E cambió.
3. tab_T15_4 (curva de HH por etapa) y tab_T15_3 (HH por etapa): deltas por mes.
4. Perfiles (sección 6.3): deltas por rol repartidos entre los perfiles que ejecutan.
Escribe revision/estimacion_20261109.json con la conciliación.
"""
import json, re, math
from fractions import Fraction as F
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
T = ROOT / 'formulario-t15/tablas'
BS2 = chr(92) * 2
g = {'__file__': str(ROOT / 'revision/estimacion_modulos_20261109.py'), '__name__': 'lib'}
exec((ROOT / 'revision/estimacion_modulos_20261109.py').read_text(encoding='utf-8'), g)
MODS = {r['code']: r for r in g['estimate']()}

CLASS = {'G': (0.90, 1.10), 'E': (0.80, 1.20), 'I': (0.80, 1.20), 'V': (0.85, 1.15),
         'T': (0.85, 1.15), 'R': (0.90, 1.10)}
RISK = {'3.3.2': (0.85, 1.60), '3.6.5': (0.85, 1.60), '3.6.6': (0.85, 1.50),
        '3.7.1': (0.90, 1.50), '3.7.2': (0.90, 1.40), '3.7.3': (0.90, 1.40), '3.7.4': (0.90, 1.40),
        '2.4.3': (0.90, 1.50), '4.1.4': (0.90, 1.50)}

def fmt(x): return f'{x:.2f}'

p2 = T / 'tab_T15_2.tex'
lines = p2.read_text(encoding='utf-8').split('\n')
delta = {}   # código -> (E anterior, E nuevo, rol, meses)
for i, l in enumerate(lines):
    if not re.match(r'\s*\d+(\.\d+)+\s*&', l): continue
    c = [x.strip() for x in l.strip().removesuffix(BS2).strip().split(' & ')]
    code, cl, role, months = c[0], c[1], c[2], c[3]
    o, m, p, e = map(float, c[4:8])
    if code in MODS:
        r = MODS[code]; O, M, P, E = r['O'], r['M'], r['P'], r['E']
    elif code in RISK:
        fo, fp = RISK[code]; O, M, P = m * fo, m, m * fp; E = round((O + 4 * M + P) / 6, 2)
    elif cl in CLASS:
        fo, fp = CLASS[cl]; O, M, P = m * fo, m, m * fp; E = e
        assert abs(E - M) < 0.01, code
    else:
        continue
    if abs(E - e) > 0.001: delta[code] = (e, E, role, months)
    c[4:8] = [fmt(O), fmt(M), fmt(P), fmt(E)]
    lines[i] = '  ' + ' & '.join(c) + ' ' + BS2
p2.write_text('\n'.join(lines), encoding='utf-8')

# tab_T15_paquetes
pp = T / 'tab_T15_paquetes.tex'
lines = pp.read_text(encoding='utf-8').split('\n'); n = 0
for i, l in enumerate(lines):
    c = l.split(' & ')
    if len(c) > 6 and c[0].strip() in delta:
        old, new, _, _ = delta[c[0].strip()]
        avg, mx = [x.strip() for x in c[2].split('/')]
        avgf = float(avg.replace(',', '.')); mxf = float(mx)
        navg = min(round(avgf * new / old, 1), mxf)
        c[2] = f"{str(navg).replace('.', ',')} / {mx}"
        c[3] = (f'{new:.2f}'.rstrip('0').rstrip('.')).replace('.', ',')
        lines[i] = ' & '.join(c); n += 1
assert n == len(delta), (n, len(delta))
pp.write_text('\n'.join(lines), encoding='utf-8')

# Curva de HH por etapa: columnas 1 E1 des, 2 E1 MB, 3 E2 des, 4 E2 MB, 5 E1 prod, 6 Op, 7 E2 cierre
p4 = T / 'tab_T15_4.tex'
lines = p4.read_text(encoding='utf-8').split('\n')
rows = {}
for i, l in enumerate(lines):
    if re.match(r'^\s*\d+\s*&', l):
        c = [x.strip() for x in l.strip().removesuffix(BS2).strip().split(' & ')]
        rows[int(c[0])] = (i, [round(F(x) * 100) for x in c[1:8]])
stage_delta = {}
def col_for(code, m):
    if m <= 12: return 0
    if code.startswith('3.5.') or code in ('3.6.5', '3.6.6'):
        return 2 if m <= 18 else 3
    raise ValueError((code, m))
for code, (old, new, role, months) in delta.items():
    a, b = map(int, months.split('–')); k = b - a + 1
    cents = round((new - old) * 100)
    share = [cents // k] * k; share[-1] += cents - sum(share)
    for m, s in zip(range(a, b + 1), share):
        col = col_for(code, m); rows[m][1][col] += s
        stage_delta[col] = stage_delta.get(col, 0) + s
for m, (i, v) in rows.items():
    lines[i] = '  ' + ' & '.join([str(m)] + [f'{x/100:.2f}' for x in v] + [f'{sum(v)/100:.2f}']) + ' ' + BS2
p4.write_text('\n'.join(lines), encoding='utf-8')
total_cents = sum(sum(v) for _, v in rows.values())

# HH por etapa (tab_T15_3): filas en el orden de las columnas de la curva
p3 = T / 'tab_T15_3.tex'
names = ['E1 Desarrollo', 'E1 Marcha blanca', 'E2 Desarrollo', 'E2 Marcha blanca']
lines = p3.read_text(encoding='utf-8').split('\n')
for i, l in enumerate(lines):
    for col, nm in enumerate(names):
        if l.strip().startswith(nm + ' &') and col in stage_delta:
            c = l.split(' & ')
            base = F(c[1].strip()) + F(stage_delta[col], 100)
            prog = F(c[3].strip()) + F(stage_delta[col], 100)
            c[1] = f'{float(base):.2f}'; c[3] = f'{float(prog):.2f}'
            lines[i] = ' & '.join(c)
p3.write_text('\n'.join(lines), encoding='utf-8')

# Perfiles: deltas por rol
PROF = {'DES': ['07S', '07J', '08S', '08J', '09S', '09J'],
        'DAT': ['23', '10S', '10J'],
        'ARQ': ['02', '12S', '12J'],
        'SRE': ['14S', '14J'],
        'IMP': ['21', '32']}
INTEG = {'3.6.5', '3.6.6'}   # integración con cadenas: ingenieros de integración
role_delta = {}
for code, (old, new, role, _) in delta.items():
    key = 'ARQ' if code in INTEG else role
    role_delta[key] = role_delta.get(key, 0) + (new - old)
pf = T / 'tab_T15_perfiles_internos.tex'
s = pf.read_text(encoding='utf-8'); L = s.split('\n')
def num(x): return float(x.strip().replace('.', '').replace(',', '.'))
def es(x, d=2):
    t = f'{x:,.{d}f}'.replace(',', 'X').replace('.', ',').replace('X', '.')
    return t.rstrip('0').rstrip(',') if ',' in t else t
idx = {l.split(' & ')[0].strip(): i for i, l in enumerate(L) if re.match(r'^\d\d[A-Z]? & ', l)}
for role, d in role_delta.items():
    codes = PROF[role]; hh = {c: num(L[idx[c]].split(' & ')[5]) for c in codes}; tot = sum(hh.values())
    for c in codes:
        parts = L[idx[c]].split(' & ')
        nh = hh[c] + d * hh[c] / tot
        parts[5] = es(round(nh, 2)); parts[6] = es(round(nh / 8, 4), 4)
        L[idx[c]] = ' & '.join(parts)
impl = sum(num(L[i].split(' & ')[5]) for i in idx.values())
jor = sum(num(L[i].split(' & ')[6]) for i in idx.values())
pf.write_text('\n'.join(L), encoding='utf-8')

out = {'delta': {k: [v[0], v[1], round(v[1] - v[0], 2), v[2]] for k, v in delta.items()},
       'delta_total': round(sum(v[1] - v[0] for v in delta.values()), 2),
       'total_curva': total_cents / 100, 'stage_delta': {k: v / 100 for k, v in stage_delta.items()},
       'role_delta': {k: round(v, 2) for k, v in role_delta.items()},
       'perfiles_impl': round(impl, 2), 'perfiles_jornadas': round(jor, 4)}
(ROOT / 'revision/estimacion_20261109.json').write_text(json.dumps(out, ensure_ascii=False, indent=1), encoding='utf-8')
print(json.dumps(out, ensure_ascii=False, indent=1))
