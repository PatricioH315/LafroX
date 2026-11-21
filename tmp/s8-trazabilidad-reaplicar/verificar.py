"""Verificación estructural acotada de la reaplicación de SD8."""
import ast
import json
from collections import Counter
from pathlib import Path

root = Path('Trazabilidad-Informe2')
scratch = Path('tmp/s8-trazabilidad-reaplicar')
src = (root / 'generar_tablas.py').read_text(encoding='utf-8')
node = next(n for n in ast.parse(src).body if isinstance(n, ast.Assign) and any(isinstance(t, ast.Name) and t.id == 'GRUPOS' for t in n.targets))
groups = eval(compile(ast.Expression(node.value), '<verificacion>', 'eval'), {'C': 'Corregida', 'P': 'Parcial', 'N': 'Pendiente'})
before = json.loads((scratch / 'grupos-antes.json').read_text(encoding='utf-8'))
allowed = {1, 3, 4, 6, 9, 10, 12, 13, 14, 15, 19}
changed = []
assert len(groups) == len(before)
for (title, pref, rows), (oldtitle, oldpref, oldrows) in zip(groups, before):
    assert (title, pref) == (oldtitle, oldpref)
    assert len(rows) == len(oldrows)
    for i, (row, oldrow) in enumerate(zip(rows, oldrows), 1):
        assert tuple(row[:2]) == tuple(oldrow[:2]), (pref, i, 'observacion/estado')
        if tuple(row) != tuple(oldrow):
            assert pref == 'SD8' and i in allowed, (pref, i, 'fuera de alcance')
            changed.append(i)
assert set(changed) == allowed
sd8 = next(rows for _, pref, rows in groups if pref == 'SD8')
assert Counter(row[1] for row in sd8) == {'Corregida': 12, 'Parcial': 7, 'Pendiente': 2}
assert Counter(row[1] for _, _, rows in groups for row in rows) == {'Corregida': 105, 'Parcial': 34, 'Pendiente': 13}
assert 'CT-15' in sd8[5][2]
assert all(value in sd8[9][2] for value in ['1.183,12', '180,00', '821,13', '137,20', '683,93', '1.001,13', '160', '3.072', '202.108,62'])
assert 'dos años' in sd8[14][2] and 'sin fecha calendario' in sd8[14][2]
assert '8.C–8.H' in sd8[18][2] and 'falta confirmar' in sd8[18][2]
old = (scratch / 'narrativa-antes.tex').read_text(encoding='utf-8')
new = (root / 'LAFROX_AnalisisFinanciero_2_Anexos_20261113.tex').read_text(encoding='utf-8')
assert 'En SD9 y SD13 se citan las páginas' in new
assert old.split('Los escenarios y las pautas de revisión')[0] == new.split('Los escenarios y las pautas de revisión')[0]
print('PASS: 152 observaciones; SD8 21 (12C/7P/2N); total 105C/34P/13N; solo 11 respuestas/referencias SD8 modificadas; SD9/SD13 intactos.')
if (root / 'partes/tablas.tex').exists():
    tex = (root / 'partes/tablas.tex').read_text(encoding='utf-8')
    for i in range(1, 22):
        assert tex.count('\\mbox{SD8-%02d}' % i) == 1
    assert '..' not in '\n'.join(line for line in tex.splitlines() if '\\mbox{SD8-' in line)
    assert (root / 'partes/tablas_sintesis.tex').read_bytes() == (scratch / 'sintesis-antes.tex').read_bytes()
    print('PASS: 21 IDs SD8 únicos, sin doble punto; síntesis idéntica byte a byte.')
