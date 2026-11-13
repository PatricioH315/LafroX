"""Cifras de B+ en los textos y tablas del SD7 (13-11-2026). Complementa aplicar_bplus_20261113.py.

Cada reemplazo indica cuántas veces debe aparecer el texto anterior; si no coincide, se detiene
antes de escribir.
"""
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]

R = {
    'formulario-t15/contenido.tex': [
        ('219.727,83', '199.219,03', 8),
        ('207.191,83 HH de los 227 paquetes para formar las 207.319,83 HH',
         '186.683,03 HH de los 227 paquetes para formar las 186.811,03 HH', 1),
        ('199.219,03 HH: 207.191,83 de los 227 paquetes', '199.219,03 HH: 186.683,03 de los 227 paquetes', 1),
        ('separa 160.047 HH de los 59 paquetes continuos', 'separa 139.538,20 HH de los 59 paquetes continuos', 1),
        ('juntos reproducen las 207.191,83 HH', 'juntos reproducen las 186.683,03 HH', 1),
        ('muestra los 24 paquetes cuyas HH cambian. La línea base pasa de 220.023 a 199.219,03 HH.',
         'muestra los 26 paquetes cuyas HH cambian. La línea base pasa de 220.023 a 199.219,03 HH.', 1),
    ],
    'formulario-t15/tablas/tab_T15_7.tex': [('219.727,83', '199.219,03', 1)],
    'formulario-t15/tablas/tab_T15_asignacion_partidas.tex': [
        ('218.403,03 HH de los perfiles y 1.324,80 HH de servicios especializados, para un total de 219.727,83 HH',
         '197.894,23 HH de los perfiles y 1.324,80 HH de servicios especializados, para un total de 199.219,03 HH', 1),
        ('& SRE & 21–56 & 26.280 & 30 (26.280) \\\\', '& SRE & 21–56 & 21.764,2 & 30 (21.748,2), 22 (16) \\\\', 1),
        ('& SRE & 21–56 & 54.239 & 17 (54.239) \\\\', '& SRE & 21–56 & 38.246 & 17 (38.246) \\\\', 1),
    ],
    'formulario-t15/tablas/tab_T15_perfiles_internos.tex': [
        ('Analista / Diseñador Senior & 1 & 1.352 & 169 & 2.640 & 330 \\\\',
         'Analista / Diseñador Senior & 1 & 1.352 & 169 & 2.656 & 332 \\\\', 1),
        ('Operador de Mesa N1 & TIC & 16 & 5.664 & 708 & 54.239 & 6.779,875 \\\\',
         'Operador de Mesa N1 & TIC & 16 & 5.664 & 708 & 38.246 & 4.780,75 \\\\', 1),
        ('Operador NOC & TIC & 6 & 3.672 & 459 & 26.280 & 3.285 \\\\',
         'Operador NOC & TIC & 6 & 3.672 & 459 & 21.748,2 & 2.718,525 \\\\', 1),
        ('\\textbf{128.354,20} & \\textbf{16.044,275}', '\\textbf{107.845,40} & \\textbf{13.480,675}', 1),
        ('90.048,83 HH de implementación y 128.354,20 HH de operación',
         '90.048,83 HH de implementación y 107.845,40 HH de operación', 1),
        ('HH_{oper.}&=128.354,20+460,80=128.815,', 'HH_{oper.}&=107.845,40+460,80=108.306,20,', 1),
        ('HH_{proyecto}&=90.912,83+128.815=219.727,83.', 'HH_{proyecto}&=90.912,83+108.306,20=199.219,03.', 1),
        ('(90.809,86 y 128.917,97 HH en el resumen por etapa), con el mismo total de 219.727,83 HH',
         '(90.809,86 y 108.409,17 HH en el resumen por etapa), con el mismo total de 199.219,03 HH', 1),
        ('11.364,10 de implementación y 16.101,875 de operación: 27.465,98 en total',
         '11.364,10 de implementación y 13.538,275 de operación: 24.902,38 en total', 1),
    ],
    'formulario-t15/tablas/tab_T15_conciliacion.tex': [
        ('  \\midrule\n  \\textbf{Total} & 19.360 & 19.064,83 & \\textbf{-295,17} & La línea base pasa de 220.023 a 219.727,83 HH \\\\',
         '  8.1.1 & 26.280 & 21.764,20 & -4.515,80 & Dotación de operación del SD4, Anexo 4-W.7 \\\\\n'
         '  8.1.2 & 54.239 & 38.246 & -15.993 & Dotación de operación del SD4, Anexo 4-W.7 \\\\\n'
         '  \\midrule\n  \\textbf{Total} & 99.879 & 79.075,03 & \\textbf{-20.803,97} & La línea base pasa de 220.023 a 199.219,03 HH \\\\', 1),
    ],
    'subdocumento-07/contenido.tex': [
        ('219.727,83', '199.219,03', 3),
        ('(207.319,83 HH de paquetes y restauraciones previas a Operación',
         '(186.811,03 HH de paquetes y restauraciones previas a Operación', 1),
    ],
    'subdocumento-07/tablas/tab_SD7_13.tex': [
        ('Operación & 21 a 56  & 128.917,97 & 0 & 128.917,97', 'Operación & 21 a 56  & 108.409,17 & 0 & 108.409,17', 1),
        ('\\textbf{216.655,83} & \\textbf{3.072} & \\textbf{219.727,83}',
         '\\textbf{196.147,03} & \\textbf{3.072} & \\textbf{199.219,03}', 1),
    ],
}

texts = {}
for f, reps in R.items():
    p = ROOT / f
    s = p.read_text(encoding='utf-8')
    for old, new, n in reps:
        c = s.count(old)
        assert c == n, (f, old[:70], c, n)
        s = s.replace(old, new)
    texts[p] = s
for p, s in texts.items():
    p.write_text(s, encoding='utf-8')
    print('ok', p.relative_to(ROOT))
