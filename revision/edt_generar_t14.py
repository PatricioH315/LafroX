# -*- coding: utf-8 -*-
"""Genera el T-14 con la EDT por productos a partir del T-14 vigente.

- Diccionario: una tabla por cuenta nueva (formulario-t14/tablas/dic_N_M.tex), filas
  copiadas del T-14 vigente con los códigos traducidos y la etapa al inicio de «Período».
- contenido.tex: reemplaza las secciones «Estructura de descomposición del trabajo» y
  «Diccionario de la EDT»; deja comentarios «% CODEX:» donde hay que redactar.
- Traduce los códigos del resto del archivo (carta Gantt y criterios).
Uso: python revision/edt_generar_t14.py  (desde la raíz del repo)
"""
import glob, io, json, os, re, sys
sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__))))
import edt_recodificar as R

RAIZ = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
T14 = os.path.join(RAIZ, 'formulario-t14')
BS = chr(92)

# ---- estructura nueva (misma que la propuesta) ----
EDT = json.load(io.open(os.path.join(RAIZ, 'revision', 'edt_estructura_20261117.json'), encoding='utf8'))

# ---- filas vigentes del diccionario ----
filas = {}
fuente_tabla = {}
for f in sorted(glob.glob(os.path.join(T14, 'tablas', 'tab_T14_*.tex'))):
    n = int(re.search(r'tab_T14_(\d+)', f).group(1))
    if not 3 <= n <= 51:
        continue
    txt = io.open(f, encoding='utf8').read()
    cap = re.search(r'Diccionario de la cuenta [\d.]+\. Fuente: (.*?)\}\{tab:', txt, re.S)
    for l in txt.splitlines():
        m = re.match(r'\s*(\d+(?:\.\d+){2,3})\s*&', l)
        if not m:
            continue
        cuerpo = l.strip()
        assert cuerpo.endswith(BS * 2), l
        celdas = [c.strip() for c in cuerpo[:-2].split(' & ')]
        assert len(celdas) == 6, (len(celdas), l[:80])
        filas[m.group(1)] = celdas
        fuente_tabla[m.group(1)] = cap.group(1).strip() if cap else ''
assert len(filas) == 227, len(filas)

# ---- etapa como atributo ----
AMBAS = {'1.1.1', '1.1.2', '1.1.3', '1.2.3', '1.7.1', '1.7.2', '7.1.2', '7.1.3', '7.1.4', '7.1.5', '7.1.6',
         '7.2.1', '7.2.4', '7.2.5', '9.1.2', '5.4.4'}
E1 = {'1.2.1', '1.2.2', '1.2.4', '7.1.1', '7.2.3', '7.3.1', '4.1.4', '4.2.1', '4.2.2', '4.2.3'}
E2 = {'1.2.5', '2.1.4', '2.4.2', '4.1.3', '4.3.1', '4.3.2', '4.3.3', '4.3.4', '7.2.2', '7.3.2', '5.4.3', '9.1.1', '3.6.5', '3.6.6'}
def etapa(v):
    if v in AMBAS: return 'Ambas'
    if v in E1: return 'E1'
    if v in E2: return 'E2'
    if v.startswith(('8.', '9.2.')): return 'Operación'
    if v.startswith(('1.3.', '1.4.', '1.5.', '1.6.', '1.8.', '1.9.', '2.2.', '3.11.')): return 'Ambas'
    if v.startswith(('3.5.', '3.9.', '3.10.4.')): return 'E2'
    return 'E1'

rep = []
def tr(s):
    return R.traducir(s, rep)

# ---- tablas del diccionario por cuenta nueva ----
os.makedirs(os.path.join(T14, 'tablas'), exist_ok=True)
vistos = set()
for n1, t1, cuentas in EDT:
    for i, (t2, paqs) in enumerate(cuentas, 1):
        cod2 = '%s.%d' % (n1, i)
        fuentes = []
        for v in paqs:
            if fuente_tabla[v] not in fuentes:
                fuentes.append(fuente_tabla[v])
        L = []
        L.append(BS + 'begin{tablalafrox}{Diccionario de la cuenta %s. Fuente: %s}{tab:T14-dic-%s-%d}' % (cod2, '; '.join(fuentes), n1, i))
        L.append('  {L{1.2cm} Y Y Y C{0.9cm} L{2.3cm}}')
        L.append('  {' + BS + 'cab{Código} & ' + BS + 'cab{Paquete de trabajo} & ' + BS + 'cab{Entregable} & ' + BS + 'cab{Criterio de aceptación} & ' + BS + 'cab{Resp.} & ' + BS + 'cab{Período}}')
        for j, v in enumerate(paqs, 1):
            c = filas[v]
            nuevo = '%s.%d' % (cod2, j)
            assert R.MAPA[v] == nuevo, (v, nuevo)
            vistos.add(v)
            per = tr(c[5])
            L.append('  %s & %s & %s & %s & %s & %s %s' % (nuevo, tr(c[1]), tr(c[2]), tr(c[3]), c[4], etapa(v) + ' · ' + per, BS * 2))
        L.append(BS + 'end{tablalafrox}')
        io.open(os.path.join(T14, 'tablas', 'dic_%s_%d.tex' % (n1, i)), 'w', encoding='utf8', newline='\n').write('\n'.join(L) + '\n')
assert vistos == set(filas), set(filas) - vistos

# ---- tabla de productos (reemplaza tab_T14_1) ----
L = [BS + 'begin{tablalafrox}{Productos de la EDT, cuentas de control y paquetes de trabajo. Fuente: (Bases Administrativas, arts. 17.2–17.6 y Formulario T-14, p. 63); (Bases Técnicas Transversales, secciones 17.2–17.6, pp. 32–34).}{tab:T14-1}',
     '  {L{0.8cm} Y C{2.2cm} C{2.2cm}}',
     '  {' + BS + 'cab{N.º} & ' + BS + 'cab{Producto} & ' + BS + 'cab{Cuentas de control} & ' + BS + 'cab{Paquetes de trabajo}}']
tc = tp = 0
for n1, t1, cuentas in EDT:
    np_ = sum(len(p) for _, p in cuentas)
    tc += len(cuentas); tp += np_
    L.append('  %s & %s & %d & %d %s' % (n1, t1, len(cuentas), np_, BS * 2))
L.append('  & ' + BS + 'textbf{Total} & ' + BS + 'textbf{%d} & ' % tc + BS + 'textbf{%d} %s' % (tp, BS * 2))
L.append(BS + 'end{tablalafrox}')
io.open(os.path.join(T14, 'tablas', 'tab_T14_1.tex'), 'w', encoding='utf8', newline='\n').write('\n'.join(L) + '\n')

# ---- contenido.tex ----
cont_path = os.path.join(T14, 'contenido.tex')
cont = io.open(cont_path, encoding='utf8').read().replace('\r\n', '\n')
ini = cont.index(BS + 'section{Estructura de descomposición del trabajo}')
fin = cont.index(BS + 'section{Carta Gantt}')
viejo = cont[ini:fin]

# intros de las cuentas vigentes
intros = {}
for m in re.finditer(r'\\subsubsection\{Cuenta (\d+\.\d+) — [^}]*\}\n(.*?)\\parte\{tablas/tab_T14_\d+\}', viejo, re.S):
    txt = re.sub(r'La Tabla \\ref\{[^}]*\} presenta sus paquetes\.\s*', '', m.group(2)).strip()
    intros[m.group(1)] = tr(txt)
# párrafos generales del diccionario
dic_ini = viejo.index(BS + 'section{Diccionario de la EDT}')
dic_intro = viejo[dic_ini:viejo.index(BS + 'subsection{Fase 1. Inicio}')]
fig_ini = viejo.index('La Figura ' + BS + 'ref{fig:T14-edt-completa}')
fig_bloque = viejo[fig_ini:dic_ini]

def comentario(t):
    return '\n'.join('% ' + l if l.strip() else '%' for l in t.strip().splitlines())

S = []
S.append(BS + 'section{Estructura de descomposición del trabajo}\n')
S.append('% CODEX: párrafo de apertura de la EDT por productos (100 % del alcance, 10 productos, 60 cuentas, 227 paquetes; criterio de agrupación; etapa como atributo; fases RUP como ciclo de ejecución y no como estructura). Texto vigente como referencia:')
ap = viejo[viejo.index('La EDT descompone'):viejo.index(BS + 'begin{itemize}', viejo.index('La EDT descompone'))]
S.append(comentario(tr(ap)))
S.append('')
S.append(BS + 'parte{tablas/tab_T14_1}\n')
S.append('% CODEX: párrafo breve que lea la Tabla tab:T14-1 (qué productos concentran el trabajo) y presente la lista siguiente, con la raíz «Plataforma logística de Distribuidora Puelche» y sus diez productos en el primer nivel.\n')
S.append(BS + 'begin{itemize}')
for n1, t1, cuentas in EDT:
    S.append(BS + 'item ' + BS + 'textbf{%s. %s}\n' % (n1, t1))
    for i, (t2, paqs) in enumerate(cuentas, 1):
        S.append(BS + 'item %s.%d %s\n' % (n1, i, t2))
        for j, v in enumerate(paqs, 1):
            S.append(BS + 'item %s.%d.%d %s\n' % (n1, i, j, tr(filas[v][1])))
S.append(BS + 'end{itemize}')
S.append('% CODEX: revisar el párrafo de la figura de la EDT completa: la figura se rehace después con la estructura por productos; no mencionar «estructura anterior».')
S.append(tr(fig_bloque).strip() + '\n')
S.append('% CODEX: revisar la introducción del diccionario (los paquetes de esfuerzo continuo ya no son «de la fase 8», sino los de operación y los recurrentes de gestión; explicar que la columna Período empieza con la etapa que el paquete habilita: E1, E2, Ambas u Operación).')
S.append(tr(dic_intro).strip() + '\n')
for n1, t1, cuentas in EDT:
    np_ = sum(len(p) for _, p in cuentas)
    S.append(BS + 'subsection{Producto %s. %s}\n' % (n1, t1))
    S.append('% CODEX: una o dos frases sobre qué acepta la Contraparte en este producto y qué hitos produce.')
    S.append('El producto %s reúne %d cuentas de control y %d paquetes de trabajo.\n' % (n1, len(cuentas), np_))
    for i, (t2, paqs) in enumerate(cuentas, 1):
        S.append(BS + 'subsubsection{Cuenta %s.%d — %s}\n' % (n1, i, t2))
        origen = sorted({'.'.join(v.split('.')[:2]) for v in paqs}, key=lambda s: [int(x) for x in s.split('.')])
        S.append('% CODEX: párrafo de la cuenta (qué producto reúne y por qué; si junta incrementos de E1 y E2, decirlo). Paquetes vigentes: ' + ', '.join('%s→%s' % (v, R.MAPA[v]) for v in paqs))
        for o in origen:
            if o in intros:
                S.append('% Texto vigente de la cuenta ' + o + ':')
                S.append(comentario(intros[o]))
        S.append('')
        S.append('La Tabla ' + BS + 'ref{tab:T14-dic-%s-%d} presenta sus paquetes.\n' % (n1, i))
        S.append(BS + 'parte{tablas/dic_%s_%d}\n' % (n1, i))
nuevo = '\n'.join(S) + '\n'
resto = cont[fin:]
resto_tr = tr(resto)
cabeza = cont[:ini]
# quitar el párrafo «Estructura de alcance por productos» si quedó en la cabeza (está dentro del bloque reemplazado)
salida = cabeza + nuevo + resto_tr
io.open(cont_path, 'w', encoding='utf8', newline='\n').write(salida)

# tablas viejas del diccionario
for n in range(3, 52):
    p = os.path.join(T14, 'tablas', 'tab_T14_%d.tex' % n)
    if os.path.exists(p):
        os.remove(p)

from collections import Counter
print(Counter(r[0] for r in rep))
for r in rep:
    if r[0] in ('desconocido', 'protegido', 'cuenta-dividida'):
        print(r)
