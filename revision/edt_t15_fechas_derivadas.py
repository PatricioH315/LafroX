# -*- coding: utf-8 -*-
"""Actualiza tablas del T-15 que derivan de la programación (17-11-2026), en códigos vigentes:
- columna de meses de tab_T15_asignacion_partidas según tab_T15_2;
- calendario de iteraciones de 14 días de los módulos 3.4.x según tab_T15_paquetes.
Imprime el número de ventanas de iteración resultante.
"""
import io, os, re, sys
from datetime import date, timedelta
sys.stdout.reconfigure(encoding='utf-8')
RAIZ = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
T = os.path.join(RAIZ, 'formulario-t15', 'tablas')
C = os.path.join(RAIZ, 'formulario-t15', 'contenido.tex')
BS2 = chr(92) * 2
ROW = re.compile(r'\s*(\d+(?:\.\d+)+)\s*&')

def leer(p): return io.open(p, encoding='utf8').read()
def escribir(p, t): io.open(p, 'w', encoding='utf8', newline='\n').write(t)

meses = {}
for l in leer(os.path.join(T, 'tab_T15_2.tex')).splitlines():
    m = ROW.match(l)
    if m: meses[m.group(1)] = [x.strip() for x in l.split('&')][3]
fechas = {}
for l in leer(os.path.join(T, 'tab_T15_paquetes.tex')).splitlines():
    m = ROW.match(l)
    if m:
        c = [x.strip() for x in l.replace(BS2, '').split(' & ')]
        fechas[c[0]] = (date(*map(int, c[4].split('-')[::-1])), date(*map(int, c[5].split('-')[::-1])))

# 1. asignación por partida: columna de meses (4.ª)
p = os.path.join(T, 'tab_T15_asignacion_partidas.tex'); L = []; n = 0
for l in leer(p).splitlines():
    m = ROW.match(l)
    if m and m.group(1) in meses:
        c = l.split(' & ')
        if len(c) >= 5 and re.fullmatch(r'\d+–\d+', c[3].strip()) and c[3].strip() != meses[m.group(1)]:
            c[3] = meses[m.group(1)]; l = ' & '.join(c); n += 1
    L.append(l)
escribir(p, '\n'.join(L) + '\n'); print('asignación por partida: filas cambiadas', n)

# 2. iteraciones de 14 días corridos de los módulos 3.4.x
def ventanas(a, b):
    out = []; s = a
    while s <= b:
        e = min(s + timedelta(13), b); out.append((s, e)); s = e + timedelta(1)
    return out
t = leer(C); L = []; total = 0
for l in t.splitlines():
    m = re.match(r'(\s*)(3\.4\.\d+) & 2027 & .*$', l)
    if m:
        a, b = fechas[m.group(2)]
        v = ventanas(a, b); total += len(v)
        l = '%s%s & 2027 & %s %s' % (m.group(1), m.group(2), ', '.join(x.strftime('%d/%m') if x == y else '%s--%s' % (x.strftime('%d/%m'), y.strftime('%d/%m')) for x, y in v), BS2)
    elif re.match(r'\s*3\.5\.\d+ & 2028 & ', l):
        total += l.count('--')
    L.append(l)
escribir(C, '\n'.join(L) + '\n'); print('ventanas de iteración de los 15 módulos:', total)
