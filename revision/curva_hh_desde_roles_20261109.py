"""Curva de HH por etapa desde el mismo reparto que las plazas (09-11-2026).

La Tabla tab_T15_4 arrastraba ajustes acumulados y no coincidía mes a mes con la
curva de plazas (tab_T15_4_personas), que sale de horas_por_rol_20261109.py
(reparto uniforme por ventana de la sección 4.1 y coberturas por calendario).
Este script fija el total de cada mes al de ese reparto:
  - meses 1-12: todo en E1 desarrollo; meses 23-56: todo en Operación;
  - meses 13-22: el total del mes se reparte entre las etapas que comparten el
    mes en la misma proporción que tenía la tabla anterior.
Mantiene el total de 219.727,83 HH al centavo. Imprime los totales por etapa.
"""
import re, sys
from pathlib import Path
sys.path.insert(0, str(Path(__file__).resolve().parent))
import horas_por_rol_20261109 as h

BS2 = chr(92) * 2
p4 = h.T / 'tab_T15_4.tex'
ROW = re.compile(r'^\s*\d+\s*&')
lines = p4.read_text(encoding='utf-8').splitlines()
old = {}
for l in lines:
    if ROW.match(l):
        c = [x.strip() for x in l.strip().removesuffix(BS2).strip().split('&')]
        old[int(c[0])] = [float(x) for x in c[1:8]]

tot = {m: sum(h.H[r][m] for r in h.H) for m in range(1, 57)}
cents = {m: round(tot[m] * 100) for m in tot}
drift = round(sum(sum(v) for v in old.values()) * 100) - sum(cents.values())
cents[56] += drift                       # cierre al centavo
assert sum(cents.values()) == 21972783, sum(cents.values())

new = {}
for m in range(1, 57):
    o = [round(x * 100) for x in old[m]]
    share = [x / sum(o) for x in o]
    v = [int(cents[m] * s) for s in share]
    v[max(range(7), key=lambda i: o[i])] += cents[m] - sum(v)
    new[m] = v

out = []
for l in lines:
    if ROW.match(l):
        m = int(l.split('&')[0])
        l = '  ' + ' & '.join([str(m)] + [f'{x/100:.2f}' for x in new[m]] + [f'{sum(new[m])/100:.2f}']) + ' ' + BS2
    out.append(l)
p4.write_text('\n'.join(out) + '\n', encoding='utf-8')

names = ['E1 desarrollo', 'E1 MB', 'E2 desarrollo', 'E2 MB', 'E1 producción', 'Operación', 'E2 cierre']
for i, n in enumerate(names):
    print(n, f'{sum(new[m][i] for m in new)/100:.2f}', 'antes', f'{sum(old[m][i] for m in old):.2f}')
print('total', sum(map(sum, new.values())) / 100)
