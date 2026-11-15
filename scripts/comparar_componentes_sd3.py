"""Clasifica diferencias textuales; no certifica cobertura funcional ni pruebas."""
import csv
import re
from pathlib import Path

root = Path(__file__).resolve().parents[1]
with (root / 'trazabilidad/auditoria_pendientes_sd3.csv').open(encoding='utf-8-sig', newline='') as stream:
    rows = list(csv.DictReader(stream))

def normal(s):
    return re.sub(r'\s+', ' ', s.replace(r'\_', '_')).strip().rstrip('.')

def reduced(s):
    # Las versiones y tecnologías suprimidas se revisan separadamente en SD4/T-11.
    return re.sub(r'^(M\d+\s+[^;(]+)\s*\([^)]*\)', r'\1', normal(s), count=1)

out = []
for row in rows:
    if row['componente_coincide_t13'] != 'False':
        continue
    left, right = normal(row['componente']), normal(row['componente_t13'])
    if left == right:
        result = 'Solo puntuación o escape'
    elif reduced(left) == reduced(right):
        result = 'Mismo texto tras retirar la descripción inicial de tecnología; verificar dicha descripción en SD4/T-11'
    else:
        result = 'Diferencia de contenido o estructura: requiere cotejo individual'
    out.append({'id': row['id'], 'clasificacion': result,
                'componente_t12': row['componente'], 'componente_t13': row['componente_t13'],
                'huella_t12': row['huella_fila_t12'], 'version_sd9': row['version_sd9']})

path = root / 'trazabilidad/diferencias_componentes_t12_t13.csv'
with path.open('w', encoding='utf-8-sig', newline='') as stream:
    writer = csv.DictWriter(stream, fieldnames=list(out[0]))
    writer.writeheader()
    writer.writerows(out)
from collections import Counter
print(len(out), dict(Counter(item['clasificacion'] for item in out)))
