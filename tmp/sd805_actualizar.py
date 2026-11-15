from pathlib import Path
from decimal import Decimal as D, ROUND_HALF_UP
from collections import defaultdict
import re, json, xml.etree.ElementTree as ET

root = Path(__file__).resolve().parents[1]
paths = ['08_plan_riesgos/contenido.tex', 'LAFROX-Subdocumento8-Anexos.tex',
         'LAFROX-Formulario-T-16.tex', '08_plan_riesgos/anexo-f-respuestas.tex',
         '08_plan_riesgos/anexo-e-controles.tex', '08_plan_riesgos/anexo-h-reservas.tex']
base = {p: (root/p).read_text(encoding='utf-8') for p in paths}
snapshot = root/'tmp/sd805-base.json'
if snapshot.exists():
    assert json.loads(snapshot.read_text(encoding='utf-8')) == base, 'Aplicación única; el estado previo ya cambió.'
snapshot.write_text(json.dumps(base, ensure_ascii=False, indent=2), encoding='utf-8')
b, a, t, f, e, h = [base[p] for p in paths]

event = ('Dado que el perfil real de carga requiere confirmar su concentración temporal y mezcla de transacciones con Operaciones y TI, '
         'entonces puede que esas características difieran del perfil validado durante la ejecución u operación, '
         'teniendo como consecuencia revalidación de capacidad y recuperación coordinada antes de habilitar el alcance afectado.')
action = ('Mitigar. ARQ solicita el perfil a Operaciones/TI en los primeros cinco días hábiles del mes 1 y lo valida al cierre de ese mes; '
          'revalida antes de H5/H10, preparación del peak y cambios del perfil. SRE asume gestión operativa desde mes 22, familia ARQ. '
          'Ante divergencia, conservar mediciones, ejecutar CT-14, bloquear promoción afectada y elevar recuperación por CT antes del hito. '
          'El peak conocido, crecimiento comprometido y corrección del diseño dentro del alcance siguen a cargo de LafroX.')
evidence = ('Perfil versionado y validado por Operaciones/TI, comparación de carga acordada y observada por ventana y operación, '
            'informe CT-14 y decisión de habilitación del alcance verificado.')
trigger = 'Mediciones de concentración temporal o mezcla de transacciones distintas del perfil validado, o perfil sin confirmar al cierre del mes 1.'
cont = ('ARQ, y SRE desde mes 22, registra divergencia y avisa a JP/CT el mismo día hábil; '
        'presenta recuperación en dos días hábiles y siempre antes del hito. Conservar bloqueo, '
        'corregir y repetir CT-14 en ventana autorizada antes de habilitar. Si la divergencia pertenece '
        'al alcance comprometido, LafroX corrige como trabajo ordinario; no presume ampliación contractual.')

def add_row(s, label, row):
    start = re.search(r'\\begin\{tablalafrox\}[^\n]*\{'+re.escape(label)+r'\}', s).start()
    end = s.index('\\end{tablalafrox}', start)
    assert 'R-036 &' not in s[start:end], label
    return s[:end] + row + ' \\\\\n' + s[end:]

t = add_row(t, 'tab:t16-riesgos', 'R-036 & '+event+' & Operación del cliente & 2 / 0,30 & 4 / 0,40 & 0,12 (Media) & '+action+' & Arquitecto de Solución') if '{tab:t16-riesgos}' in t else t
# Use actual label from the first register table; preserve all existing rows.
if 'R-036 &' not in t:
    first = re.search(r'\{(tab:[^}]+)\}', t[t.index('\\renewcommand{\\thetable}{T-16.1}'):])
    t = add_row(t, first[1], 'R-036 & '+event+' & Operación del cliente & 2 / 0,30 & 4 / 0,40 & 0,12 (Media) & '+action+' & Arquitecto de Solución')
t = add_row(t, 'tab:t16-residual', r'R-036 & 30,00\% & 4 / 0,40 & 0,12 / Media & ARQ (SRE desde mes 22)')

labels = re.findall(r'\{(tab:[^}]+)\}', a)
# Locate by caption instead of assuming historical label names.
def label_after(s, caption):
    return re.search(r'\{(tab:[^}]+)\}', s[s.index(caption):])[1]
a = add_row(a, label_after(a, 'Matriz de respuestas'), 'R-036 & '+trigger+' & '+action+' & Arquitecto de Solución')
a = add_row(a, label_after(a, 'Contrapartes'), 'R-036 / ARQ & Gerente de Operaciones y Jefe de TI; SRE gestiona desde mes 22, familia ARQ. & Entregar y validar perfil por ventana, concentración temporal y mezcla de transacciones, incluyendo peak y crecimiento comprometidos; conservar mediciones y aprobación de cada versión. & Solicitar en los primeros cinco días hábiles del mes 1; validar al cierre del mes 1 y revalidar antes de H5/H10, preparación del peak y cambios del perfil. & '+cont)
a = add_row(a, 'tab:sd8-anexo-b-pert', r'R-036 & 30\% & 1 & 16,00 & 48,00 & 120,00 & 54,67 & 16,40')
a = add_row(a, 'tab:sd8-ampliacion-hipotesis', r'R-036 / 30\% / 1 & Meses 1--56; un episodio acumulado en toda la ventana. & Hipótesis no observada de divergencia de concentración temporal o mezcla respecto del perfil validado; el peak conocido no es incierto. p0=p1=30\%, sin descuento por eficacia futura. & ARQ/CAL: 60/40 de O/M/P=16/48/120 HH acumuladas; PERT=54,67 HH. Sólo coordinación y recuperación extraordinarias. CT-14 y correcciones del alcance son ordinarias; A=0 y C=16 HH contenidas en PERT. & Aclaración 2, 8.2; Caso, caps. 17.5 y 19; perfil por confirmar con Operaciones/TI; CT-14.')
a = add_row(a, label_after(a, 'Fundamento del impacto'), 'R-036 & 54,67 / 2 & 4 / 4 & 0,40 & Aceptación y servicio: la divergencia exige revalidar capacidad antes de habilitar el alcance; puede amenazar aceptación o servicio. Se conserva I=4 aunque el esfuerzo sea nivel 2; no se presupone daño sanitario ni cambio de alcance.')

f = add_row(f, 'tab:cierre-fichas', 'R-036 & '+action+' Evidencia de salida: '+evidence+' & '+cont+' & ARQ / CAL; A: 0,00/0,00; C: 9,60/6,40 HH. SRE asume desde mes 22, familia ARQ. & Ventana de programación 1--56; A=0. Confirmación del perfil y CT-14 en trabajo ordinario. C es parte de H0, no se suma de nuevo; no multiplicar por revisiones ni por meses.')
f = add_row(f, 'tab:cierre-residual', r'R-036 & 30,00\% / 2 / 0,30 & 4 / 0,40; 0,12 (Media) & L=38,67 HH; p1L=11,60 HH. & Sin reducción de p0: '+evidence+' Conservar I=4 y E=0,12; la prueba permite habilitar sólo el alcance verificado. Si falta evidencia o falla CT-14, mantener bloqueo y corregir/repetir; no acreditar eficacia ni alcance ampliado por el solo resultado de carga.')

# Recalculate from current source inputs, not rounded PERT printouts.
qblock = a[a.index('{tab:sd8-anexo-b-pert}'):]
qblock = qblock[:qblock.index('\\end{tablalafrox}')]
q = {l.split(' & ')[0]: l.split(' & ') for l in qblock.splitlines() if l.startswith('R-')}
model = json.loads((root/'tmp/cierre-s8-datos.json').read_text(encoding='utf-8'))['risks']
model['R-036'] = dict(p='30', pr='30', A='0', C='16', owner='ARQ', support='CAL', start=1, end=56)
monthly = defaultdict(lambda: defaultdict(D))
initial = after = residual = response = prevent = D(0)
for rid, x in model.items():
    cells = q[rid]
    p = D(cells[1].replace('\\%', ''))/100
    o, m, pe = [D(v.replace(',', '.')) for v in cells[3:6]]
    hh = (o+4*m+pe)/6
    pr, aa, cc = D(x['pr'])/100, D(x['A']), D(x['C'])
    initial += p*hh; after += pr*hh; residual += pr*(hh-cc); response += pr*cc; prevent += aa
    for month in range(x['start'], x['end']+1):
        for role, share in [(x['owner'],D('.6')),(x['support'],D('.4'))]:
            monthly[month][role] += pr*hh*share/D(x['end']-x['start']+1)
def fmt(x): return str(x.quantize(D('.01'), rounding=ROUND_HALF_UP)).replace('.', ',')
def pretty(x): return format(x.quantize(D('.01'), rounding=ROUND_HALF_UP), ',.2f').replace(',', 'X').replace('.', ',').replace('X', '.')
assert fmt(initial)=='1199,52' and fmt(after)=='837,53'
assert fmt(response)=='142,00' and fmt(residual)=='695,53'
assert sum(sum(v.values()) for v in monthly.values()).quantize(D('.000001')) == after.quantize(D('.000001'))
blockstart = h.index('{tab:cierre-mensual}')
blockend = h.index('\\end{tablalafrox}',blockstart)
oldblock = h[blockstart:blockend]
newblock = re.sub(r'^\d+ &.*$', '', oldblock, flags=re.M).rstrip()+'\n'
roles=['JP','ARQ','DAT','CAL','SRE','IMP','SEG']
newblock += ''.join(' & '.join([str(month)]+[fmt(monthly[month][rr]) for rr in roles]+[fmt(sum(monthly[month].values()))])+' \\\\\n' for month in range(1,57))
h = h[:blockstart]+newblock+h[blockend:]
h += ('\nR-036 añade 16,40 HH a la contingencia específica, distribuidas uniformemente entre meses 1--56: '
      '9,84 HH de familia ARQ y 6,56 HH de CAL en toda la ventana. SRE asume la gestión operativa desde mes 22 '
      'sin crear una segunda imputación ni cambiar la familia ARQ. A=0; C=16 HH forma parte de H0. '
      'El dimensionamiento, las pruebas CT-14 y la corrección del alcance comprometido conservan su presupuesto ordinario.\n')

replacements = {'35 riesgos':'36 riesgos','35 eventos':'36 eventos','35 fichas':'36 fichas',
                'los 35,':'los 36,','las 28 dependencias':'las 29 dependencias','los 28 riesgos':'los 29 riesgos',
                'de 28 riesgos':'de 29 riesgos','1.183,12':pretty(initial),'821,13':fmt(after),
                '683,93':fmt(residual),'137,20':fmt(response),'1.001,13':pretty(prevent+after),'1001,13':fmt(prevent+after),
                '15 medios y 5 bajos':'16 medios y 5 bajos','19 medios y 11 bajos':'20 medios y 11 bajos','58,3\\%':'57,5\\%'}
out=[b,a,t,f,e,h]
for i,s in enumerate(out):
    for old,new in replacements.items(): s=s.replace(old,new)
    out[i]=s
b,a,t,f,e,h=out
# Explicit boundary between technical obligation and uncertain workload profile.
b=b.replace('Son trece riesgos;', 'R-036 añade la divergencia del perfil real de carga respecto del validado. Son catorce riesgos;')
b=b.replace('mientras R-030 trata', 'mientras R-036 trata diferencias por confirmar de concentración temporal y mezcla respecto del perfil validado, R-030 trata')
b=b.replace('Esta justificación no añade riesgos ni modifica sus valoraciones.', 'R-036 se incorpora por esa incertidumbre distinta; las valoraciones de R-001--R-035 se conservan. CT-14 no traslada al CLIENTE fallos de diseño ni el peak conocido.')
b=b.replace('T-16 contiene el registro', 'La matriz 8.D.2 coteja los diez temas de SD8-05 y distingue cobertura documental de eficacia pendiente. T-16 contiene el registro')
t=t.replace('Las condiciones de origen corresponden al Caso 02, capítulos 10 y 19.', 'Las condiciones de origen corresponden al Caso 02, capítulos 10 y 19; R-036 explicita además la incertidumbre del perfil de carga para el análisis de escalabilidad de la Aclaración 2, 8.2. La matriz 8.D.2 presenta la cobertura de SD8-05, con implementación y eficacia pendientes de verificar.')
e=e.replace('Demostrar capacidad efectiva por ventana y dependencia, incluidos ERP, colas y recursos compartidos; ajustar el dimensionamiento ofertado sin degradar requisitos.',
            'Comparar perfil de carga acordado y observado, concentración por ventana y mezcla de operaciones; demostrar capacidad efectiva por dependencia, incluidos ERP, colas y recursos compartidos, peak conocido y crecimiento comprometido. Ajustar el dimensionamiento ofertado sin degradar requisitos.')
e=e.replace('La coordinación comercial del cierre sigue en R-031.', 'Conservar perfil, entradas, resultados y aprobación. Ante prueba fallida, LafroX corrige y repite antes de promover; no presume demanda adicional del CLIENTE. R-036 trata divergencias del perfil; R-031, coordinación del cierre; R-030, interfaces legadas.')
f=f.replace('Para vigilancia ordinaria y aceptación pasiva A=0.', 'Para vigilancia ordinaria, aceptación pasiva y confirmación ordinaria del perfil de R-036, A=0.')

# Add coverage matrix in annex D, before the technical-control annex inputs.
coverage = [
('Conocimiento del planificador / R-014','Caso, cap. 19; retiro y efecto OTIF en T-16.','Transferencia incompleta antes del retiro; recuperar y validar reglas/excepciones.','IMP; CAL verifica.','V-14 y prueba sin planificador en piloto; conservar evidencia del efecto de 6--9 puntos OTIF.'),
('Objeción sindical / R-028','Caso, caps. 10, 16.1 y 19.','Desacuerdo sobre finalidades/controles antes de la ola; acuerdo 5.4.2, sin vigilancia excluida.','JP/IMP; Operaciones, TI y sindicato.','Acta de finalidades, accesos y controles antes de la ola; cobertura pendiente ante desacuerdo.'),
('Conductores externos / R-035','Caso, caps. 10, 15 y 19; RT-22.04.','Rechazo individual pese a acuerdo e incorporación; demostración en andén y conductor certificado/dispuesto.','IMP; Operaciones y transportista.','Uso práctico antes de salida y evidencia de adopción; distinto de firma R-011 y reemplazo R-024.'),
('Rotación nocturna / R-029','Caso, caps. 7.2, 10 y 19.','Altas superan tutoría o llegan sin competencia; inducción y cobertura por turno.','IMP; SRE desde 22; Bodega/Operaciones.','Evaluación previa a autonomía y aprendizaje máximo dos horas; matriz 8.F.2a. El 38\\% no es p0.'),
('Interfaces legadas / R-030','Caso, caps. 5 y 19.','Contrato/extracción no verificables a tiempo; ensayo temprano ERP/WMS sin modificar ERP.','ARQ/DAT; TI; CAL verifica.','Entradas/salidas, tiempos y conciliación contra origen; matriz 8.F.2a. Distinto de calidad de historia.'),
('Enlace de Concepción / R-017','Caso, caps. 6 y 19.','Interrupción antes de validar respaldos o pérdida del último camino; ensayo y restitución.','SRE; TI y operadores de enlace.','Conmutación y recuperación probadas antes de aceptar la ola; respaldo ofertado no equivale a disponible.'),
('Peak y cierre / R-031','Caso, caps. 10, 17.5 y 19.','Condición de cierre incumplida bajo peak/congelamiento; continuidad y recuperación autorizadas.','JP; CAL y Operaciones.','Seis condiciones acumulativas y cuatro semanas finales; matriz 8.F.2a. No duplica capacidad CT-14.'),
('Obsolescencia / R-032','Aclaración 2, 8.2; plataforma declarada.','Cambio excepcional de soporte/compatibilidad que excede mantenimiento ordinario; transición probada.','ARQ; DES/SRE.','Inventario y revisión trimestral de soporte, regresión y reversión; actualización ordinaria excluida de contingencia.'),
('Bloqueo por proveedor / R-033','Aclaración 2, 8.2; servicios gestionados.','Restricción efectiva de exportación o sustitución; probar restauración y transición utilizable.','ARQ/SRE; TI.','Credenciales, exportaciones e infraestructura como código; prueba de restauración. Elegir AWS no acredita bloqueo.'),
('Escalabilidad / R-036 y CT-14','Aclaración 2, 8.2; Caso, caps. 17.5 y 19; perfil por confirmar.','Divergencia de concentración/mezcla frente al perfil validado; confirmar, comparar y repetir CT-14.','ARQ/CAL; Operaciones/TI; SRE desde 22.','Perfil versionado e informe de carga/estrés: ERP, colas, errores, p95 y recuperación; habilitar sólo alcance probado.')]
matrix = r'''
\clearpage
\subsection*{Cobertura de omisiones de SD8-05}
\addcontentsline{toc}{subsection}{Cobertura de omisiones de SD8-05}
La Tabla 8.D.2 coteja la primera revisión del Informe 2, apartado 8 y prioridades
de corrección, con el Caso 02 y la Aclaración 2, 8.2. Los IDs son los vigentes:
las menciones históricas de la revisión no sustituyen la numeración actual.
La cobertura documental se completa en S8 con diez temas trazados; no acredita
implementación ni eficacia. Las referencias a S4/S9/S13 siguen sujetas a su
integración y verificación en las ramas correspondientes.

\begingroup
\renewcommand{\thetable}{8.D.2}
\begin{landscape}
\setlength{\textwidth}{\linewidth}
\renewcommand{\arraystretch}{1.08}
\begin{tablalafrox}{Cobertura documental de SD8-05 y evidencia pendiente. Fuente: Caso 02, Aclaración 2 y primera revisión del Informe 2.}{tab:sd805-cobertura}{F{0.15} F{0.16} F{0.24} F{0.14} Y}{\cab{Tema / referencia vigente} & \cab{Fuente de la condición} & \cab{Evento y respuesta} & \cab{Responsable} & \cab{Evidencia y estado}}
'''
matrix += ''.join(' & '.join(row[:-1]+(row[-1]+' Estado: cobertura documentada; eficacia pendiente.',))+' \\\\\n' for row in coverage)
matrix += r'''\end{tablalafrox}
\end{landscape}
\endgroup

\paragraph{Decisión ante el perfil de carga}
Si el perfil es conforme, CAL verifica CT-14 y la autoridad competente habilita
sólo el alcance probado; R-036 conserva su hipótesis de exposición en la ventana.
Si existe variación pendiente de confirmar, ARQ conserva perfil y mediciones,
solicita validación a Operaciones/TI, aplica la respuesta de R-036 y mantiene
la promoción afectada pendiente hasta revalidar capacidad.
Si hay saturación dentro de la carga comprometida, LafroX registra un problema,
corrige el diseño y repite CT-14 con cargo al trabajo ordinario. La concentración
o mezcla no detalladas no convierten por sí solas esa carga en ampliación de
alcance: JP contrasta requisitos y acuerdos antes de cualquier decisión contractual.
Una misma causa recibe un único ID principal; R-030 atiende la interfaz,
R-031 la coordinación del cierre y R-036 la divergencia del perfil, vinculando
efectos sin duplicar HH. El peak conocido y el crecimiento contratado permanecen
en el dimensionamiento obligatorio de CT-14.

'''
a = a.replace('\\input{08_plan_riesgos/anexo-e-controles.tex}',matrix+'\\input{08_plan_riesgos/anexo-e-controles.tex}')
for path,s in zip(paths,[b,a,t,f,e,h]): (root/path).write_text(s,encoding='utf-8')

# Editable RBS source: add one node in the existing two-column client branch.
src=root/'08_plan_riesgos/figuras/LafroX_RBS_35_riesgos_S8_v3.drawio'
tree=ET.parse(src); graph=tree.find('.//root')
for c in graph.findall('mxCell'):
    if c.get('id')=='root': c.set('value',c.get('value').replace('35 riesgos','36 riesgos').replace('15 medios','16 medios'))
    if c.get('id')=='b3': c.set('value',c.get('value').replace('13 riesgos','14 riesgos'))
node=ET.SubElement(graph,'mxCell',id='n3.14',parent='1',vertex='1',
    style='html=1;whiteSpace=wrap;align=left;spacingLeft=25;spacingRight=18;verticalAlign=middle;rounded=1;arcSize=8;fillColor=#f5f5f5;strokeColor=#666666;strokeWidth=3;fontColor=#000000;fontSize=45;',
    value='<b>3.14</b>  Perfil real de carga difiere del validado<br><font style="font-size:40px">R-036 · Media</font>')
ET.SubElement(node,'mxGeometry',height='254',width='440',x='1720',y='2373',attrib={'as':'geometry'})
edge=ET.SubElement(graph,'mxCell',id='e-r036',parent='1',edge='1',source='b3',target='n3.14',style='edgeStyle=orthogonalEdgeStyle;endArrow=none;strokeColor=#666666;strokeWidth=3;')
ET.SubElement(edge,'mxGeometry',relative='1',attrib={'as':'geometry'})
target=root/'08_plan_riesgos/figuras/LafroX_RBS_36_riesgos_S8_v4.drawio'
tree.write(target,encoding='utf-8',xml_declaration=True)
p=root/'08_plan_riesgos/figuras/rbs.tex'
p.write_text(p.read_text(encoding='utf-8').replace('LafroX_RBS_35_riesgos_S8_v3.pdf','LafroX_RBS_36_riesgos_S8_v4.pdf'),encoding='utf-8')
print('R-036 integrado. Totales:',pretty(initial),fmt(after),fmt(response),fmt(residual),pretty(prevent+after))
