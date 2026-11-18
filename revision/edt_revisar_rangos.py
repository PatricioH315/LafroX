# -*- coding: utf-8 -*-
"""Detecta rangos de códigos de paquete («X–Y», «X a Y») que tras la traducción ya no describen
el mismo conjunto de paquetes. Uso: python revision/edt_revisar_rangos.py archivo.tex ..."""
import io, json, os, re, sys
sys.stdout.reconfigure(encoding='utf-8')
RAIZ = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
MAPA = json.load(io.open(os.path.join(RAIZ, 'revision', 'edt_equivalencias_20261117.json'), encoding='utf8'))
INV = {v: k for k, v in MAPA.items()}
def k(c): return [int(x) for x in c.split('.')]
RX = re.compile(r'(?<![\d.])(\d{1,2}\.\d{1,2}\.\d{1,2})\s*(?:–|--|-|\s+a\s+)\s*(\d{1,2}\.\d{1,2}\.\d{1,2})(?![\d]|\.\d)')
for f in sys.argv[1:]:
    t = io.open(f, encoding='utf8').read()
    for m in RX.finditer(t):
        a, b = m.group(1), m.group(2)
        if a not in INV or b not in INV: continue
        mismo = a.rsplit('.', 1)[0] == b.rsplit('.', 1)[0]
        nuevos = [c for c in INV if c.rsplit('.', 1)[0] == a.rsplit('.', 1)[0] and k(a) <= k(c) <= k(b)] if mismo else None
        viejos_a, viejos_b = INV[a], INV[b]
        viejos_rango = [c for c in MAPA if c.rsplit('.', 1)[0] == viejos_a.rsplit('.', 1)[0] and k(viejos_a) <= k(c) <= k(viejos_b)] if viejos_a.rsplit('.', 1)[0] == viejos_b.rsplit('.', 1)[0] else None
        ok = mismo and viejos_rango is not None and sorted(MAPA[c] for c in viejos_rango) == sorted(nuevos)
        if not ok:
            print('%s: «%s» (antes %s–%s) | %s' % (os.path.basename(f), m.group(0), viejos_a, viejos_b, t[max(0, m.start() - 60):m.end() + 20].replace('\n', ' ')))
