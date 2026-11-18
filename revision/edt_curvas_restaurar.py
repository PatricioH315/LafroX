# -*- coding: utf-8 -*-
"""Restaura en tab_T15_4 los meses que la reprogramación no toca (1-4 y 20-56) y verifica totales."""
import io, re, subprocess, sys, os
sys.stdout.reconfigure(encoding='utf-8')
RAIZ = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
P = os.path.join(RAIZ, 'formulario-t15', 'tablas', 'tab_T15_4.tex')
ROW = re.compile(r'^\s*(\d+)\s*&')
viejo = subprocess.run(['git', 'show', 'HEAD:formulario-t15/tablas/tab_T15_4.tex'], cwd=RAIZ, capture_output=True).stdout.decode('utf8').replace('\r\n', '\n')
vo = {int(ROW.match(l).group(1)): l for l in viejo.split('\n') if ROW.match(l)}
L = []
for l in io.open(P, encoding='utf8').read().split('\n'):
    m = ROW.match(l)
    if m and not 5 <= int(m.group(1)) <= 19:
        l = vo[int(m.group(1))]
    L.append(l)
io.open(P, 'w', encoding='utf8', newline='\n').write('\n'.join(L))
def tot(txt):
    s = [0.0] * 8
    for l in txt.split('\n'):
        if ROW.match(l):
            c = [float(x.strip().split()[0]) for x in l.replace(chr(92) * 2, '').split('&')[1:9]]
            s = [a + b for a, b in zip(s, c)]
    return [round(x, 2) for x in s]
print('antes ', tot(viejo))
print('ahora ', tot('\n'.join(L)))
