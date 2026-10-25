"""Aplica la reprogramación del 25-10-2026 a las curvas publicadas del T-15.

Cambios de ventana (tab_T15_2 y tab_T15_paquetes):
  2.4.2 mes 14 -> 13; 3.5.1-3.5.4 mes 15 -> 14-15; 4.3.4 mes 21 -> 20;
  9.1.2 mes 21 -> 21-22; 4.3.2 se recalcula desde el acta H12 calculada (25-10-2028).
Las HH totales no cambian. Las personas siguen la regla del T-15: techo de HH/128 por
familia; cuando la familia no es separable se suma techo(alza/128) o se resta piso(baja/128),
de modo que la envolvente nunca queda por debajo de la demanda.
Ejecutar una sola vez sobre las tablas previas a la reprogramación.
"""
from pathlib import Path
from fractions import Fraction as F
import re

ROOT = Path(__file__).resolve().parents[1]
T = ROOT / 'formulario-t15/tablas'
ROW = re.compile(r'^\s*\d+\s*&')
END = ' \\\\'


def rows(text):
    return [l.strip().removesuffix('\\\\').strip().split(' & ') for l in text.splitlines() if ROW.match(l)]


def write(path, new):
    it = iter(new)
    out = ['  ' + ' & '.join(next(it)) + END if ROW.match(l) else l
           for l in path.read_text(encoding='utf-8').splitlines()]
    assert next(it, None) is None
    path.write_text('\n'.join(out) + '\n', encoding='utf-8')


if '  15 & 0.00 & 4067.14 & 4045.71 &' not in (T / 'tab_T15_4.tex').read_text(encoding='utf-8'):
    raise SystemExit('La reprogramación ya está aplicada; volver a ejecutarla duplicaría los deltas.')

DIA = F(2464, 24)
OLD_432 = {21: 10 * DIA, 22: 14 * DIA}   # acompañamiento desde el 20-10-2028
NEW_432 = {21: 5 * DIA, 22: 19 * DIA}    # desde el 26-10-2028, lunes a sábado
# Columnas de tab_T15_4: 0 E1 des, 1 E1 MB, 2 E2 des, 3 E2 MB, 4 puente, 5 Operación, 6 cierre
HH = {(13, 2): F(240), (14, 2): F(-240 + 1920), (15, 2): F(-1920), (20, 3): F(80),
      (21, 6): F(-80 - 40) + NEW_432[21] - OLD_432[21],
      (22, 6): F(40) + NEW_432[22] - OLD_432[22]}
assert sum(HH.values()) == 0

cur = rows((T / 'tab_T15_4.tex').read_text(encoding='utf-8'))
cents = [[round(F(c) * 100) for c in r[1:8]] for r in cur]
for (m, c), v in HH.items():
    cents[m - 1][c] += round(v * 100)
assert sum(map(sum, cents)) == 22002300
write(T / 'tab_T15_4.tex',
      [[str(i + 1)] + [f'{v / 100:.2f}' for v in r] + [f'{sum(r) / 100:.2f}'] for i, r in enumerate(cents)])

ROLES = ['JP', 'ARQ', 'SEG', 'DAT', 'DES', 'CAL', 'SRE', 'IMP']
# 3.5.x y 4.3.2 son familias separables (techo directo); el resto, regla de alza/baja.
FIX = {(13, 'ARQ'): 5, (14, 'ARQ'): 1, (14, 'DES'): 15, (14, 'DAT'): 6, (15, 'DES'): 14,
       (15, 'DAT'): 4, (20, 'JP'): 2, (21, 'IMP'): 6, (22, 'JP'): 2, (22, 'IMP'): 17}
pers = rows((T / 'tab_T15_4_personas.tex').read_text(encoding='utf-8'))
for r in pers:
    m = int(r[0])
    for j, role in enumerate(ROLES):
        if (m, role) in FIX:
            r[j + 1] = str(FIX[m, role])
    r[9] = str(sum(int(x) for x in r[1:9]))
write(T / 'tab_T15_4_personas.tex', pers)

tot = [sum(r[c] for r in cents) for c in range(7)]
order = {'E1 Desarrollo': 0, 'E1 Marcha blanca': 1, 'E2 Desarrollo': 2, 'E2 Marcha blanca': 3,
         'E1 Producción y estabilización': 4, 'Operación': 5, 'E2 Cierre y estabilización posterior al H12': 6}
p = T / 'tab_T15_3.tex'
ls = p.read_text(encoding='utf-8').splitlines()
for n, l in enumerate(ls):
    c = l.strip().removesuffix('\\\\').strip().split(' & ')
    if c[0] in order:
        t = tot[order[c[0]]] / 100
        c[1] = f'{t - float(c[2]):.2f}'
        c[3] = f'{t:.2f}'
        ls[n] = '  ' + ' & '.join(c) + END
p.write_text('\n'.join(ls) + '\n', encoding='utf-8')

peak = max(int(r[9]) for r in pers)
print('totales por etapa', [t / 100 for t in tot])
print('peak', peak, 'meses', [r[0] for r in pers if int(r[9]) == peak])
print({int(r[0]): int(r[9]) for r in pers if 12 <= int(r[0]) <= 23})
