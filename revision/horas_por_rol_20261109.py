"""Horas mensuales por rol y grupo de origen del T-15 (09-11-2026).

Reconstruye la curva de HH por rol con las reglas de la sección 4.1 del T-15:
reparto uniforme en la ventana, coberturas por calendario (NOC, SOC, mesa),
soporte puente, reserva protegida, restauraciones, 4.2.2 por previsión mensual,
4.3.2 y 3.9.2-3.9.7 por días. Valida contra el total mensual de tab_T15_4.
Calcula la demanda de plazas por grupo como techo(HH del grupo / 128).
"""
import re, calendar, math, json, sys
from collections import defaultdict
from datetime import date
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
T = ROOT / 'formulario-t15/tablas'

def ym(m):  # mes 1 = febrero de 2027
    y = 2027 + (m) // 12; mm = (m) % 12 + 1
    return y, mm

def days(m): return calendar.monthrange(*ym(m))[1]
def monsat(m):
    y, mm = ym(m); return sum(1 for d in range(1, days(m) + 1) if date(y, mm, d).weekday() < 6)
def sundays(m): return days(m) - monsat(m)

rows = []
for l in (T / 'tab_T15_2.tex').read_text(encoding='utf-8').splitlines():
    if re.match(r'\s*\d+(\.\d+)+\s*&', l):
        c = [x.strip() for x in l.strip().replace(chr(92) * 2, '').split('&')]
        rows.append((c[0], c[1], c[2], c[3], float(c[7])))

H = defaultdict(lambda: defaultdict(float))   # H[rol][mes]
def add(role, m, v): H[role][m] += v

for code, cl, role, mm, e in rows:
    a, b = map(int, mm.split('–'))
    if code == '8.1.1':
        for m in range(a, b + 1): add('NOC', m, days(m) * 24)
        continue
    if code == '8.1.5':
        for m in range(a, b + 1): add('SOC', m, days(m) * 24)
        continue
    if code == '8.1.2':
        for m in range(a, b + 1):
            y, mo = ym(m); rate = 41 if m < 25 else 58
            v = monsat(m) * rate
            if mo in (9, 12): v += monsat(m) * 6 + sundays(m) * 24
            add('MESA', m, v)
        continue
    if code == '4.2.2':
        for m, v in zip(range(16, 21), (2464, 1312, 544, 544, 544)): add(role, m, v)
        continue
    if code == '4.3.2':
        add(role, 21, 2464 * 11 / 24); add(role, 22, 2464 * 13 / 24)
        continue
    for m in range(a, b + 1): add(role, m, e / (b - a + 1))

for m, v in zip(range(16, 21), (1851, 1786, 1810, 1851, 2038)): add('PUENTE', m, v)
for m in range(13, 21): add('DES', m, 256); add('CAL', m, 128)
for m in range(13, 21): add('SRE', m, 16)

ref = {}
for l in (T / 'tab_T15_4.tex').read_text(encoding='utf-8').splitlines():
    if re.match(r'^\s*\d+\s*&', l):
        c = [x.strip().split()[0] for x in l.split('&')]; ref[int(c[0])] = float(c[-1])

if __name__ == '__main__':
    tot = {m: sum(H[r][m] for r in H) for m in range(1, 57)}
    print('total reconstruido', round(sum(tot.values()), 2), 'publicado', round(sum(ref.values()), 2))
    for m in range(1, 57):
        d = tot[m] - ref[m]
        if abs(d) > 1: print('mes', m, 'reconstr', round(tot[m], 2), 'publicado', ref[m], 'dif', round(d, 2))
    print('mesa total', round(sum(H['MESA'].values()), 2), 'NOC', round(sum(H['NOC'].values()), 2), 'SOC', round(sum(H['SOC'].values()), 2))


GROUPS = ['Desarrollo', 'Arq', 'NOC', 'SRE', 'Calidad', 'Seguridad', 'Implantacion']
def group_hours():
    """HH por grupo y mes según la regla de reparto del T-15 (sección 4.1) y las
    ventanas de tab_T15_2. La suma de los 56 meses coincide con las 220.023 HH."""
    G = {g: {} for g in GROUPS}
    for m in range(1, 57):
        raw = {
            'Desarrollo': H['JP'][m] + H['DES'][m],
            'Arq': H['ARQ'][m] + H['DAT'][m],
            'NOC': H['NOC'][m] + H['MESA'][m] + H['PUENTE'][m] + H['RED'][m] + H['SOC'][m] * 2 / 6,
            'SRE': H['SRE'][m],
            'Calidad': H['CAL'][m],
            'Seguridad': H['SEG'][m] + H['SOC'][m] * 4 / 6,
            'Implantacion': H['IMP'][m],
        }
        for g in GROUPS: G[g][m] = raw[g]
    return G

def write_personas():
    G = group_hours()
    p = T / 'tab_T15_4_personas.tex'
    out = []
    for l in p.read_text(encoding='utf-8').splitlines():
        if re.match(r'^\s*\d+\s*&', l):
            m = int(l.split('&')[0])
            v = [math.ceil(round(G[g][m], 6) / 128) for g in GROUPS]
            l = '  ' + ' & '.join(map(str, [m] + v + [sum(v)])) + ' ' + chr(92) * 2
        out.append(l)
    p.write_text('\n'.join(out) + '\n', encoding='utf-8')
    return G
