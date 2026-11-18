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

# EDT por productos (17-11-2026): los módulos de la Etapa 1 y las integraciones reprogramadas
# reparten sus HH por los días hábiles (lunes a viernes) entre su inicio y su fin publicados.
from datetime import timedelta
POR_DIAS = {}
for l in (T / 'tab_T15_paquetes.tex').read_text(encoding='utf-8').splitlines():
    if re.match(r'\s*\d+(\.\d+)+\s*&', l):
        c = [x.strip() for x in l.strip().replace(chr(92) * 2, '').split(' & ')]
        if c[0].startswith('3.4.') or c[0] in ('3.6.4', '3.6.5', '3.6.6'):
            d0 = date(*map(int, c[4].split('-')[::-1])); d1 = date(*map(int, c[5].split('-')[::-1]))
            POR_DIAS[c[0]] = [d0 + timedelta(n) for n in range((d1 - d0).days + 1) if (d0 + timedelta(n)).weekday() < 5]

H = defaultdict(lambda: defaultdict(float))   # H[rol][mes]
def add(role, m, v): H[role][m] += v

for code, cl, role, mm, e in rows:
    a, b = map(int, mm.split('–'))
    if code == '8.1.1':   # B+ (13-11-2026): dedicación declarada, franja 20-22 y formación
        for m in range(a, b + 1):
            k = 1.0 if m < 33 else 0.75 if m < 45 else 0.5
            add('NOC', m, days(m) * 24 * k + 1.9 * monsat(m) + {21: 128, 33: 64, 45: 64}.get(m, 0))
        add('IMP', 21, 16)
        continue
    if code == '8.1.5':
        for m in range(a, b + 1): add('SOC', m, days(m) * 24)
        continue
    if code == '8.1.2':
        for m in range(a, b + 1):
            y, mo = ym(m); rate = 52 if m in (32, 35, 44, 47, 56) else 37   # B+ (13-11-2026)
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
    if code in POR_DIAS:   # EDT por productos (17-11-2026): reparto por días hábiles de la programación
        dd = POR_DIAS[code]
        for d in dd: add(role, (d.year - 2027) * 12 + d.month - 1, e / len(dd))
        continue
    for m in range(a, b + 1): add(role, m, e / (b - a + 1))

for m, v in zip(range(16, 21), (1851, 1786, 1810, 1851, 2038)): add('PUENTE', m, v)
for m in range(13, 21): add('DES', m, 256); add('CAL', m, 128)
for m in range(13, 21): add('SRE', m, 16)
# Roles mínimos de BTT 19.2 (14-11-2026): HH que no reemplazan trabajo de otro perfil
_FAM = {'01': 'JP', '04': 'DES', '05': 'ARQ', '24': 'SRE', '23': 'DAT', '16': 'CAL'}
for _q, _m, _v in json.loads((ROOT / 'revision/roles_minimos_20261114.json').read_text(encoding='utf-8'))['newm']:
    add(_FAM[_q], _m, _v)

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


GROUPS = ['Desarrollo', 'Arq', 'NOC', 'SRE', 'Calidad', 'Seguridad', 'Implantacion', 'Mesa', 'SOC']
PUENTE_MESA = 5664 / 9336   # 4.2.2: puente N1 5.664 HH y puente NOC 3.672 HH (tab_T15_asignacion_partidas)
def group_hours():
    """HH por grupo de origen y mes (14-11-2026: mesa y SOC como orígenes propios) según la regla de reparto del T-15 (sección 4.1) y las
    ventanas de tab_T15_2. La suma de los 56 meses coincide con las 220.023 HH."""
    G = {g: {} for g in GROUPS}
    for m in range(1, 57):
        raw = {
            'Desarrollo': H['JP'][m] + H['DES'][m],
            'Arq': H['ARQ'][m] + H['DAT'][m],
            'NOC': H['NOC'][m] + H['PUENTE'][m] * (1 - PUENTE_MESA) + H['RED'][m],
            'SRE': H['SRE'][m],
            'Calidad': H['CAL'][m],
            'Seguridad': H['SEG'][m],
            'Implantacion': H['IMP'][m],
            'Mesa': H['MESA'][m] + H['PUENTE'][m] * PUENTE_MESA,   # agentes de la mesa de servicios, fuera de la planta técnica (SD1)
            'SOC': H['SOC'][m],                                    # analistas del SOC, dotación adicional (SD1, sección 1.5)
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
