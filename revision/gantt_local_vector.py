"""Genera los editables y las láminas vectoriales de la red validada del SD7."""
from pathlib import Path
from datetime import date,timedelta
from collections import defaultdict
from html import escape
import argparse
import hashlib,json,re,subprocess,sys,xml.etree.ElementTree as ET
from edt_cpm_20261117 import endpoints, rank, topological, workdays
from reportlab.pdfgen import canvas
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont
from reportlab.lib.styles import ParagraphStyle
from reportlab.lib.colors import HexColor,Color,white
from reportlab.platypus import Paragraph

ROOT=Path(__file__).resolve().parents[1]
SRC=ROOT/'imagenes/Diagramas que faltaban'
OUT=SRC/'Revision-local'
W,H=624,344
PX,PW=334,284
FONT=10
pdfmetrics.registerFont(TTFont('ArialLocal','C:/Windows/Fonts/arial.ttf'))
pdfmetrics.registerFont(TTFont('ArialLocalBold','C:/Windows/Fonts/arialbd.ttf'))
STYLE=ParagraphStyle('fila',fontName='ArialLocal',fontSize=10,leading=11.7,textColor=HexColor('#253746'))
TYPES={'1':'CC','2':'FC','3':'FF','4':'CF'}
T15_DURATION_ID = 'tpc2'
T15_DURATION_NAME = 'Días hábiles T-15'

def guard():
    branch=subprocess.check_output(['git','branch','--show-current'],cwd=ROOT,text=True).strip()
    assert branch=='LafroX-Subdoc7-LateX-CORRIGIENDO',branch

def add_month(d,n):
    m=d.year*12+d.month-1+n
    return date(m//12,m%12+1,1)

def read(name):
    root=ET.parse(name).getroot()
    holidays={date(int(d.get('year')),int(d.get('month')),int(d.get('date')))
              for d in root.findall('./calendars/date') if d.get('type')=='HOLIDAY'}
    working_exceptions = {date(int(d.get('year')), int(d.get('month')), int(d.get('date')))
                          for d in root.findall('./calendars/date') if d.get('type') == 'WORKING_DAY'}
    def finish(a,n):
        if not n:return a
        d=a; left=n
        while True:
            if d in working_exceptions or d.weekday() < 5 and d not in holidays:
                left-=1
                if left==0:return d
            d+=timedelta(days=1)
    tasks=[];edges=[]
    for i,t in enumerate(root.findall('.//task')):
        a=date.fromisoformat(t.get('start'));n=int(t.get('duration'))
        t15_duration = t.find(f"customproperty[@taskproperty-id='{T15_DURATION_ID}']")
        tasks.append({'id':t.get('id'),'name':t.get('name'),'start':a,'end':finish(a,n),
                      'duration':int(t15_duration.get('value')) if t15_duration is not None else n,
                      'duration_gantt':n,'color':t.get('color','#4472c4'),'milestone':t.get('meeting')=='true',
                      'order':i,'attributes':dict(t.attrib)})
        edges += [{'source':t.get('id'),'target':e.get('id'),'type':e.get('type'),
                   'difference':e.get('difference','0'),'hardness':e.get('hardness','')} for e in t.findall('depend')]
    return tasks,edges

def label(c,x,y,text,bold=False,size=10):
    c.setFont('ArialLocalBold' if bold else 'ArialLocal',size);c.setFillColor(HexColor('#253746'));c.drawString(x,y,text)

def heading(c,title,subtitle):
    label(c,5,H-16,title,True,11)
    label(c,5,H-32,subtitle,size=9.5)
    c.setStrokeColor(HexColor('#de6b20'));c.setLineWidth(1.2);c.line(5,H-40,W-5,H-40)

def footer(c):
    label(c,5,16,'Rojo: tareas con holgura cero y puertas críticas de la carta.',size=9.5)
    label(c,5,3,'Barras: fechas fuente. Conectores fuera de lámina: consultar relaciones por ID.',size=9.5)

def paginate(tasks):
    pages=[];page=[];height=0
    for t in tasks:
        p=Paragraph(escape(t['name']),STYLE);_,h=p.wrap(200,1000)
        row={**t,'paragraph':p,'height':max(24,h+8)}
        if page and height+row['height']>232:pages.append(page);page=[];height=0
        page.append(row);height+=row['height']
    if page:pages.append(page)
    return pages

def arrow(c,x,y,direction=1):
    p=c.beginPath();p.moveTo(x,y);p.lineTo(x-direction*3,y+2);p.lineTo(x-direction*3,y-2);p.close();c.drawPath(p,fill=1,stroke=0)

def chart(path,title,rows,edges,a,b,index,total):
    c=canvas.Canvas(str(path),pagesize=(W,H));c.setTitle(title)
    heading(c,title,f'Lámina {index} de {total} · meses calendario · continuidad de filas y vínculos por ID')
    ytop=H-77
    label(c,5,ytop+7,'ID',True,9.5);label(c,27,ytop+7,'Frente y responsable' if title.startswith('Frentes') else 'Paquete o hito',True,9.5)
    label(c,242,ytop+7,'Inicio',True,9.5);label(c,286,ytop+7,'Fin',True,9.5)
    bottom=ytop-sum(t['height'] for t in rows)
    span=(b-a).days
    def x(d):return PX+max(0,min(1,(d-a).days/span))*PW
    months = (b.year - a.year) * 12 + b.month - a.month
    label_step = max(1, (months + 21) // 22)
    month_index = 0
    m=a
    while m<b:
        nxt=add_month(m,1);lo=x(m);hi=x(nxt)
        if m.month%2==0:
            c.setFillColor(HexColor('#f2f5f7'));c.rect(lo,bottom,max(.1,hi-lo),ytop-bottom,fill=1,stroke=0)
        c.setStrokeColor(HexColor('#d5dde3'));c.setLineWidth(.35);c.line(lo,bottom,lo,ytop+2)
        if month_index % label_step == 0:
            c.setFont('ArialLocal',9.5);c.setFillColor(HexColor('#253746'));c.drawCentredString((lo+hi)/2,ytop+7,f'{m.month:02}')
        month_index += 1
        m=nxt
    label(c,PX,ytop+21,f'Período: {a.strftime("%m/%Y")} a {(b-timedelta(days=1)).strftime("%m/%Y")}',True,9.5)
    positions={};y=ytop
    for t in rows:
        h=t['height'];cy=y-h/2;positions[t['id']]=(x(t['start']),x(t['end']+timedelta(days=1)),cy)
        label(c,5,y-14,t['id'],size=9.5)
        t['paragraph'].drawOn(c,27,y-h+4)
        label(c,237,cy-3,t['start'].strftime('%d/%m/%y'),size=9.5)
        label(c,283,cy-3,t['end'].strftime('%d/%m/%y'),size=9.5)
        c.setStrokeColor(HexColor('#d5dde3'));c.setLineWidth(.35);c.line(5,y-h,W-5,y-h)
        y-=h
    # Flechas completas cuando los dos extremos están visibles; el listado conserva todas.
    for e in edges:
        if e['source'] not in positions or e['target'] not in positions:continue
        s=positions[e['source']];t=positions[e['target']]
        if not (a<=next(r for r in rows if r['id']==e['source'])['start']<b):continue
        sx=s[0] if e['type'] in ['1','4'] else s[1]
        tx=t[1] if e['type'] in ['3','4'] else t[0]
        c.setStrokeColor(HexColor('#7b8995'));c.setFillColor(HexColor('#7b8995'));c.setLineWidth(.55)
        bend=min(W-5,max(PX,sx+4));p=c.beginPath();p.moveTo(sx,s[2]);p.lineTo(bend,s[2]);p.lineTo(bend,t[2]);p.lineTo(tx,t[2]);c.drawPath(p)
        arrow(c,tx,t[2],1 if tx>=bend else -1)
    for t in rows:
        if t['end']<a or t['start']>=b:continue
        sx,ex,cy=positions[t['id']];c.setFillColor(HexColor(t['color']));c.setStrokeColor(HexColor(t['color']))
        if t['milestone']:
            xx=x(t['start']);p=c.beginPath();p.moveTo(xx,cy+4);p.lineTo(xx+4,cy);p.lineTo(xx,cy-4);p.lineTo(xx-4,cy);p.close();c.drawPath(p,fill=1,stroke=0)
        else:
            c.roundRect(sx,cy-3,max(1,ex-sx),6,1,fill=1,stroke=0)
            if t['start']<a:arrow(c,PX,cy,-1)
            if t['end']>=b:arrow(c,W-6,cy,1)
    if title.startswith('Frentes'):
        label(c,5,16,'F1–F8 identifican los frentes de trabajo y sus responsables.',size=9.5)
        label(c,5,3,'Las barras con flecha derecha continúan después del mes 21.',size=9.5)
    else:footer(c)
    c.save()

def relation_pages(stem,title,edges,start_index):
    chunks=[edges[i:i+40] for i in range(0,len(edges),40)]
    for k,chunk in enumerate(chunks):
        path=OUT/f'{stem}-{start_index+k}.pdf';c=canvas.Canvas(str(path),pagesize=(W,H))
        heading(c,title,'Dependencias · ID de origen → ID de destino; tipo y desfase')
        label(c,5,H-57,'CC: comienzo-comienzo; FC: fin-comienzo; FF: fin-fin; CF: comienzo-fin.',size=9.5)
        for i,e in enumerate(chunk):
            col=i//20;row=i%20
            text=f'{e["source"]} → {e["target"]}   {TYPES[e["type"]]}   desfase {e["difference"]}'
            label(c,12+col*310,H-78-row*12,text,size=10)
        label(c,5,15,'Los ID permiten seguir los vínculos. Desfases en días del calendario del editable.',size=9.5)
        c.save()
    return len(chunks)

def make(stem,title,tasks,edges,windows=None):
    a=min(t['start'] for t in tasks).replace(day=1)
    end=max(t['end'] for t in tasks);b=add_month(end.replace(day=1),1)
    if windows is None:windows=[(a,b)]
    windows_rows=[(lo,hi,paginate([t for t in tasks if t['end']>=lo and t['start']<hi])) for lo,hi in windows]
    total=sum(len(pages) for _,_,pages in windows_rows)
    index=1
    for lo,hi,pages in windows_rows:
        for page in pages:
            chart(OUT/f'{stem}-{index}.pdf',title,page,edges,lo,hi,index,total);index+=1
    n=relation_pages(stem,title,edges,index)
    return total+n

MACRO=r'''
% Continuaciones de una misma figura: conserva números, etiquetas y lista de figuras.
\newcounter{laminaGanttLocal}
\newcommand{\figuraGanttLocal}[4]{%
  \begingroup
  \setcounter{laminaGanttLocal}{1}%
  \loop
    \clearpage
    \begin{anexohorizontal}
      \centering
      \includegraphics[width=\linewidth]{#1-\arabic{laminaGanttLocal}.pdf}\par
      \captionsetup{hypcap=false}
      \ifnum\value{laminaGanttLocal}=1
        \captionof{figure}{#3}\label{#4}%
      \else
        \captionof*{figure}{Figura \ref{#4} (continuación \arabic{laminaGanttLocal} de #2). #3}%
      \fi
    \end{anexohorizontal}
    \stepcounter{laminaGanttLocal}%
  \ifnum\value{laminaGanttLocal}<\numexpr#2+1\relax
  \repeat
  \endgroup\clearpage}
'''

def integrate(manifest):
    for folder in ['formulario-t14', 'formulario-t15']:
        p=ROOT/folder/'contenido.tex';text=p.read_text(encoding='utf-8')
        if '\\newcommand{\\figuraGanttLocal}' not in text:
            pos=text.index('\\newcommand{\\figuraDiagramaHorizontal}')
            text=text[:pos]+MACRO+'\n'+text[pos:]
        # Sustituir sólo las llamadas existentes; conservar títulos y etiquetas.
        for old,item in manifest.items():
            if old not in text and item['stem'] not in text:continue
            pattern=r'\\figuraDiagramaHorizontal\[[^\]]*\]\{'+re.escape(old)+r'\}'
            text,count=re.subn(pattern,lambda m:'\\figuraGanttLocal{imagenes/Diagramas que faltaban/Revision-local/'+item['stem']+'}{'+str(item['pages'])+'}',text)
            if not count and item['stem'] not in text:raise RuntimeError('Llamada no encontrada '+old)
            if not count:
                pattern=r'(\\figuraGanttLocal\{imagenes/Diagramas que faltaban/Revision-local/'+re.escape(item['stem'])+r'\})\{\d+\}'
                text=re.sub(pattern,lambda m:m[1]+'{'+str(item['pages'])+'}',text)
        p.write_text(text,encoding='utf-8')


ACTIVE = ('Fig_7_Gantt_Resumen_Dependencias.gan', 'Fig_7_Gantt_56_Meses.gan',
          'Fig_7_Gantt_Vista_Critica.gan')
HISTORICAL = ('Fig_7_Gantt_Red_Independiente_25_Filas.gan', 'Fig_7_Gantt_Red_Independiente_80_Filas.gan')
XML_TYPE = {name: code for code, name in TYPES.items()}


def generate_views(model, target):
    tasks = {key: {**row, 'start': date.fromisoformat(row['start']), 'finish': date.fromisoformat(row['finish'])}
             for key, row in model['tareas'].items()}
    holidays = {date.fromisoformat(value) for value in model['feriados']}
    links = [dict(item) for item in model['relaciones']]
    for link in links:
        a, b = endpoints(link, tasks)
        origin, target_day = tasks[a[0]][a[1]], tasks[b[0]][b[1]]
        if target_day < origin or rank(target_day) - rank(origin) < link['lag']:
            raise ValueError(f'Precedencia incompatible: {link}')
    # GanttProject relaciona filas completas. Un evento dentro de una barra
    # necesita un marcador de cierre separado para conservar la red acíclica.
    markers = {}
    for edge in links:
        key = edge['target']
        if edge['kind'] != 'CF':
            continue
        if key not in markers:
            marker = markers[key] = 'FIN:' + key
            row = tasks[key]
            tasks[marker] = {**row, 'name': f'{key} · Cierre del paquete',
                             'start': row['finish'], 'milestone': True, 'kind': 'event'}
        edge['target'] = markers[key]
        edge['kind'] = 'CC'
    for key, marker in markers.items():
        for edge in links:
            if edge['source'] == key and edge['kind'] in ('FC', 'FF'):
                edge['source'] = marker
                edge['kind'] = 'CC' if edge['kind'] == 'FC' else 'CF'
        links.append(dict(source=key, target=marker, kind='FC', lag=0, reason='Fin de la barra de seguimiento'))
    keys = sorted(tasks, key=lambda key: (tasks[key]['start'], tasks[key]['kind'] != 'package', key))
    ids = {key: str(i + 1) for i, key in enumerate(keys)}
    # GanttProject admite un vínculo por par de tareas. Cuando se controlan
    # ambos extremos, se conserva CC y se hace pasar FF por un hito de cierre.
    by_pair = defaultdict(list)
    for edge in links:
        by_pair[edge['source'], edge['target']].append(edge)
    export_markers = {}
    for (source, target_key), pair in by_pair.items():
        if len(pair) == 1:
            continue
        if len(pair) != 2 or {edge['kind'] for edge in pair} != {'CC', 'FF'}:
            raise ValueError(f'Vínculos simultáneos sin representación: {source} → {target_key}')
        marker = 'FIN:EXPORT:' + source
        if marker not in tasks:
            row = tasks[source]
            tasks[marker] = {**row, 'name': f'{source} · Fin de referencia para la precedencia',
                             'start': row['finish'], 'milestone': True, 'kind': 'event'}
            ids[marker] = str(len(ids) + 1)
            links.append(dict(source=source, target=marker, kind='FC', lag=0,
                              reason='Fin del predecesor para conservar el vínculo FF'))
        ff = next(edge for edge in pair if edge['kind'] == 'FF')
        ff.update(source=marker, kind='CF')
        export_markers[source, target_key] = marker
    keys = sorted(tasks, key=lambda key: (tasks[key]['start'], tasks[key]['kind'] != 'package', key))
    relations = [(e['source'], e['target'], e['lag']) for e in links]
    topological(tasks, relations)
    critical = {key for key, row in model['detalle'].items() if row['holgura'] == 0}
    critical |= {f'ACT:{h}' for h in ('H6', 'H11')} | {'CUT:H7', 'CUT:H12'}
    windows = {'H7', 'H12'}
    # Las vistas comparten calendario para conservar las fechas civiles de la
    # red. La duración contractual se guarda aparte de la duración del motor.
    working_exceptions = {row[side] for row in tasks.values() for side in ('start', 'finish')
                          if row[side].weekday() >= 5 or row[side] in holidays}

    def work_before(day):
        return rank(day - timedelta(days=1)) + 1 + sum(extra < day for extra in working_exceptions)

    def overview(key, row):
        return (row['kind'] == 'phase' or key in ('6.8.6', '9.4.3')
                or key.startswith('ACT:') or key.rsplit(':', 1)[-1] in windows and row['kind'] == 'event')

    def write_view(filename, title, selected):
        selected = selected | {marker for (a, b), marker in export_markers.items() if a in selected and b in selected}
        project = ET.parse(SRC / ACTIVE[0]).getroot()
        project.set('name', title)
        desc = project.find('description')
        desc.text = ('Red SD7 generada desde T-14, T-15 y Anexo 7.B. El calendario es nominal. '
                     'Las esperas de la carta nivelada se conservan en los desfases publicados. '
                     'Duración usa el calendario del motor, con excepciones para representar fechas civiles. '
                     'Días hábiles T-15 conserva la duración nominal de la fuente. Los ID coinciden entre vistas.')
        view = project.find("./view[@id='gantt-chart']")
        for field in list(view.findall('field')):
            if field.get('id') in ('tpd6', T15_DURATION_ID):
                view.remove(field)
        ET.SubElement(view, 'field', id='tpd6', name='Duration', width='90', order='3')
        ET.SubElement(view, 'field', id=T15_DURATION_ID, name=T15_DURATION_NAME, width='125', order='4')
        parent = project.find('tasks')
        for child in list(parent):
            if child.tag != 'taskproperties':
                parent.remove(child)
        properties = parent.find('taskproperties')
        old_property = properties.find(f"taskproperty[@id='{T15_DURATION_ID}']")
        if old_property is not None:
            properties.remove(old_property)
        ET.SubElement(properties, 'taskproperty', id=T15_DURATION_ID, name=T15_DURATION_NAME,
                      type='custom', valuetype='int')
        calendar_node = project.find('calendars')
        for child in calendar_node.findall('date'):
            calendar_node.remove(child)
        for day in sorted(holidays - working_exceptions):
            ET.SubElement(calendar_node, 'date', year=str(day.year), month=str(day.month), date=str(day.day), type='HOLIDAY')
        for day in sorted(working_exceptions):
            ET.SubElement(calendar_node, 'date', year=str(day.year), month=str(day.month), date=str(day.day),
                          type='WORKING_DAY')

        nodes, offsets, model_dates = {}, {}, {}
        for key in keys:
            if key not in selected:
                continue
            row = tasks[key]
            start, end = row['start'], row['finish']
            duration_t15 = 0 if row['milestone'] else workdays(start, end)
            duration = 0 if row['milestone'] else work_before(end + timedelta(days=1)) - work_before(start)
            style = '#c00000' if key in critical else '#404040' if row['milestone'] else '#4472c4'
            nodes[key] = ET.SubElement(parent, 'task', id=ids[key], name=row['name'], color=style,
                                       meeting=str(row['milestone']).lower(), start=start.isoformat(),
                                       duration=str(duration), complete='0', expand='true')
            ET.SubElement(nodes[key], 'notes').text = row['note']
            ET.SubElement(nodes[key], 'customproperty', {'taskproperty-id': T15_DURATION_ID,
                                                         'value': str(duration_t15)})
            offsets[key] = (work_before(start), work_before(start) + duration)
            model_dates[ids[key]] = (start, end)
        for edge in links:
            a, b, kind = edge['source'], edge['target'], edge['kind']
            if a not in nodes or b not in nodes:
                continue
            a_side, b_side = ('F' if kind in ('FC', 'FF') else 'C'), kind[-1]
            difference = offsets[b][b_side == 'F'] - offsets[a][a_side == 'F']
            ET.SubElement(nodes[a], 'depend', id=ids[b], type=XML_TYPE[kind], difference=str(difference), hardness='Rubber')
        ET.indent(project, space='    ')
        path = target / filename
        ET.ElementTree(project).write(path, encoding='utf-8', xml_declaration=True)
        parsed, parsed_edges = read(path)
        by_id = {r['id']: r for r in parsed}
        assert len(by_id) == len(parsed) == len(nodes), filename
        assert len({(e['source'], e['target']) for e in parsed_edges}) == len(parsed_edges), filename
        topological(by_id, [(e['source'], e['target'], 0) for e in parsed_edges])
        for key in selected:
            row = by_id[ids[key]]
            start, end = model_dates[row['id']]
            assert (row['start'], row['end']) == (start, end), (key, row['start'], row['end'])
            assert row['duration'] == (0 if tasks[key]['milestone'] else workdays(start, end)), key
        for edge in parsed_edges:
            a, b = by_id[edge['source']], by_id[edge['target']]
            kind = TYPES[edge['type']]
            a_date = work_before(a['start']) + (a['duration_gantt'] if kind in ('FC', 'FF') else 0)
            b_date = work_before(b['start']) + (b['duration_gantt'] if kind in ('FF', 'CF') else 0)
            assert b_date == a_date + int(edge['difference']), edge
        return parsed, parsed_edges

    return {
        ACTIVE[0]: write_view(ACTIVE[0], 'Detalle nivelado de implementación y precedencias del SD7', set(keys)),
        ACTIVE[1]: write_view(ACTIVE[1], 'Carta de 56 meses del SD7', {key for key in keys if overview(key, tasks[key])}),
        ACTIVE[2]: write_view(ACTIVE[2], 'Vista de ruta crítica y puertas de aceptación del SD7',
                              critical | {key for key in keys if key.rsplit(':', 1)[-1] in windows and tasks[key]['kind'] == 'event'}),
    }


def main():
    global OUT
    parser = argparse.ArgumentParser(description='Genera PDF y editables de GanttProject desde la red validada.')
    parser.add_argument('--schedule', type=Path, required=True)
    parser.add_argument('--output-dir', type=Path, required=True)
    parser.add_argument('--publish', action='store_true')
    args = parser.parse_args()
    guard()
    model = json.loads(args.schedule.read_text(encoding='utf-8'))
    root = args.output_dir.resolve()
    destination = SRC / 'Revision-local'
    if root == SRC.resolve() or destination.resolve() in (root, *root.parents):
        raise ValueError('Genere en una carpeta temporal distinta de la carpeta de figuras publicadas.')
    OUT = root / 'Revision-local'
    OUT.mkdir(parents=True, exist_ok=True)
    views = generate_views(model, root)
    manifest = {}; log = {'fuentes': {}, 'laminas': {}, 'vistas_historicas': HISTORICAL}
    tasks, edges = views[ACTIVE[0]]
    sizes = [len(tasks) // 7 + (i < len(tasks) % 7) for i in range(7)]
    offset = 0
    for i,n in enumerate(sizes,1):
        block=tasks[offset:offset+n];ids={t['id'] for t in block};rels=[e for e in edges if e['target'] in ids]
        stem=f'Gantt-detalle-{i}';count=make(stem,f'Gantt de implementación · tramo {i} de 7',block,rels)
        old=f'imagenes/Diagramas que faltaban/Gantt-Resumen-Tramos/LafroX-Gantt-resumen-{i}-de-7.png'
        manifest[old]={'stem':stem,'pages':count};log['laminas'][stem]={'paginas':count,'filas':n,'relaciones':len(rels)};offset+=n
    for filename,stem,title,old in [
        ('Fig_7_Gantt_56_Meses.gan','Gantt-56-meses','Carta de los 56 meses','LafroX-Gantt-56-meses.png'),
        ('Fig_7_Gantt_Vista_Critica.gan','Gantt-vista-critica','Vista de la ruta crítica','LafroX-Gantt-vista-critica.png')]:
        ts,es=views[filename];windows=None
        if stem=='Gantt-56-meses':
            a=min(t['start'] for t in ts).replace(day=1);b=add_month(max(t['end'] for t in ts).replace(day=1),1)
            windows=[];lo=a
            while lo<b:hi=min(add_month(lo,24),b);windows.append((lo,hi));lo=hi
        count=make(stem,title,ts,es,windows)
        manifest['imagenes/Diagramas que faltaban/'+old]={'stem':stem,'pages':count}
        log['laminas'][stem]={'paginas':count,'filas':len(ts),'relaciones':len(es)}
    for filename in ['Fig_7_Gantt_Resumen_Dependencias.gan','Fig_7_Gantt_56_Meses.gan','Fig_7_Gantt_Vista_Critica.gan']:
        ts,es=views[filename]
        log['fuentes'][filename]={'sha256':hashlib.sha256((root/filename).read_bytes()).hexdigest(),
                                'tareas':[{k:str(v) if isinstance(v,date) else v for k,v in t.items()} for t in ts], 'relaciones':es}
    fronts=[];origin=ROOT/'formulario-t15/tablas/tab_T15_1.tex'
    for line in origin.read_text(encoding='utf-8').splitlines():
        if not re.match(r'^\s*F\d ',line):continue
        cells=[s.strip() for s in line.strip().removesuffix('\\\\').split(' & ')]
        nums=list(map(int,re.findall(r'\d+',cells[3])))
        a,b=nums[:2];base=date(2027,2,1)
        fronts.append({'id':cells[0].split()[0],'name':cells[0]+'. '+cells[1]+'. Cuentas: '+cells[2]+'. Meses: '+cells[3],
                       'start':add_month(base,a-1),'end':add_month(base,b)-timedelta(days=1),
                       'duration':b-a+1,'color':'#4472c4','milestone':False,'order':len(fronts)})
    assert len(fronts)==8
    count=make('Frentes-trabajo','Frentes de trabajo · meses 1 a 21',fronts,[],[(date(2027,2,1),date(2028,11,1))])
    manifest['imagenes/Diagramas que faltaban/Fig_7-6_T15-2_Frentes_Trabajo.pdf']={'stem':'Frentes-trabajo','pages':count}
    log['frentes']={'fuente':'formulario-t15/tablas/tab_T15_1.tex','sha256':hashlib.sha256(origin.read_bytes()).hexdigest(),'frentes':8,'paginas':count}
    log['mapeo']=manifest;log['tamano_tipografico_minimo_pdf_pt']=9.5
    expected={f'{item["stem"]}-{i}.pdf' for item in manifest.values() for i in range(1,item['pages']+1)}

    (root/'GANTT_VECTOR.json').write_text(json.dumps(log, ensure_ascii=False, indent=2)+'\n', encoding='utf-8')
    if args.publish:
        from shutil import copyfile

        for name in ACTIVE:
            copyfile(root / name, SRC / name)
        for name in HISTORICAL:
            path = SRC / name
            project = ET.parse(path)
            element = project.getroot()
            if not element.get('name').startswith('Histórica · '):
                element.set('name', 'Histórica · ' + element.get('name'))
                desc = element.find('description')
                if desc is not None:
                    desc.text = 'Vista histórica de la EDT por fases. Consultar las tres vistas activas del SD7 para la línea base vigente. ' + (desc.text or '')
                project.write(path, encoding='utf-8', xml_declaration=True)
        for name in expected:
            copyfile(OUT / name, destination / name)
        for path in destination.glob('Gantt-*.pdf'):
            if re.fullmatch(r'Gantt-(?:56-meses|vista-critica|detalle-[1-7])-\d+\.pdf', path.name) and path.name not in expected:
                assert path.resolve().parent == destination.resolve()
                path.unlink()
        copyfile(root / 'GANTT_VECTOR.json', ROOT/'revision/local-20261105/GANTT_VECTOR.json')
        integrate(manifest)
    print(json.dumps(log['laminas'], ensure_ascii=False))


if __name__ == '__main__':
    sys.stdout.reconfigure(encoding='utf-8')
    main()
