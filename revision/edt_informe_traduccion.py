# -*- coding: utf-8 -*-
"""Informe (sin escribir) de lo que haría el traductor sobre carpetas de subdocumento.
Uso: python revision/edt_informe_traduccion.py carpeta [carpeta ...]"""
import collections, glob, io, os, sys
sys.stdout.reconfigure(encoding='utf-8')
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import edt_recodificar as R
tot = collections.Counter()
for d in sys.argv[1:]:
    archivos = sorted(glob.glob(os.path.join(d, '**', '*.tex'), recursive=True))
    for f in archivos:
        rep = []
        R.traducir(io.open(f, encoding='utf8').read(), rep)
        tot.update(r[0] for r in rep)
        for r in rep:
            if r[0] in ('cuenta-dividida', 'desconocido', 'protegido'):
                print(os.path.relpath(f, d)[:30], r[0], r[1], '|', r[3].replace(chr(10), ' ')[:110])
print(tot)
