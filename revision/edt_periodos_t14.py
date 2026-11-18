# -*- coding: utf-8 -*-
"""Alinea la columna Período del diccionario del T-14 con la reprogramación (olas e intercambio)."""
import io, os, sys
sys.stdout.reconfigure(encoding='utf-8')
RAIZ = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
D = os.path.join(RAIZ, 'formulario-t14', 'tablas')
BS = chr(92)
CAMBIOS = [
 ('dic_4_1.tex', '4.1.1', 'E1 · H4.', 'E1 · Meses 5 a 7 (ola A); H4.'),
 ('dic_4_1.tex', '4.1.2', 'E1 · H4.', 'E1 · Meses 5 y 6 (ola A); H4.'),
 ('dic_4_1.tex', '4.1.3', 'E1 · Meses 5 a 7; construye', 'E1 · Meses 5 a 7 (ola B); construye'),
 ('dic_4_2.tex', '4.2.1', 'E1 · H4, antes del piloto.', 'E1 · Meses 5 a 7 (ola B); H4, antes del piloto.'),
 ('dic_4_2.tex', '4.2.2', 'E1 · H4, antes del piloto.', 'E1 · Meses 5 a 7 (ola B); H4, antes del piloto.'),
 ('dic_4_3.tex', '4.3.1', 'E1 · H4.', 'E1 · Meses 5 a 7 (ola A); H4.'),
 ('dic_4_3.tex', '4.3.2', 'E1 · Meses 5 a 8; construye', 'E1 · Meses 7 y 8 (ola C, al terminar 4.1.1); construye'),
 ('dic_4_3.tex', '4.3.3', 'E1 · Meses 5 a 8; construye', 'E1 · Meses 7 y 8 (ola C, al terminar 4.3.1); construye'),
 ('dic_4_3.tex', '4.3.4', 'E1 · Meses 5 a 8; H4.', 'E1 · Meses 6 a 8 (ola C, al terminar 4.1.2); H4.'),
 ('dic_4_3.tex', '4.3.5', 'E1 · Meses 5 a 9; construye', 'E1 · Meses 7 y 8 (ola C); construye'),
 ('dic_4_5.tex', '4.5.1', 'E1 · Mes 8; H4.', 'E1 · Meses 7 y 8 (ola C, al terminar 4.2.1); H4.'),
 ('dic_5_3.tex', '5.3.1', 'E2 · Meses 13 a 18 (H10).', 'E2 · Meses 9 a 16: habilitación con la cadena desde el mes 9 y prueba de punta a punta con 4.4.1; antes del H10.'),
 ('dic_5_3.tex', '5.3.2', 'E2 · Certificación antes de cada activación;', 'E2 · Meses 16 a 18; certificación antes de cada activación;'),
]
for f, cod, a, b in CAMBIOS:
    p = os.path.join(D, f); L = io.open(p, encoding='utf8').read().split('\n'); n = 0
    for i, l in enumerate(L):
        if l.strip().startswith(cod + ' &'):
            celdas = l.split(' & ')
            assert celdas[-1].startswith(a), (cod, celdas[-1][:60])
            celdas[-1] = b + celdas[-1][len(a):]
            L[i] = ' & '.join(celdas); n += 1
    assert n == 1, (f, cod, n)
    io.open(p, 'w', encoding='utf8', newline='\n').write('\n'.join(L))
print('períodos actualizados', len(CAMBIOS))
