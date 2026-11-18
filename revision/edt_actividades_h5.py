# -*- coding: utf-8 -*-
"""Tabla compacta de actividades de los paquetes con entregable que terminan entre el H2 y el H5
(17-11-2026). Una fila por paquete: clase, actividades de hasta 80 HH según la plantilla de su
clase (T-15, sección 6.1), y quincenas de ejecución. Escribe formulario-t15/tablas/tab_T15_9h5.tex.
"""
import io, math, os, re, sys
from datetime import date, timedelta
sys.stdout.reconfigure(encoding='utf-8')
RAIZ = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
T = os.path.join(RAIZ, 'formulario-t15', 'tablas')
BS = chr(92); BS2 = BS * 2
ROW = re.compile(r'\s*(\d+(?:\.\d+)+)\s*&')

def leer(n): return io.open(os.path.join(T, n), encoding='utf8').read()
cls = {}
for l in leer('tab_T15_2.tex').splitlines():
    m = re.match(r'\s*(\d+(?:\.\d+)+)\s*&\s*(\w+)\s*&', l)
    if m: cls[m.group(1)] = m.group(2)
ya = set()
for n in ('tab_T15_9_bloque_1.tex', 'tab_T15_9_bloque_2.tex'):
    for l in leer(n).splitlines():
        m = re.match(r'\s*(\d+(?:\.\d+)+)\.A\d+', l)
        if m: ya.add(m.group(1))
def d(s): return date(*map(int, s.split('-')[::-1]))
def quincena(x): return '%s/%s' % ('1.ª' if x.day <= 15 else '2.ª', x.strftime('%m/%Y'))
def quincenas(a, b):
    out = []; x = a
    while x <= b:
        q = quincena(x)
        if q not in out: out.append(q)
        x += timedelta(1)
    return out

PLANT = {  # secuencia de la plantilla por clase (T-15, sección 6.1)
 'G': ['elaboración, revisión y aprobación del entregable'],
 'E': ['levantamiento de insumos y análisis', 'elaboración del entregable', 'revisión, corrección y presentación para aprobación'],
 'I': ['análisis con muestras reales', 'contrato de interfaz', 'adaptador', 'pruebas de falla y de lentitud', 'integración en QA', 'entrega'],
 'T': ['preparación y ejecución de la instalación o de la capacitación', 'prueba o evaluación, corrección y acta'],
 'V': ['preparación de datos y casos', 'primer ciclo', 'segundo ciclo y regresión', 'informe y acta'],
}
filas = []
for l in leer('tab_T15_paquetes.tex').splitlines():
    m = ROW.match(l)
    if not m: continue
    c = [x.strip() for x in l.replace(BS2, '').split(' & ')]
    cod, hh, a, b = c[0], float(c[3].replace(',', '.')), d(c[4]), d(c[5])
    if cod in ya or b > date(2028, 1, 31): continue
    k = cls[cod]; n = max(1, math.ceil(hh / 80))
    if k == 'D':
        iters = (b - a).days // 14 + 1
        sec = 'A01–A02: análisis y contratos de interfaz; A03–A%02d: construcción en %d iteraciones de 14 días con pruebas del incremento y demostración; A%02d–A%02d: pruebas de contrato, integración en QA y entrega' % (n - 2, iters, n - 1, n)
    else:
        base = PLANT[k]
        if n <= len(base):
            sec = '; '.join('A%02d: %s' % (i + 1, t) for i, t in enumerate(base[:n - 1] + [base[-1]] if n < len(base) else base))
        else:  # más HH que la plantilla: el trabajo central se divide en actividades de hasta 80 HH
            extra = n - len(base); medio = len(base) // 2
            partes = []; i = 1
            for j, t in enumerate(base):
                reps = 1 + (extra if j == medio else 0)
                if reps == 1: partes.append('A%02d: %s' % (i, t))
                else: partes.append('A%02d–A%02d: %s' % (i, i + reps - 1, t))
                i += reps
            sec = '; '.join(partes)
    q = quincenas(a, b)
    qtxt = q[0] if len(q) == 1 else '%s a %s (%d)' % (q[0], q[-1], len(q))
    filas.append((cod, k, n, '%.2f' % (hh / n), sec, qtxt))
filas.sort(key=lambda f: [int(x) for x in f[0].split('.')])
L = [BS + 'begin{tablalafrox}{Actividades de los paquetes que terminan entre el H2 y el H5. Fuente: elaboración a partir de la Tabla ' + BS + 'ref{tab_T15_paquetes} y de las plantillas por clase de esta sección.}{tab_T15_9h5}',
     '  {L{1.2cm} C{0.8cm} C{1.1cm} C{1.2cm} Y L{2.6cm}}',
     '  {' + BS + 'cab{Paquete} & ' + BS + 'cab{Clase} & ' + BS + 'cab{Activi\\-dades} & ' + BS + 'cab{HH por actividad} & ' + BS + 'cab{Secuencia} & ' + BS + 'cab{Quincenas}}']
for cod, k, n, h, sec, q in filas:
    L.append('  %s & %s & %d & %s & %s & %s %s' % (cod, k, n, h.replace('.', ','), sec, q, BS2))
L.append(BS + 'end{tablalafrox}')
io.open(os.path.join(T, 'tab_T15_9h5.tex'), 'w', encoding='utf8', newline='\n').write('\n'.join(L) + '\n')
print('paquetes', len(filas), 'actividades', sum(f[2] for f in filas))
