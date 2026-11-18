# -*- coding: utf-8 -*-
"""Actualiza los totales por etapa (tab_T15_3 y tab_SD7_13) con las diferencias de la reprogramación."""
import io, os, sys
sys.stdout.reconfigure(encoding='utf-8')
RAIZ = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
DELTA = {  # nuevo − anterior, por columna de tab_T15_4
 'E1 Desarrollo': 258.00, 'E1 Marcha blanca': -51.20, 'E2 Desarrollo': -29.26,
 'E2 Marcha blanca': -97.69, 'E1 Producción y estabilización': -79.85}
PICO = {'E1 Desarrollo': ('60', '51'), 'E2 Desarrollo': ('57', '58')}
SD7 = {'Etapa 1 · Desarrollo': 'E1 Desarrollo', 'Etapa 1 · Marcha blanca': 'E1 Marcha blanca',
       'Etapa 2 · Desarrollo': 'E2 Desarrollo', 'Etapa 2 · Marcha blanca': 'E2 Marcha blanca',
       'Etapa 1 · Producción y estabilización': 'E1 Producción y estabilización'}
def es(x):  # 12345.6 -> 12.345,60
    s = '%.2f' % x; e, d = s.split('.'); e = '{:,}'.format(int(e)).replace(',', '.'); return e + ',' + d
def num(s): return float(s.replace('.', '').replace(',', '.')) if ',' in s else float(s)

p = os.path.join(RAIZ, 'formulario-t15', 'tablas', 'tab_T15_3.tex'); L = []
for l in io.open(p, encoding='utf8').read().split('\n'):
    c = l.split(' & ')
    k = c[0].strip()
    if k in DELTA:
        a, r, t = float(c[1]), float(c[2]), float(c[3])
        a2 = round(a + DELTA[k], 2); t2 = round(a2 + r, 2)
        c[1] = '%.2f' % a2; c[3] = '%.2f' % t2
        if k in PICO:
            tail = c[-1].strip().split(' ', 1)
            assert tail[0] == PICO[k][0], (k, tail)
            c[-1] = ' ' + PICO[k][1] + ' ' + tail[1]
        print('T-15', k, c[1], c[3])
    L.append(' & '.join(c))
io.open(p, 'w', encoding='utf8', newline='\n').write('\n'.join(L))

if '--solo-t15' in sys.argv: sys.exit(0)
p = os.path.join(RAIZ, 'subdocumento-07', 'tablas', 'tab_SD7_13.tex'); L = []
for l in io.open(p, encoding='utf8').read().split('\n'):
    c = l.split(' & ')
    k = c[0].strip()
    if k in SD7:
        a, r = num(c[2].strip()), num(c[3].strip())
        a2 = round(a + DELTA[SD7[k]], 2)
        c[2] = es(a2); c[4] = es(round(a2 + r, 2)) + ' ' + chr(92) * 2
        print('SD7', k, c[2], c[4])
    L.append(' & '.join(c))
io.open(p, 'w', encoding='utf8', newline='\n').write('\n'.join(L))
