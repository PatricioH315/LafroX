"""Genera las tablas LaTeX de la estimación por tamaño del T-15 (09-11-2026)."""
import json, re
from pathlib import Path
ROOT = Path(__file__).resolve().parents[1]
T = ROOT / 'formulario-t15/tablas'
BS2 = chr(92) * 2
g = {'__file__': str(ROOT / 'revision/estimacion_modulos_20261109.py'), '__name__': 'lib'}
exec((ROOT / 'revision/estimacion_modulos_20261109.py').read_text(encoding='utf-8'), g)
R = g['estimate'](); RATE = g['RATE']
conc = json.loads((ROOT / 'revision/estimacion_20261109.json').read_text(encoding='utf-8'))

def es(x, d=2):
    t = f'{x:,.{d}f}'.replace(',', 'X').replace('.', ',').replace('X', '.')
    return t[:-3] if t.endswith(',00') else t
def row(*c): return '  ' + ' & '.join(map(str, c)) + ' ' + BS2

# 1. Tamaño y esfuerzo por módulo
L = [r'\begin{anexohorizontal}\setlength{\textwidth}{\linewidth}',
     r'\begin{tablalafrox}{Tamaño y esfuerzo de los módulos (HH). Fuente: requisitos del Formulario T-12 por paquete EDT y tasas de esta sección.}{tab:T15-tamano}',
     r'  {L{1.1cm} C{0.9cm} C{1.2cm} C{1.0cm} C{1.3cm} R{0.95cm} R{1.05cm} R{0.95cm} R{0.95cm} R{0.95cm} R{1.05cm} R{1.05cm} R{1.1cm} R{1.4cm}}',
     r'  {\cab{Paquete} & \cab{Req. T-12} & \cab{Flujos S/M/C} & \cab{Interf. y disp.} & \cab{Sin conexión / rend. / otras} & \cab{Diseño} & \cab{Constr.} & \cab{Pruebas} & \cab{Integr. QA} & \cab{Iterac.} & \cab{O} & \cab{M} & \cab{P} & \cab{E}}']
for r in R:
    n = r['nf']
    L.append(row(r['code'], r['nreq'], f"{n['S']}/{n['M']}/{n['C']}", n['I'] + n['D'],
                 f"{n['OFF']}/{n['REN']}/{n['ESP']}", r['diseno'], r['constr'], r['pruebas'], r['integ'],
                 r['iterac'], es(r['O']), es(r['M']), es(r['P']), es(r['E'])))
tot = {k: sum(r[k] for r in R) for k in ('O', 'M', 'P', 'E')}
L.append(r'  \midrule')
L.append(row(r'\textbf{Total}', '', '', '', '', '', '', '', '', '', es(tot['O']), es(tot['M']), es(tot['P']), r'\textbf{' + es(tot['E']) + '}'))
L += [r'\end{tablalafrox}', r'\end{anexohorizontal}']
(T / 'tab_T15_tamano.tex').write_text('\n'.join(L) + '\n', encoding='utf-8')

# 2. Motivos de O y P
L = [r'\begin{tablalafrox}{Fundamento del optimista y del pesimista de cada módulo. Fuente: elaboración propia a partir de la ficha de cada módulo.}{tab:T15-tamano-motivos}',
     r'  {L{1.4cm} C{1.0cm} Y C{1.0cm} Y}',
     r'  {\cab{Paquete} & \cab{O/M} & \cab{Qué permite el optimista} & \cab{P/M} & \cab{Qué incluye el pesimista}}']
for r in R:
    L.append(row(r['code'], es(r['O'] / r['M']), r['omot'][0].upper() + r['omot'][1:], es(r['P'] / r['M']), r['pmot'][0].upper() + r['pmot'][1:]))
L.append(r'\end{tablalafrox}')
(T / 'tab_T15_tamano_motivos.tex').write_text('\n'.join(L) + '\n', encoding='utf-8')

# 3. Detalle de elementos por módulo
TIPO = {'S': 'Flujo S', 'M': 'Flujo M', 'C': 'Flujo C', 'I': 'Interfaz', 'D': 'Dispositivo',
        'OFF': 'Sin conexión', 'REN': 'Rendimiento', 'ESP': 'Necesidad especial'}
L = [r'\begin{tablalafrox}{Elementos de alcance de cada módulo. Fuente: Formulario T-12, columna Paquete EDT; tasas M de esta sección.}{tab:T15-tamano-detalle}',
     r'  {L{1.3cm} Y L{3.2cm} L{2.0cm} R{1.0cm}}',
     r'  {\cab{Paquete} & \cab{Elemento de alcance} & \cab{Requisitos T-12} & \cab{Tipo} & \cab{M (HH)}}']
for r in R:
    for k, (t, d, ids) in enumerate(r['els']):
        L.append(row(r['code'] + ' ' + r['name'].split(' ', 1)[0] if k == 0 else '', d, ids, TIPO[t], RATE[t]))
    L.append(r'  \midrule')
L[-1] = L[-1]
L.append(r'\end{tablalafrox}')
(T / 'tab_T15_tamano_detalle.tex').write_text('\n'.join(L) + '\n', encoding='utf-8')

# 4. Rangos por tipo
L = [r'\begin{tablalafrox}{Rangos del PERT por tipo de paquete. Fuente: elaboración propia; clases de la Tabla de supuestos.}{tab:T15-pert-tipo}',
     r'  {L{1.2cm} C{1.0cm} C{1.0cm} Y}',
     r'  {\cab{Clase} & \cab{O/M} & \cab{P/M} & \cab{Fundamento del rango}}',
     row('G', '0,90', '1,10', 'Acta o informe con formato y contenido fijados en el T-14; varía el número de rondas de revisión.'),
     row('E', '0,80', '1,20', 'Diseño o configuración que depende de decisiones del CLIENTE y de la arquitectura aprobada.'),
     row('I', '0,80', '1,20', 'Interfaz o migración con contraparte conocida y documentada; los casos sin documentación tienen rango propio.'),
     row('V', '0,85', '1,15', 'Casos y ciclos fijados en el plan de pruebas; una repetición adicional usa la reserva protegida de 3.072 HH.'),
     row('T', '0,85', '1,15', 'Cantidades del T-11 y sesiones del plan de capacitación; varía el acceso a los sitios.'),
     row('R', '0,90', '1,10', 'Frecuencia fijada por contrato; varía la duración de cada ocurrencia.'),
     row('A y C', '1,00', '1,00', 'Cobertura por puestos y calendario; no se reduce por un escenario optimista.'),
     row('D', '—', '—', 'Módulos: rango propio de cada uno (Tabla de fundamentos de O y P).'),
     r'\end{tablalafrox}']
(T / 'tab_T15_pert_tipo.tex').write_text('\n'.join(L) + '\n', encoding='utf-8')

# 5. Paquetes con riesgo identificado
RISK = [('3.3.2', '0,85', '1,60', 'Interfaces del ERP sin documentación (Caso, sección 17.5): el pesimista incluye un segundo ciclo de análisis con muestras y de pruebas.'),
        ('3.6.5', '0,85', '1,60', 'Negociación y certificación con la principal cadena, que el caso advierte que no es de dos semanas.'),
        ('3.6.6', '0,85', '1,50', 'Perfiles de mensajes distintos en cada cadena restante.'),
        ('3.7.1', '0,90', '1,50', 'Calidad de datos desconocida: el 41 \\% de las recepciones del retiro de marzo no tenía lote registrado.'),
        ('3.7.2 a 3.7.4', '0,90', '1,40', 'Repetición de cargas y conciliación sobre datos ya perfilados.'),
        ('2.4.3', '0,90', '1,50', 'Banco de frío: homologación de sensores y repetición de ensayos de excursión.'),
        ('4.1.4', '0,90', '1,50', 'Piloto de frío en cuatro camiones con cobertura variable en ruta.')]
L = [r'\begin{tablalafrox}{Paquetes con rango propio por riesgo identificado. Fuente: elaboración propia a partir del caso y del T-14.}{tab:T15-pert-riesgo}',
     r'  {L{1.8cm} C{1.0cm} C{1.0cm} Y}',
     r'  {\cab{Paquete} & \cab{O/M} & \cab{P/M} & \cab{Fundamento}}'] + [row(*x) for x in RISK] + [r'\end{tablalafrox}']
(T / 'tab_T15_pert_riesgo.tex').write_text('\n'.join(L) + '\n', encoding='utf-8')

# 6. Conciliación
order = sorted(conc['delta'], key=lambda s: [int(x) for x in s.split('.')])
L = [r'\begin{tablalafrox}{Conciliación de las HH que cambian. Fuente: Tabla de horas por paquete anterior y vigente.}{tab:T15-conciliacion}',
     r'  {L{1.6cm} R{1.8cm} R{1.8cm} R{1.8cm} Y}',
     r'  {\cab{Paquete} & \cab{HH anteriores} & \cab{HH vigentes} & \cab{Diferencia} & \cab{Explicación}}']
for k in order:
    old, new, d, _ = conc['delta'][k]
    why = 'Estimación por tamaño' if k.startswith(('3.4.', '3.5.')) else 'Rango por riesgo identificado'
    L.append(row(k, es(old), es(new), es(d), why))
L.append(r'  \midrule')
L.append(row(r'\textbf{Total}', es(sum(conc['delta'][k][0] for k in order)), es(sum(conc['delta'][k][1] for k in order)),
             r'\textbf{' + es(conc['delta_total']) + '}', 'La línea base pasa de 220.023 a ' + es(220023 + conc['delta_total']) + ' HH'))
L.append(r'\end{tablalafrox}')
(T / 'tab_T15_conciliacion.tex').write_text('\n'.join(L) + '\n', encoding='utf-8')
print('ok', es(tot['E']), es(220023 + conc['delta_total']))
