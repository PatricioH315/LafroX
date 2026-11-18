# -*- coding: utf-8 -*-
"""Traduce a los códigos de la EDT por productos todos los .tex de las carpetas indicadas.
Uso: python revision/edt_recodificar_carpetas.py carpeta [carpeta ...]"""
import collections, glob, io, os, sys
sys.stdout.reconfigure(encoding='utf-8')
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import edt_recodificar as R
tot = collections.Counter(); n = 0
for d in sys.argv[1:]:
    for f in sorted(glob.glob(os.path.join(d, '**', '*.tex'), recursive=True)):
        t = io.open(f, encoding='utf8').read().replace('\r\n', '\n')
        rep = []
        nt = R.traducir(t, rep)
        tot.update(r[0] for r in rep)
        if nt != t:
            io.open(f, 'w', encoding='utf8', newline='\n').write(nt); n += 1
print('archivos modificados', n, dict(tot))
