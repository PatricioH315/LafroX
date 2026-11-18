# -*- coding: utf-8 -*-
"""Corrige rangos de paquetes partidos tras la traducción en SD7, anexos y T-18."""
import io, os, sys
sys.stdout.reconfigure(encoding='utf-8')
RAIZ = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
CAMBIOS = [  # archivo, texto, reemplazo, ocurrencias esperadas (None = todas, al menos una)
 ('subdocumento-07-anexos/tablas/tab_7B1.tex', 'D-23 & 6.2.1 a 6.5.1 y 6.6.1 &', 'D-23 & 6.2.1, 6.2.2, 6.3.1, 6.4.1, 6.5.1 y 6.6.1 &', 1),
 ('subdocumento-07-anexos/tablas/tab_7B1.tex', 'D-31c & 6.2.3 a 6.5.2 y 6.6.2 &', 'D-31c & 6.2.3, 6.3.2, 6.4.2, 6.5.2 y 6.6.2 &', 1),
 ('subdocumento-07-anexos/tablas/tab_7B1.tex', '& 5.2.2 a 5.3.2 Integraciones', '& 5.2.2 a 5.2.4, 5.3.1 y 5.3.2 Integraciones', 1),
 ('subdocumento-07-anexos/tablas/tab_7E1.tex', '2.7.1, 2.7.2, 2.7.3 y 6.1.1 a 6.5.1 &', '2.7.1, 2.7.2, 2.7.3 y 6.1 a 6.5, incremento E1 &', 1),
 ('subdocumento-07-anexos/tablas/tab_7E1.tex', '& 6.1.1 a 6.5.1 &', '& 6.1 a 6.5, incremento E1 &', None),
 ('subdocumento-07-anexos/tablas/tab_7E1.tex', '& 6.1.2 a 6.5.2 &', '& 6.1 a 6.5, incremento E2 &', 1),
 ('subdocumento-07-anexos/tablas/tab_7E1.tex', '& 3.8 y 3.9 &', '& 6.1 a 6.5, ambos incrementos &', 1),
 ('formulario-t18/contenido.tex', '(paquetes 4.1.1 a 4.5.1 del Formulario T-14', '(paquetes 4.1.1 a 4.3.5 y 4.5.1 del Formulario T-14', 1),
 ('formulario-t18/contenido.tex', 'Corresponde a los paquetes 4.4.1 a 4.5.2, 5.3.1 y 5.3.2', 'Corresponde a los paquetes 4.4.1 a 4.4.3, 4.5.2, 5.3.1 y 5.3.2', 1),
 ('formulario-t18/contenido.tex', '(paquetes 6.1.2 a 6.6.2)', '(paquetes 6.1.2, 6.2.3, 6.3.2, 6.4.2, 6.5.2, 6.6.2 y 6.7.2)', 1),
]
for f, a, b, n in CAMBIOS:
    p = os.path.join(RAIZ, f); t = io.open(p, encoding='utf8').read()
    c = t.count(a)
    assert (c >= 1) if n is None else (c == n), (f, a, c)
    io.open(p, 'w', encoding='utf8', newline='\n').write(t.replace(a, b))
    print('%-45s %d × %s' % (os.path.basename(f), c, a[:50]))
