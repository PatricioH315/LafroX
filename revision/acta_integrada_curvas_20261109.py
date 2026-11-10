"""Acta integrada H7/H12 (09-11-2026): reparto de 4.3.2 desde el paso a producción del 18-10-2028.

Refuerzo de 24 jornadas de lunes a sábado: 11 en el mes 21 y 13 en el mes 22,
2.464/24 HH por jornada. Antes: 5 y 19 jornadas desde el 26-10-2028.
Plazas por perfil (techo HH/128): bodega 26 (16 HH/día), plataformas 27 (24), ruta 28 (56).
Ejecutar una sola vez.
"""
from pathlib import Path
from fractions import Fraction as F
import math, re
T = Path(__file__).resolve().parents[1] / 'formulario-t15/tablas'
BS2 = chr(92) * 2
ROW = re.compile(r'^\s*\d+\s*&')
def rows(p): return [l.strip().rstrip().removesuffix(BS2).strip().split(' & ') for l in p.read_text(encoding='utf-8').splitlines() if ROW.match(l)]
def write(p, new):
    it = iter(new)
    out = ['  ' + ' & '.join(next(it)) + ' ' + BS2 if ROW.match(l) else l for l in p.read_text(encoding='utf-8').splitlines()]
    assert next(it, None) is None
    p.write_text('\n'.join(out) + '\n', encoding='utf-8')
p4 = T / 'tab_T15_4.tex'
cur = rows(p4)
APLICADO = cur[20][7] == '1319.88'
assert APLICADO or (cur[20][7] == '703.88' and cur[21][7] == '1990.66'), 'Tabla distinta'
DIA = F(2464, 24)
delta = (11 - 5) * DIA            # 616 HH pasan del mes 22 al mes 21
cents = [[round(F(c) * 100) for c in r[1:8]] for r in cur]
if not APLICADO:
  cents[20][6] += round(delta * 100); cents[21][6] -= round(delta * 100)
assert sum(map(sum, cents)) == 22002300
if not APLICADO: write(p4, [[str(i + 1)] + [f'{v/100:.2f}' for v in r] + [f'{sum(r)/100:.2f}'] for i, r in enumerate(cents)])
# Plazas: techo por perfil antes y después (coordinación 21 conserva 1 plaza en ambos meses).
def plazas(d): return sum(math.ceil(h * d / 128) for h in (16, 24, 56))
d21 = plazas(11) - plazas(5); d22 = plazas(13) - plazas(19)
pp = T / 'tab_T15_4_personas.tex'
pers = rows(pp)
assert pers[20][1] == '20' and pers[21][1] == '29'
for m, d in ((21, d21), (22, d22)):
    r = pers[m - 1]; r[1] = str(int(r[1]) + d); r[7] = str(int(r[7]) + d)
write(pp, pers)
print('delta HH', float(delta), 'plazas', d21, d22)
tot = {int(r[0]): int(r[7]) for r in pers}
for name, a, b in [('Operación', 21, 56), ('E2 cierre', 21, 22), ('E1 prod', 16, 20), ('E2 MB', 19, 20)]:
    print(name, max(tot[m] for m in range(a, b + 1)))
