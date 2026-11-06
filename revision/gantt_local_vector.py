"""Recompone las vistas .gan existentes en láminas vectoriales legibles.

No ejecuta un planificador: conserva los atributos XML y el calendario fuente.
Tipos persistentes GanttProject: 1=CC, 2=FC, 3=FF, 4=CF (ConstraintType.java).
"""
from pathlib import Path
from datetime import date,timedelta
from collections import defaultdict
from html import escape
import hashlib,json,math,re,subprocess,sys,xml.etree.ElementTree as ET
from reportlab.pdfgen import canvas
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont
from reportlab.lib.styles import ParagraphStyle
from reportlab.lib.colors import HexColor,Color,white
from reportlab.platypus import Paragraph

ROOT=Path(__file__).resolve().parents[1]
SRC=ROOT/'imagenes/Diagramas que faltaban'
OUT=SRC/'Revision-local'; OUT.mkdir(exist_ok=True)
W,H=624,344
PX,PW=334,284
FONT=10
pdfmetrics.registerFont(TTFont('ArialLocal','C:/Windows/Fonts/arial.ttf'))
pdfmetrics.registerFont(TTFont('ArialLocalBold','C:/Windows/Fonts/arialbd.ttf'))
STYLE=ParagraphStyle('fila',fontName='ArialLocal',fontSize=10,leading=11.7,textColor=HexColor('#253746'))
TYPES={'1':'CC','2':'FC','3':'FF','4':'CF'}

def guard():
    branch=subprocess.check_output(['git','branch','--show-current'],cwd=ROOT,text=True).strip()
    assert branch=='LafroX-Subdoc7-LateX-CORRIGIENDO',branch

def add_month(d,n):
    m=d.year*12+d.month-1+n
    return date(m//12,m%12+1,1)

def read(name):
    root=ET.parse(SRC/name).getroot()
    holidays={date(int(d.get('year')),int(d.get('month')),int(d.get('date')))
              for d in root.findall('./calendars/date') if d.get('type')=='HOLIDAY'}
    def finish(a,n):
        if not n:return a
        d=a; left=n
        while True:
            if d.weekday()<5 and d not in holidays:
                left-=1
                if left==0:return d
            d+=timedelta(days=1)
    tasks=[];edges=[]
    for i,t in enumerate(root.findall('.//task')):
        a=date.fromisoformat(t.get('start'));n=int(t.get('duration'))
        tasks.append({'id':t.get('id'),'name':t.get('name'),'start':a,'end':finish(a,n),
                      'duration':n,'color':t.get('color','#4472c4'),'milestone':t.get('meeting')=='true',
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
    label(c,5,16,'RC: ruta crítica marcada en la fuente. PT/H: demás paquetes e hitos.',size=9.5)
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
    m=a
    while m<b:
        nxt=add_month(m,1);lo=x(m);hi=x(nxt)
        if m.month%2==0:
            c.setFillColor(HexColor('#f2f5f7'));c.rect(lo,bottom,max(.1,hi-lo),ytop-bottom,fill=1,stroke=0)
        c.setStrokeColor(HexColor('#d5dde3'));c.setLineWidth(.35);c.line(lo,bottom,lo,ytop+2)
        c.setFont('ArialLocal',9.5);c.setFillColor(HexColor('#253746'));c.drawCentredString((lo+hi)/2,ytop+7,f'{m.month:02}')
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
        label(c,5,15,'Los ID permiten seguir los vínculos entre láminas. Desfases en días hábiles.',size=9.5)
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
    for folder in ['subdocumento-07','formulario-t14','formulario-t15']:
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
        if folder=='subdocumento-07':
            text=text.replace('{imagenes/Diagramas que faltaban/Fig_7-20_Red_Precedencias.pdf}',
                              '{imagenes/Diagramas que faltaban/Revision-local/Fig_7-20_Red_Precedencias.pdf}')
        p.write_text(text,encoding='utf-8')

def main():
    guard();manifest={};log={'fuentes':{},'laminas':{}}
    tasks,edges=read('Fig_7_Gantt_Resumen_Dependencias.gan');assert len(tasks)==155 and len(edges)==262
    sizes=[23,22,22,22,22,22,22];offset=0
    for i,n in enumerate(sizes,1):
        block=tasks[offset:offset+n];ids={t['id'] for t in block};rels=[e for e in edges if e['target'] in ids]
        stem=f'Gantt-detalle-{i}';count=make(stem,f'Gantt de implementación · tramo {i} de 7',block,rels)
        old=f'imagenes/Diagramas que faltaban/Gantt-Resumen-Tramos/LafroX-Gantt-resumen-{i}-de-7.png'
        manifest[old]={'stem':stem,'pages':count};log['laminas'][stem]={'paginas':count,'filas':n,'relaciones':len(rels)};offset+=n
    for filename,stem,title,old in [
        ('Fig_7_Gantt_56_Meses.gan','Gantt-56-meses','Carta de los 56 meses','LafroX-Gantt-56-meses.png'),
        ('Fig_7_Gantt_Vista_Critica.gan','Gantt-vista-critica','Vista de la ruta crítica','LafroX-Gantt-vista-critica.png')]:
        ts,es=read(filename);windows=None
        if stem=='Gantt-56-meses':
            a=min(t['start'] for t in ts).replace(day=1);b=add_month(max(t['end'] for t in ts).replace(day=1),1)
            windows=[];lo=a
            while lo<b:hi=min(add_month(lo,24),b);windows.append((lo,hi));lo=hi
        count=make(stem,title,ts,es,windows)
        manifest['imagenes/Diagramas que faltaban/'+old]={'stem':stem,'pages':count}
        log['laminas'][stem]={'paginas':count,'filas':len(ts),'relaciones':len(es)}
    for filename in ['Fig_7_Gantt_Resumen_Dependencias.gan','Fig_7_Gantt_56_Meses.gan','Fig_7_Gantt_Vista_Critica.gan']:
        ts,es=read(filename)
        log['fuentes'][filename]={'sha256':hashlib.sha256((SRC/filename).read_bytes()).hexdigest(),
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
    for path in OUT.glob('Gantt-*.pdf'):
        # Sólo salidas de este generador, dentro de su carpeta exclusiva.
        assert path.resolve().parent==OUT.resolve()
        if path.name not in expected:path.unlink()
    (ROOT/'revision/local-20261105/GANTT_VECTOR.json').write_text(json.dumps(log,ensure_ascii=False,indent=2),encoding='utf-8')
    integrate(manifest);print(json.dumps(log['laminas'],ensure_ascii=False))

if __name__=='__main__':sys.stdout.reconfigure(encoding='utf-8');main()
