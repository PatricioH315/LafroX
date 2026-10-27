"""Verificación reproducible del frente B. No cambia fechas ni HH de las fuentes.

K4 se captura una sola vez; K6 se regenera con el estado de las fuentes.
El calendario es el supuesto del CPM, no una certificación legal del calendario.
"""
from pathlib import Path
from datetime import date, timedelta
from decimal import Decimal
from collections import defaultdict
import csv, hashlib, json, math, re, subprocess

ROOT = Path(__file__).resolve().parents[2]
OUT = Path(__file__).resolve().parent
FOLDERS = ['subdocumento-07', 'subdocumento-07-anexos', 'formulario-t14', 'formulario-t15', 'formulario-t18']

def read(p):
    return (ROOT / p).read_text(encoding='utf-8-sig')

def rows(p):
    return [l.strip().removesuffix('\\\\').strip().split(' & ')
            for l in read(p).splitlines() if re.match(r'^\s*\d+(?:\.\d+)*\s*&', l)]

def sha(p):
    return hashlib.sha256((ROOT / p).read_bytes()).hexdigest()

def csv_write(name, headers, data):
    with (OUT / name).open('w', encoding='utf-8-sig', newline='') as f:
        w = csv.writer(f); w.writerow(headers); w.writerows(data)

def git(*args):
    return subprocess.check_output(['git', *args], cwd=ROOT).decode('utf-8').strip()

eff = {r[0]: r for r in rows('formulario-t15/tablas/tab_T15_2.tex')}
dates = {r[0]: r for r in rows('formulario-t15/tablas/tab_T15_paquetes.tex')}
names = {}
for p in (ROOT / 'formulario-t14/tablas').glob('*.tex'):
    for r in rows(p):
        if re.fullmatch(r'\d+(?:\.\d+){2,3}', r[0]) and len(r) == 6:
            names[r[0]] = (r, str(p.relative_to(ROOT)).replace('\\', '/'))
assert len(eff) == len(names) == 227 and eff.keys() == names.keys()
assert len(dates) == 168
assert sum(Decimal(r[7]) for r in eff.values()) == Decimal('207487')
source_paths = ['formulario-t15/tablas/tab_T15_2.tex', 'formulario-t15/tablas/tab_T15_paquetes.tex',
                'formulario-t15/tablas/tab_T15_4.tex', 'formulario-t15/tablas/tab_T15_4_personas.tex']
manifest = {p: sha(p) for p in source_paths}
if not (OUT / 'K4_PAQUETES.csv').exists():
    data = []
    for code, r in eff.items():
        d = dates.get(code)
        n, source = names[code]
        data.append([code, n[1], r[1], r[2], r[3], r[7], 'HH', n[2], n[3], n[5],
                     d[4] if d else '', d[5] if d else '', d[3] if d else '', d[2] if d else '',
                     d[6] if d else '', 'Reserva 3072 HH separada; no imputada otra vez al paquete', source])
    csv_write('K4_PAQUETES.csv', ['EDT','nombre','clase','rol','meses','esfuerzo','unidad','entregable',
              'criterio','periodo_hito','inicio','fin','HH_fecha','personas_promedio_maximo','predecesoras','reserva','fuente_T14'], data)
    (OUT / 'K4_MANIFIESTO.json').write_text(json.dumps({'head':git('rev-parse','HEAD'), 'fuentes':manifest,
        'paquetes':227,'entregables':168,'continuos':59,'hh_paquetes':207487,
        'componentes':{'restauraciones':128,'soporte_puente':9336,'reserva_protegida':3072},
        'hh_total':220023}, ensure_ascii=False, indent=2), encoding='utf-8')

hours = rows('formulario-t15/tablas/tab_T15_4.tex')
people = rows('formulario-t15/tablas/tab_T15_4_personas.tex')
assert len(hours) == len(people) == 56
assert all(sum(map(Decimal, r[1:8])) == Decimal(r[8]) for r in hours)
assert sum(Decimal(r[8]) for r in hours) == Decimal('220023')
assert all(sum(map(int, r[1:9])) == int(r[9]) for r in people)
periods = [('E1 desarrollo',1,12),('E1 marcha blanca',13,15),('E2 desarrollo',13,18),
           ('E2 marcha blanca',19,20),('E1 producción y estabilización',16,20),
           ('Operación',21,56),('E2 cierre y estabilización',21,22)]
peaks = []
for title, a, b in periods:
    subset = [r for r in people if a <= int(r[0]) <= b]
    peak = max(int(r[9]) for r in subset)
    peaks.append([title,a,b,peak,','.join(r[0] for r in subset if int(r[9]) == peak)])
csv_write('K6_PEAKS_PERIODOS.csv',['etapa','mes_desde','mes_hasta','peak_conjunto_periodo','meses_peak'],peaks)

# Concurrencia de ventanas es una cota superior, no asignación diaria demostrada.
# HH / (6.4 * días) es demanda media mínima, no el máximo real ni nivelación.
script = ROOT / 'revision/recalcular_cpm_20261025.py'
ns = {'__file__': str(script)}
exec(compile(script.read_text(encoding='utf-8').split('OUT.mkdir(')[0], str(script), 'exec'), ns)
cal, ix = ns['CAL'], ns['ix']
def dt(s): return date(*map(int, s.split('-')[::-1]))
load = defaultdict(lambda: [0.0, 0.0, []])
for code, r in dates.items():
    active = [d for d in cal if dt(r[4]) <= d <= dt(r[5])]
    assert active
    peak = float(r[2].split('/')[-1].strip().replace(',','.'))
    avg_min = float(r[3]) / (6.4 * len(active))
    assert avg_min <= peak + 1e-8, (code, avg_min, peak)
    for d in active:
        item = load[d,r[1]]; item[0] += avg_min; item[1] += peak; item[2].append(code)
capacities = {'DES':48, 'SRE':44, 'CAL':10, 'ARQ+DAT':15, 'SEG':7}
capacity_data = []
for role, cap in capacities.items():
    vals = []
    for d in cal:
        rs = ['ARQ','DAT'] if role == 'ARQ+DAT' else [role]
        entries = [load[d,r] for r in rs if (d,r) in load]
        if entries:
            vals.append((sum(v[0] for v in entries),sum(v[1] for v in entries),d,
                         sorted(set(c for v in entries for c in v[2]))))
    peak_min = max(vals, key=lambda x:x[0]); peak_upper = max(vals, key=lambda x:x[1])
    capacity_data.append([role,cap,round(peak_min[0],3),peak_min[2].isoformat(),
                          peak_upper[1],peak_upper[2].isoformat(),';'.join(peak_upper[3])])
csv_write('K6_CAPACIDAD.csv',['familia','dotacion_declarada','max_demanda_media_ventanas','fecha_media',
          'cota_suma_maximos_ventanas','fecha_cota','paquetes_en_fecha_cota'],capacity_data)

# Condición necesaria de capacidad por intervalo: cada paquete tiene HH y un
# máximo diario. Lo que no cabe fuera del intervalo tiene que ejecutarse dentro.
# Es una cota inferior aun permitiendo preempción, sin servicios continuos.
intervals = []
for role, cap in {**capacities, 'DES_escenario_40':40}.items():
    rs = ['ARQ','DAT'] if role == 'ARQ+DAT' else ['DES'] if role.startswith('DES_') else [role]
    tasks=[]
    for code,r in dates.items():
        if r[1] not in rs: continue
        a,b=ix(dt(r[4])),ix(dt(r[5])+timedelta(days=1))
        tasks.append((code,a,b,float(r[3]),float(r[2].split('/')[-1].replace(',','.'))*6.4))
    starts=sorted({t[1] for t in tasks}); ends=sorted({t[2] for t in tasks})
    worst=None
    for a in starts:
        for b in ends:
            if b<=a: continue
            mandatory=[]
            for code,ta,tb,hh,daily in tasks:
                overlap=max(0,min(b,tb)-max(a,ta))
                required=max(0,hh-daily*((tb-ta)-overlap))
                if required>1e-7: mandatory.append((code,required))
            required=sum(v for _,v in mandatory); available=(b-a)*cap*6.4
            excess=required-available
            if worst is None or excess>worst[0]:worst=(excess,a,b,required,available,mandatory)
    excess,a,b,required,available,mandatory=worst
    intervals.append([role,cap,cal[a].isoformat(),cal[b-1].isoformat(),round(required,3),
                      round(available,3),round(excess,3),';'.join(c for c,_ in mandatory)])
csv_write('K6_INTERVALOS_CAPACIDAD.csv',['familia','capacidad_personas','desde','hasta',
          'HH_minimas_dentro','HH_capacidad','exceso_HH','paquetes'],intervals)

closures = []
for stage, end, production, acceptance in [('E1',date(2028,4,30),date(2028,5,5),date(2028,5,29)),
                                         ('E2',date(2028,9,30),date(2028,10,5),date(2028,10,25))]:
    submission = next(d for d in cal if d > end)
    review = [d for d in cal if d > submission][:10]
    closures.append({'etapa':stage,'evidencia_desde':(end+timedelta(days=1)-timedelta(days=28)).isoformat(),
      'evidencia_hasta':end.isoformat(),'entrega_completa_escenario':submission.isoformat(),
      'revision_desde':review[0].isoformat(),'revision_hasta':review[-1].isoformat(),
      'produccion_objetivo':production.isoformat(),'aceptacion_objetivo':acceptance.isoformat(),
      'dias_revision_antes_produccion':sum(submission<d<production for d in cal),
      'compatible_diez_dias_antes_produccion':review[-1]<production,
      'supuesto':'entrega en primer hábil posterior a evidencia; revisión desde siguiente hábil; sin subsanación'})

# Inventario de tablas activas: grafo real de inclusiones, sin eliminar archivos.
active = set()
def include(p):
    p = Path(p)
    if p in active: return
    active.add(p)
    text = read(p)
    for child in re.findall(r'\\parte\{([^}]+)\}',text):
        include(Path(p.parts[0]) / (child + '.tex'))
for folder in FOLDERS: include(Path(folder)/'contenido.tex')
all_tables = {p.relative_to(ROOT) for folder in FOLDERS for p in (ROOT/folder/'tablas').glob('*.tex')}
orphans = sorted(str(p).replace('\\','/') for p in all_tables-active)
table_inventory=[]
for p in sorted(all_tables):
    t=read(p); lab=re.search(r'\}\{([^{}]+)\}\s*\n',t)
    table_inventory.append([str(p).replace('\\','/'), 'activa' if p in active else 'sin inclusión',
      bool('Fuente:' in t), lab.group(1) if lab else 'revisar encabezado'])
csv_write('K6_TABLAS.csv',['archivo','estado','fuente_declarada','etiqueta'],table_inventory)

# Las referencias entre documentos se inventarían por separado: un \ref local
# no puede validar un label que vive en otro PDF.
refs=[]
for p in sorted(active):
    for lineno,line in enumerate(read(p).splitlines(),1):
        if any(x in line for x in ['Subdocumento 3','Subdocumento 4','Subdocumento 6','Subdocumento 9','Formulario T-13','Formulario T-17']):
            refs.append([str(p).replace('\\','/'),lineno,line.strip()])
csv_write('K6_REFERENCIAS_EXTERNAS.csv',['origen','linea','texto'],refs)
baseline=json.loads((OUT/'K4_MANIFIESTO.json').read_text(encoding='utf-8'))
assert all(sha(p)==baseline['fuentes'][p] for p in source_paths), 'Se alteró una fuente de fechas/HH/curvas de K4'
assert not [p for p in ns['detail'] if p['inicio']!=p['inicio_publicado'] or p['fin']!=p['fin_publicado']], 'CPM difiere de la tabla publicada'
out={'head':git('rev-parse','HEAD'),'fuentes':manifest,'paquetes':227,'entregables':168,'continuos':59,
     'hh_total':220023,'peak_mensual':max(int(r[9]) for r in people),'peaks_periodos':peaks,
     'capacidad':capacity_data,'intervalos_capacidad':intervals,'cierres':closures,'hitos':ns['results'],
     'paquetes_cpm_distintos_publicados':[p for p in ns['detail'] if p['inicio']!=p['inicio_publicado'] or p['fin']!=p['fin_publicado']],
     'tablas_sin_inclusion':orphans,'tablas_activas':len(all_tables & active),
     'calendario':'supuesto interno heredado, sujeto a confirmación del CLIENTE',
     'estado':'reconciliación local; cierre integral condicionado a K1/K3/K5 y resolución de las actas de cierre'}
(OUT/'K6_VERIFICACION.json').write_text(json.dumps(out,ensure_ascii=False,indent=2),encoding='utf-8')
print(json.dumps({k:out[k] for k in ['paquetes','entregables','continuos','hh_total','peak_mensual','capacidad','cierres','tablas_sin_inclusion']},ensure_ascii=False,indent=2))
