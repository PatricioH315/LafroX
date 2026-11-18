# -*- coding: utf-8 -*-
"""Frentes de trabajo (tab_T15_1) en cuentas nuevas y rangos de paquetes partidos tras la traducción."""
import io, json, os, re, sys
sys.stdout.reconfigure(encoding='utf-8')
RAIZ = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
MAPA = json.load(io.open(os.path.join(RAIZ, 'revision', 'edt_equivalencias_20261117.json'), encoding='utf8'))
CUENTAS = {}
for v, n in MAPA.items():
    CUENTAS.setdefault('.'.join(n.split('.')[:2]), []).append(v)

# frente -> (cuentas o paquetes nuevos, texto adicional)
FRENTES = {
 'F1': ('1.1 a 1.3, 1.5, 1.6.1, 1.6.2, 1.7, 1.8, 2.1, 6.8.6, 6.8.7, 7.4.1, 9.7, 10.3, 10.5', ''),
 'F2': ('2.2 a 2.6, 2.7.1, 2.7.2, 2.8, 3.3, 5.1, 5.4, 6.8.1 a 6.8.5', ''),
 'F3': ('4.1 a 4.3, 4.5.1, 5.2, 7.1, 7.2.1 a 7.2.4, 7.3.1 a 7.3.4', '; capacidad protegida 9.3.1'),
 'F4': ('4.4, 4.5.2, 5.3, 7.5.1 a 7.5.4', ''),
 'F5': ('3.1, 3.2, 8.1 a 8.7', '; soporte 9.3.1'),
 'F6': ('1.4, 6.1 a 6.7', ''),
 'F7': ('2.7.3, 9.1 a 9.6', ''),
 'F8': ('1.6.3, 7.2.5, 7.3.5, 7.4.2, 7.4.3, 7.5.5, 7.5.6, 10.1, 10.2, 10.4', ''),
}
# control: cada paquete nuevo pertenece a lo sumo a un frente
def expandir(s):
    out = []
    for tok in [x.strip() for x in s.split(',')]:
        if ' a ' in tok:
            a, b = tok.split(' a ')
            if a.count('.') == 1:
                n1 = a.split('.')[0]; ia, ib = int(a.split('.')[1]), int(b.split('.')[1])
                for i in range(ia, ib + 1): out += [MAPA[v] for v in CUENTAS.get('%s.%d' % (n1, i), [])]
            else:
                pre = a.rsplit('.', 1)[0]; ia, ib = int(a.rsplit('.', 1)[1]), int(b.rsplit('.', 1)[1])
                out += ['%s.%d' % (pre, i) for i in range(ia, ib + 1)]
        elif tok.count('.') == 1:
            out += [MAPA[v] for v in CUENTAS.get(tok, [])]
        else:
            out.append(tok)
    return out
visto = {}
for f, (s, _) in FRENTES.items():
    for p in expandir(s):
        assert p in set(MAPA.values()), (f, p)
        assert p not in visto, (p, visto.get(p), f)
        visto[p] = f
print('paquetes asignados a frentes:', len(visto), 'de', len(MAPA))
print('sin frente:', sorted(set(MAPA.values()) - set(visto), key=lambda c: [int(x) for x in c.split('.')]))

p = os.path.join(RAIZ, 'formulario-t15', 'tablas', 'tab_T15_1.tex'); L = []
for l in io.open(p, encoding='utf8').read().split('\n'):
    m = re.match(r'(\s*)(F\d)( [^&]*& [^&]*& )([^&]*)( & .*)$', l)
    if m:
        s, extra = FRENTES[m.group(2)]
        l = m.group(1) + m.group(2) + m.group(3) + s + extra + m.group(5)
    L.append(l)
io.open(p, 'w', encoding='utf8', newline='\n').write('\n'.join(L))

RANGOS = [  # (archivo, texto partido, texto correcto)
 ('formulario-t15/contenido.tex', 'Las pruebas de certificación 6.2.3–6.6.2', 'Las pruebas de certificación 6.2.3, 6.3.2, 6.4.2, 6.5.2, 6.6.2 y 6.7.2'),
 ('formulario-t15/contenido.tex', 'los paquetes de pruebas 6.2.1 a 6.4.1', 'los paquetes de pruebas 6.2.1, 6.2.2, 6.3.1 y 6.4.1'),
 ('formulario-t15/tablas/tab_T15_5.tex', 'Certificación E1 (H5) & 6.2.1–6.6.1', 'Certificación E1 (H5) & 6.2.1, 6.2.2, 6.3.1, 6.4.1, 6.5.1 y 6.6.1'),
 ('formulario-t15/tablas/tab_T15_5.tex', 'Certificación E2 (H10) & 6.2.3–6.6.2', 'Certificación E2 (H10) & 6.2.3, 6.3.2, 6.4.2, 6.5.2, 6.6.2 y 6.7.2'),
 ('formulario-t14/tablas/dic_6_7.tex', 'Las pruebas 6.2.1 a 6.5.1', 'Las pruebas 6.2.1, 6.2.2, 6.3.1, 6.4.1 y 6.5.1'),
 ('formulario-t14/tablas/dic_6_7.tex', 'Las pruebas 6.2.3 a 6.5.2', 'Las pruebas 6.2.3, 6.3.2, 6.4.2 y 6.5.2'),
 ('formulario-t15/contenido.tex', 'parten con el Inicio del contrato', 'parten con el inicio del contrato'),
]
for f, a, b in RANGOS:
    q = os.path.join(RAIZ, f); t = io.open(q, encoding='utf8').read()
    assert t.count(a) == 1, (f, a, t.count(a))
    io.open(q, 'w', encoding='utf8', newline='\n').write(t.replace(a, b))
print('rangos corregidos', len(RANGOS))
