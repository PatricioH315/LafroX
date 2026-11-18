# -*- coding: utf-8 -*-
"""Controles del T-14 reestructurado contra la versión de HEAD."""
import io, json, re, subprocess, sys, os
sys.stdout.reconfigure(encoding='utf-8')
RAIZ = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
MAPA = json.load(io.open(os.path.join(RAIZ, 'revision', 'edt_equivalencias_20261117.json'), encoding='utf8'))
NUEVOS = set(MAPA.values())
CUENTAS_N = {'.'.join(v.split('.')[:2]) for v in NUEVOS}
nuevo = io.open(os.path.join(RAIZ, 'formulario-t14', 'contenido.tex'), encoding='utf8').read()
viejo = subprocess.run(['git', 'show', 'HEAD:formulario-t14/contenido.tex'], cwd=RAIZ, capture_output=True).stdout.decode('utf8')

def prosa(t):
    # quita la lista de la EDT y las líneas de comandos de tabla/figura
    t = re.sub(r'\\begin\{itemize\}.*?\\end\{itemize\}', ' ', t, flags=re.S)
    return t

# 1. códigos de 3-4 niveles fuera de secciones de otros documentos que no existen en el esquema nuevo
print('== 1. Códigos que no existen en el esquema nuevo')
P = prosa(nuevo)
malos = []
for m in re.finditer(r'(?<![\d.])(\d{1,2}\.\d{1,2}\.\d{1,2}(?:\.\d{1,2})?)(?![\d]|\.\d)', P):
    c = m.group(1)
    if c not in NUEVOS and c not in CUENTAS_N:
        ctx = P[max(0, m.start() - 50):m.end() + 15].replace('\n', ' ')
        malos.append((c, ctx))
for c, ctx in malos:
    print(' ', c, '|', ctx)
print('  total', len(malos))

# 2. compromisos con cifras: tokens numéricos del diccionario vigente (prosa) que ya no aparecen
print('== 2. Cifras de los textos vigentes que no aparecen en el texto nuevo')
vi = viejo[viejo.index('\\section{Diccionario de la EDT}'):viejo.index('\\section{Carta Gantt}')]
vi = re.sub(r'\\parte\{[^}]*\}', '', vi)
tok = re.compile(r'\d+(?:[.,]\d+)*\s*(?:%|\\%|h|horas|minutos|días|meses|años|HH|personas|×\d+|x\d+)?|\d{1,2}:\d{2}')
faltan = []
for m in tok.finditer(vi):
    s = m.group(0).strip()
    if re.fullmatch(r'\d{1,2}\.\d{1,2}(\.\d{1,2}){0,2}', s):
        continue  # códigos
    if len(re.sub(r'\D', '', s)) < 2 and not re.search(r'[%:hH]', s):
        continue
    if s not in nuevo:
        ctx = vi[max(0, m.start() - 60):m.end() + 30].replace('\n', ' ')
        faltan.append((s, ctx))
vistos = set()
for s, ctx in faltan:
    if s in vistos:
        continue
    vistos.add(s)
    print(' ', repr(s), '|', ctx)
print('  total', len(vistos))

# 3. palabras prohibidas en la prosa nueva
print('== 3. Palabras prohibidas')
proh = r'(pendiente|por resolver|estructura anterior|versi[oó]n anterior|se reorganiz|reestructur|CODEX|Texto vigente|no acredita|no se presume|no demuestra|no garantiza|como exige|conforme a lo solicitado|§|\.md\b|\.py\b|\.json\b|\.csv\b|fase 8|fases 1 a 4)'
for i, l in enumerate(nuevo.splitlines(), 1):
    if l.lstrip().startswith(r'\item'):
        continue
    for m in re.finditer(proh, l, re.I):
        print('  línea', i, '|', l[max(0, m.start() - 60):m.end() + 40])

# 4. cuentas de 2 niveles mencionadas en prosa que no existen
print('== 4. «cuenta X.Y» inexistentes')
for m in re.finditer(r'[Cc]uentas?\s+((?:\d{1,2}\.\d{1,2}(?:,\s*|\s+y\s+|\s+a\s+)?)+)', P):
    for c in re.findall(r'\d{1,2}\.\d{1,2}', m.group(1)):
        if c not in CUENTAS_N:
            print('  ', c, '|', P[max(0, m.start() - 40):m.end() + 20].replace('\n', ' '))
