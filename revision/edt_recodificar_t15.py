# -*- coding: utf-8 -*-
"""Traduce el T-15 a los códigos de la EDT por productos y reordena las filas por código (17-11-2026)."""
import glob, io, os, re, sys
sys.stdout.reconfigure(encoding='utf-8')
AQUI = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, AQUI)
import edt_recodificar as R
RAIZ = os.path.dirname(AQUI)
F15 = os.path.join(RAIZ, 'formulario-t15')
ROW = re.compile(r'^\s*(\d+(?:\.\d+)+)((?:\.A\d+)?)\s*&')

def clave(l):
    m = ROW.match(l)
    nums = [int(x) for x in m.group(1).split('.')]
    suf = m.group(2)
    return (nums, int(suf[2:]) if suf else 0)

def ordenar(texto):
    """Ordena por código cada bloque contiguo de filas que empiezan con un código (orden estable)."""
    L = texto.split('\n'); out = []; i = 0
    while i < len(L):
        if ROW.match(L[i]):
            j = i
            while j < len(L) and ROW.match(L[j]):
                j += 1
            bloque = L[i:j]
            # la última fila del bloque puede no terminar en \\ si es la última de la tabla: normalizar
            out.extend(sorted(bloque, key=clave))
            i = j
        else:
            out.append(L[i]); i += 1
    return '\n'.join(out)

rep = []
archivos = [os.path.join(F15, 'contenido.tex')] + sorted(glob.glob(os.path.join(F15, 'tablas', '*.tex')))
ORDENAR = {'tab_T15_2.tex', 'tab_T15_paquetes.tex', 'tab_T15_cpm_detalle.tex', 'tab_T15_asignacion_partidas.tex',
           'tab_T15_10.tex', 'tab_T15_conciliacion.tex', 'tab_T15_pert_riesgo.tex', 'tab_T15_tamano.tex',
           'tab_T15_tamano_motivos.tex', 'tab_T15_tamano_detalle.tex', 'tab_T15_9_bloque_1.tex', 'tab_T15_9_bloque_2.tex'}
for p in archivos:
    t = io.open(p, encoding='utf8').read().replace('\r\n', '\n')
    n = R.traducir(t, rep)
    if os.path.basename(p) == 'tab_T15_paquetes.tex':
        n = n.replace('3.3 (CC)', '3.3 (CC), 5.1 (CC)')
    if os.path.basename(p) in ORDENAR:
        n = ordenar(n)
    if os.path.basename(p) == 'contenido.tex':
        # calendario de iteraciones: filas de módulos ordenadas por código nuevo
        n = re.sub(r'((?:^\s*\d+\.\d+\.\d+ & 20\d\d & .*\n)+)', lambda m: '\n'.join(sorted(m.group(1).rstrip('\n').split('\n'), key=lambda l: [int(x) for x in l.split('&')[0].split('.')])) + '\n', n, flags=re.M)
    if n != t:
        io.open(p, 'w', encoding='utf8', newline='\n').write(n)
from collections import Counter
print(Counter(r[0] for r in rep))
