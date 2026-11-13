"""Aplica la dotación de operación B+ del SD4, Anexo 4-W.7 (D48), al T-15 (13-11-2026).

Cambios de cobertura (meses 21-56):
  - 8.1.2 mesa: 37 horas-posición por día de lunes a sábado (7 en la hora cargada y
    2 en 15 horas, de 04:00 a 20:00); 52 (tercer agente) solo en septiembre y
    diciembre desde el mes 25 (meses 32, 35, 44, 47 y 56); en septiembre y diciembre
    se mantienen 6 horas-posición de 22:00 a 04:00 y 24 los domingos.
  - 8.1.1 NOC: puesto 24x7 con dedicación declarada de 100 % (meses 21-32),
    75 % (33-44) y 50 % (45-56); franja de mesa de 20:00 a 22:00 con 1,9
    horas-posición por día de lunes a sábado; formación: 8 operadores x 16 h en el
    mes 21 y repasos de 8 x 8 h en los meses 33 y 45, más 16 h del instructor (22).

Actualiza tab_T15_2, tab_T15_4, tab_T15_4_personas, tab_T15_3, tab_T15_10 y tab_T15_8.
Los textos y las demás tablas se editan aparte. Imprime los totales para verificar.
"""
import math, re, sys
from pathlib import Path
sys.path.insert(0, str(Path(__file__).resolve().parent))
import horas_por_rol_20261109 as h

T = h.T
BS2 = chr(92) * 2
PEAK = (32, 35, 44, 47, 56)

def keep(m): return 1.0 if m < 33 else 0.75 if m < 45 else 0.5
TRAIN_NOC = {21: 128, 33: 64, 45: 64}
TRAIN_IMP = {21: 16}

def mesa(m):
    y, mo = h.ym(m)
    rate = 52 if m in PEAK else 37
    v = h.monsat(m) * rate
    if mo in (9, 12): v += h.monsat(m) * 6 + h.sundays(m) * 24
    return v

def noc(m):
    return h.days(m) * 24 * keep(m) + 1.9 * h.monsat(m) + TRAIN_NOC.get(m, 0)

old_mesa = {m: h.H['MESA'][m] for m in range(21, 57)}
old_noc = {m: h.H['NOC'][m] for m in range(21, 57)}
new_mesa = {m: mesa(m) for m in range(21, 57)}
new_noc = {m: noc(m) for m in range(21, 57)}
delta = {m: new_mesa[m] - old_mesa[m] + new_noc[m] - old_noc[m] + TRAIN_IMP.get(m, 0) for m in range(21, 57)}
tot_mesa = round(sum(new_mesa.values()), 2)
tot_noc = round(sum(new_noc.values()), 2)
E811 = round(tot_noc + sum(TRAIN_IMP.values()), 2)
print('mesa', round(sum(old_mesa.values()), 2), '->', tot_mesa)
print('NOC perfil 30', round(sum(old_noc.values()), 2), '->', tot_noc, '| 8.1.1 con instructor', E811)
print('delta total', round(sum(delta.values()), 2))
assert tot_mesa == 38246 and E811 == 21764.2, (tot_mesa, E811)

# 1) tab_T15_2: filas 8.1.1 y 8.1.2
p2 = T / 'tab_T15_2.tex'
s = p2.read_text(encoding='utf-8')
s = s.replace('8.1.1 & C & SRE & 21–56 & 26280.00 & 26280.00 & 26280.00 & 26280.00',
              '8.1.1 & C & SRE & 21–56 & 21764.20 & 21764.20 & 21764.20 & 21764.20')
s = s.replace('8.1.2 & C & SRE & 21–56 & 54239.00 & 54239.00 & 54239.00 & 54239.00',
              '8.1.2 & C & SRE & 21–56 & 38246.00 & 38246.00 & 38246.00 & 38246.00')
assert '21764.20' in s and '38246.00' in s
p2.write_text(s, encoding='utf-8')

# 2) tab_T15_4: columna Operación y total, meses 21-56
p4 = T / 'tab_T15_4.tex'
out = []
for l in p4.read_text(encoding='utf-8').splitlines():
    if re.match(r'^\s*\d+\s*&', l):
        c = [x.strip() for x in l.strip().removesuffix(BS2).strip().split('&')]
        m = int(c[0])
        if m >= 21:
            v = [round(float(x) * 100) for x in c[1:9]]
            v[5] += round(delta[m] * 100)
            v[7] = sum(v[:7])
            l = '  ' + ' & '.join([str(m)] + [f'{x/100:.2f}' for x in v]) + ' ' + BS2
    out.append(l)
p4.write_text('\n'.join(out) + '\n', encoding='utf-8')
op = sum(float(l.split('&')[6]) for l in out if re.match(r'^\s*\d+\s*&', l))
tot = sum(float(l.split('&')[8].replace(BS2, '')) for l in out if re.match(r'^\s*\d+\s*&', l))
print('tab_T15_4 Operación', round(op, 2), 'total', round(tot, 2))

# 3) plazas por grupo: se recalculan con la nueva cobertura
for m in range(21, 57):
    h.H['MESA'][m] = new_mesa[m]
    h.H['NOC'][m] = new_noc[m]
    h.H['IMP'][m] += TRAIN_IMP.get(m, 0)
G = h.write_personas()
rows = {}
for l in (T / 'tab_T15_4_personas.tex').read_text(encoding='utf-8').splitlines():
    if re.match(r'^\s*\d+\s*&', l):
        c = [int(x.strip().replace(BS2, '')) for x in l.split('&')]
        rows[c[0]] = c[1:]
peak_op = max(rows[m][-1] for m in range(21, 57))
peak_e2 = max(rows[m][-1] for m in (21, 22))
noc_max = max(rows[m][2] for m in range(1, 57))
noc_months = [m for m in range(1, 57) if rows[m][2] == noc_max]
print('plazas: máximo operación', peak_op, '| E2 cierre', peak_e2, '| NOC y redes', noc_max, noc_months)

# 4) tab_T15_3: fila Operación y peak de E2 cierre
p3 = T / 'tab_T15_3.tex'
s = p3.read_text(encoding='utf-8')
s = re.sub(r'(Operación & )128917\.97 & 0 & 128917\.97( & F1,\\allowbreak\{\}F8 & 21–56 & )\d+',
           lambda mo: f'{mo.group(1)}{op:.2f} & 0 & {op:.2f}{mo.group(2)}{peak_op}', s)
s = re.sub(r'(E2 Cierre y estabilización posterior al H12 & 2690\.22 & 0 & 2690\.22 & [^&]+& 21–22 & )\d+',
           lambda mo: f'{mo.group(1)}{peak_e2}', s)
assert f'{op:.2f}' in s
p3.write_text(s, encoding='utf-8')

# 5) tab_T15_10: E HH y relevos (regla de la sección 6: quincena / 64 HH)
def relevos(series):
    n = [2 * math.ceil(x / 2 / 64) for x in series]
    return sum(n), max(x / k for x, k in zip(series, n))
r1, x1 = relevos([new_noc[m] + TRAIN_IMP.get(m, 0) for m in range(21, 57)])
r2, x2 = relevos([new_mesa[m] for m in range(21, 57)])
p10 = T / 'tab_T15_10.tex'
s = p10.read_text(encoding='utf-8')
s = re.sub(r'(8\.1\.1 & C & SRE & 21–56 & )26280( & .*? & )432 & 62\.0',
           lambda mo: f'{mo.group(1)}21764.2{mo.group(2)}{r1} & {x1:.1f}', s)
s = re.sub(r'(8\.1\.2 & C & SRE & 21–56 & )54239( & .*? & )679 & 79\.9',
           lambda mo: f'{mo.group(1)}38246{mo.group(2)}{r2} & {x2:.1f}', s)
assert '21764.2' in s and '38246' in s
p10.write_text(s, encoding='utf-8')
print('relevos 8.1.1', r1, round(x1, 1), '| 8.1.2', r2, round(x2, 1))

# 6) tab_T15_8: demanda máxima de NOC y redes
p8 = T / 'tab_T15_8.tex'
s = p8.read_text(encoding='utf-8')
meses = ', '.join(map(str, noc_months[:-1])) + (' y ' if len(noc_months) > 1 else '') + str(noc_months[-1])
s = re.sub(r'(NOC 24×7 y redes de Infraestructura & 32 & 29 & )\d+ & [^\\]+',
           lambda mo: f'{mo.group(1)}{noc_max} & {meses} ', s)
p8.write_text(s, encoding='utf-8')

# 7) actualiza la regla del generador para que la validación siga cuadrando
gen = Path(__file__).resolve().parent / 'horas_por_rol_20261109.py'
g = gen.read_text(encoding='utf-8')
old_rule = """    if code == '8.1.1':
        for m in range(a, b + 1): add('NOC', m, days(m) * 24)
        continue"""
new_rule = """    if code == '8.1.1':   # B+ (13-11-2026): dedicación declarada, franja 20-22 y formación
        for m in range(a, b + 1):
            k = 1.0 if m < 33 else 0.75 if m < 45 else 0.5
            add('NOC', m, days(m) * 24 * k + 1.9 * monsat(m) + {21: 128, 33: 64, 45: 64}.get(m, 0))
        add('IMP', 21, 16)
        continue"""
old_mesa_rule = "y, mo = ym(m); rate = 41 if m < 25 else 58"
new_mesa_rule = "y, mo = ym(m); rate = 52 if m in (32, 35, 44, 47, 56) else 37   # B+ (13-11-2026)"
if old_rule in g:
    g = g.replace(old_rule, new_rule).replace(old_mesa_rule, new_mesa_rule)
    gen.write_text(g, encoding='utf-8')
    print('generador actualizado')
