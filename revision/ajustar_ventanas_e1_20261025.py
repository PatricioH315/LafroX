"""Ajusta las ventanas internas de la Etapa 1 que el CPM marcaba con holgura negativa.

3.4.10 pasa de los meses 5-8 a 5-9 y 3.8.7 del mes 10 a los meses 10-11; las fechas
publicadas de 3.8.1-3.8.8 se alinean con las calculadas (3.4.10 conserva su duración y
termina el 04-10-2027 por la integración posterior a la entrega de 3.4.8). Corrige además el
promedio de personas cuando no alcanza para ejecutar las HH en la duración del paquete.
Las HH totales no cambian. Ejecutar una sola vez, después de reprogramar_h12_e2_20261025.py.
"""
from pathlib import Path
from fractions import Fraction as F
import json
import math
import re

ROOT = Path(__file__).resolve().parents[1]
T = ROOT / 'formulario-t15/tablas'
ROW = re.compile(r'^\s*\d+(?:\.\d+)*\s*&')
END = ' \\\\'


def replace_cells(path, code, cells):
    """Reemplaza columnas (índice -> valor) de la fila cuyo código coincide."""
    lines = path.read_text(encoding='utf-8').splitlines()
    hits = 0
    for n, l in enumerate(lines):
        c = l.strip().removesuffix('\\\\').strip().split(' & ')
        if ROW.match(l) and c[0] == code:
            for i, v in cells.items():
                c[i] = v
            lines[n] = '  ' + ' & '.join(c) + END
            hits += 1
    assert hits == 1, (path.name, code, hits)
    path.write_text('\n'.join(lines) + '\n', encoding='utf-8')


if '  3.4.10 & D & DES & 5–8 &' not in (T / 'tab_T15_2.tex').read_text(encoding='utf-8'):
    raise SystemExit('El ajuste ya está aplicado; volver a ejecutarlo duplicaría los deltas.')

# Ventanas mensuales (tab_T15_2, columna 3)
replace_cells(T / 'tab_T15_2.tex', '3.4.10', {3: '5–9'})
replace_cells(T / 'tab_T15_2.tex', '3.8.7', {3: '10–11'})

# Fechas publicadas (tab_T15_paquetes, columnas 4 y 5) iguales a las calculadas
DATES = {'3.8.1': ('05-10-2027', '22-10-2027'),
         '3.8.2': ('25-10-2027', '19-11-2027'), '3.8.3': ('25-10-2027', '19-11-2027'),
         '3.8.4': ('25-10-2027', '11-11-2027'), '3.8.5': ('25-10-2027', '11-11-2027'),
         '3.8.6': ('25-10-2027', '11-11-2027'), '3.8.8': ('25-10-2027', '11-11-2027'),
         '3.8.7': ('22-11-2027', '01-12-2027')}
for code, (a, b) in DATES.items():
    replace_cells(T / 'tab_T15_paquetes.tex', code, {4: a, 5: b})

# Curva de HH: 3.4.10 (DES) reparte 960 HH en 5 meses; 3.8.7 (CAL) 160 HH en 2 meses.
delta = {(m, 'DES'): F(960, 5) - F(960, 4) for m in range(5, 9)}
delta[9, 'DES'] = F(960, 5)
delta[10, 'CAL'] = F(-80)
delta[11, 'CAL'] = F(80)
assert sum(delta.values()) == 0

def rows(path):
    return [l.strip().removesuffix('\\\\').strip().split(' & ')
            for l in path.read_text(encoding='utf-8').splitlines() if re.match(r'^\s*\d+\s*&', l)]

def write(path, new):
    it = iter(new)
    out = ['  ' + ' & '.join(next(it)) + END if re.match(r'^\s*\d+\s*&', l) else l
           for l in path.read_text(encoding='utf-8').splitlines()]
    assert next(it, None) is None
    path.write_text('\n'.join(out) + '\n', encoding='utf-8')

cur = rows(T / 'tab_T15_4.tex')
cents = [[round(F(c) * 100) for c in r[1:8]] for r in cur]
for (m, _), v in delta.items():
    cents[m - 1][0] += round(v * 100)          # todo es Etapa 1 · desarrollo
assert sum(map(sum, cents)) == 22002300
write(T / 'tab_T15_4.tex',
      [[str(i + 1)] + [f'{v / 100:.2f}' for v in r] + [f'{sum(r) / 100:.2f}'] for i, r in enumerate(cents)])

ROLES = ['JP', 'ARQ', 'SEG', 'DAT', 'DES', 'CAL', 'SRE', 'IMP']
pers = rows(T / 'tab_T15_4_personas.tex')
for r in pers:
    m = int(r[0])
    for j, role in enumerate(ROLES):
        v = delta.get((m, role), 0)
        if v > 0:
            r[j + 1] = str(int(r[j + 1]) + math.ceil(v / 128))
        elif v < 0:
            r[j + 1] = str(int(r[j + 1]) - math.floor(-v / 128))
    r[9] = str(sum(int(x) for x in r[1:9]))
write(T / 'tab_T15_4_personas.tex', pers)
print({int(r[0]): int(r[9]) for r in pers if 4 <= int(r[0]) <= 12})
