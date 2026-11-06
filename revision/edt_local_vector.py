"""Presentación legible de la misma EDT; conserva códigos, ramas y membresía."""
from pathlib import Path
from collections import defaultdict
from html import escape
import json,re,subprocess,sys
from pypdf import PdfReader
from reportlab.pdfgen import canvas
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont
from reportlab.lib.styles import ParagraphStyle
from reportlab.platypus import Paragraph
from reportlab.lib.colors import HexColor

ROOT=Path(__file__).resolve().parents[1];OUT=ROOT/'imagenes/Diagramas que faltaban/Revision-local'
pdfmetrics.registerFont(TTFont('EDTArial','C:/Windows/Fonts/arial.ttf'))
pdfmetrics.registerFont(TTFont('EDTArialBold','C:/Windows/Fonts/arialbd.ttf'))
STYLE=ParagraphStyle('edt',fontName='EDTArial',fontSize=10,leading=12)
BOLD=ParagraphStyle('edtcc',fontName='EDTArialBold',fontSize=10,leading=12)
W=440

def names():
    source=(ROOT/'formulario-t14/contenido.tex').read_text(encoding='utf-8')
    result={}
    for line in source.splitlines():
        m=re.match(r'\\item (?:\\textbf\{)?(\d+(?:\.\d+)*)(?:\.)? (.*)',line)
        if m:
            s=m[2].removesuffix('}') if '\\textbf{' in line else m[2]
            result[m[1]]=s
    return result

def key(code):return tuple(map(int,code.split('.')))

def plain(s):
    return s.replace(r'\allowbreak{}','').replace(r'\%','%').replace(r'\ensuremath{\leq}','≤')

def render(stem,codes,title,lookup):
    bycc=defaultdict(list)
    for code in sorted(codes,key=key):
        if code.count('.')>=2:bycc['.'.join(code.split('.')[:2])].append(code)
        elif code.count('.')==1:bycc.setdefault(code,[])
    blocks=[]
    for cc,items in sorted(bycc.items(),key=lambda x:key(x[0])):
        pcc=Paragraph(escape(cc+' '+plain(lookup[cc])),BOLD);_,ch=pcc.wrap(105,1000)
        rows=[]
        for code in items:
            p=Paragraph(escape(code+' '+plain(lookup[code])),BOLD if code.startswith('3.10.') and code.count('.')==2 else STYLE)
            _,h=p.wrap(278 if code.count('.')==3 else 292,1000)
            rows.append((code,p,max(18,h+7)))
        # Dividir una cuenta extensa conservando explícitamente el mismo padre.
        chunk=[];height=0
        for row in rows:
            if chunk and height+row[2]>360:
                blocks.append((cc,pcc,ch,chunk,max(ch+12,height)+14));chunk=[];height=0
            if not chunk and row[0].count('.')==3:
                parent=row[0].rsplit('.',1)[0]
                pp=Paragraph(escape(parent+' '+plain(lookup[parent])+' (continuación)'),BOLD)
                _,ph=pp.wrap(292,1000);chunk.append((parent,pp,ph+7));height+=ph+7
            chunk.append(row);height+=row[2]
        blocks.append((cc,pcc,ch,chunk,max(ch+12,height)+14))
    pages=[];current=[];height=0
    for block in blocks:
        if current and (height+block[4]>400 or current[-1][0].split('.')[0]!=block[0].split('.')[0]):
            pages.append(current);current=[];height=0
        current.append(block);height+=block[4]
    if current:pages.append(current)
    for i,blocks in enumerate(pages,1):
        h=58+sum(b[4] for b in blocks)+20
        c=canvas.Canvas(str(OUT/f'{stem}-{i}.pdf'),pagesize=(W,h));c.setTitle(title)
        phase=blocks[0][0].split('.')[0]
        page_title=title if title.startswith('Fase ') else f'EDT completa · Fase {phase}: {lookup[phase]}'
        c.setFillColor(HexColor('#253746'));c.setFont('EDTArialBold',11);c.drawString(4,h-15,page_title)
        c.setFont('EDTArial',10);c.drawString(4,h-31,f'Cuentas y paquetes · lámina {i} de {len(pages)}')
        c.setStrokeColor(HexColor('#de6b20'));c.setLineWidth(1);c.line(4,h-40,W-4,h-40)
        y=h-52
        for cc,pcc,ch,rows,bh in blocks:
            rowtotal=sum(r[2] for r in rows)
            c.setFillColor(HexColor('#edf3f7'));c.setStrokeColor(HexColor('#647b8c'));c.setLineWidth(.65)
            c.roundRect(4,y-max(ch+12,24),113,max(ch+12,24),3,fill=1,stroke=1)
            pcc.drawOn(c,8,y-ch-6)
            if rows:
                c.line(117,y-12,129,y-12);c.line(129,y-12,129,y-rowtotal+9)
                yy=y
                group_y={}
                for code,p,rh in rows:
                    if code.count('.')==3:
                        parent=code.rsplit('.',1)[0];gy=group_y.get(parent,yy-9)
                        c.line(141,gy-3,141,yy-9);c.line(141,yy-9,154,yy-9)
                        p.drawOn(c,157,yy-rh+5)
                    else:
                        c.line(129,yy-9,139,yy-9);group_y[code]=yy-9
                        p.drawOn(c,143,yy-rh+5)
                    yy-=rh
            y-=bh
        c.setFont('EDTArial',9.5);c.setFillColor(HexColor('#253746'))
        c.drawString(4,4,'Jerarquía: fase → cuenta de control → paquete o agrupación de innovación.')
        c.save()
    return len(pages)

MACRO=r'''
% La EDT conserva sus figuras; el detalle continúa en páginas sucesivas.
\newcounter{laminaEDTLocal}
\newcommand{\figuraEDTLocal}[4]{%
  \begingroup\setcounter{laminaEDTLocal}{1}%
  \loop
    \ifnum\value{laminaEDTLocal}>1\clearpage\fi
    \par\begin{center}\begin{minipage}{\linewidth}\centering
      \includegraphics[width=\linewidth]{#1-\arabic{laminaEDTLocal}.pdf}\par
      \captionsetup{hypcap=false}
      \ifnum\value{laminaEDTLocal}=1
        \captionof{figure}{#3}\label{#4}%
      \else
        \captionof*{figure}{Figura \ref{#4} (continuación \arabic{laminaEDTLocal} de #2). #3}%
      \fi
    \end{minipage}\end{center}\stepcounter{laminaEDTLocal}%
  \ifnum\value{laminaEDTLocal}<\numexpr#2+1\relax\repeat
  \endgroup\par}
'''

def main():
    assert subprocess.check_output(['git','branch','--show-current'],cwd=ROOT,text=True).strip()=='LafroX-Subdoc7-LateX-CORRIGIENDO'
    lookup=names();mapping={};coverage=set();report=[]
    s7=ROOT/'subdocumento-07/contenido.tex';s=s7.read_text(encoding='utf-8')
    if '\\newcommand{\\figuraEDTLocal}' in s:
        s=re.sub(r'% La EDT conserva.*?\\endgroup\\(?:clearpage|par)\}',lambda m:MACRO,s,flags=re.S,count=1)
    if '\\newcommand{\\figuraEDTLocal}' not in s:s=s.replace('\\newcommand{\\figuraEDTbase}',MACRO+'\n\\newcommand{\\figuraEDTbase}',1)
    for i,p in enumerate(sorted((ROOT/'imagenes/Imagenes de la edt').glob('EDT-Fase*.pdf')),1):
        text='\n'.join(x.extract_text() or '' for x in PdfReader(p).pages)
        found=set(re.findall(r'(?<![\d.])\d+(?:\.\d+){1,3}(?![\d.])',text))&set(lookup)
        for code in list(found):
            if code.count('.')>=2:found.add('.'.join(code.split('.')[:2]))
        phase=re.search(r'Fase (\d+)',p.name)[1]
        stem=f'EDT-detalle-{i:02}';n=render(stem,found,f'Fase {phase} · {lookup[phase]}',lookup)
        rel=str(p.relative_to(ROOT)).replace('\\','/')
        pattern=r'\\figuraEDT(?:Ampliada|Reducida|Escalada|Rotada)?(?:\[[^\]]*\])?(?:\{[\d.]+\}){0,2}\{'+re.escape(rel)+r'\}'
        new='\\figuraEDTLocal{imagenes/Diagramas que faltaban/Revision-local/'+stem+'}{'+str(n)+'}'
        s,count=re.subn(pattern,lambda m:new,s)
        if not count:
            pat=r'\\figuraEDTLocal\{imagenes/Diagramas que faltaban/Revision-local/'+stem+r'\}\{\d+\}'
            s,count=re.subn(pat,lambda m:new,s)
        assert count==1,(p,count)
        coverage|=found;report.append({'origen':rel,'codigos':sorted(found,key=key),'paginas':n,'salida':stem})
    s7.write_text(s,encoding='utf-8')
    # La vista completa utiliza la misma jerarquía del diccionario existente.
    allcodes={c for c in lookup if '.' in c}
    n=render('EDT-completa',allcodes,'EDT completa · nueve fases',lookup)
    p=ROOT/'formulario-t14/contenido.tex';text=p.read_text(encoding='utf-8')
    if '\\newcommand{\\figuraEDTLocal}' in text:
        text=re.sub(r'% La EDT conserva.*?\\endgroup\\(?:clearpage|par)\}',lambda m:MACRO,text,flags=re.S,count=1)
    if '\\newcommand{\\figuraEDTLocal}' not in text:text=text.replace('\\newcommand{\\figuraDiagramaHorizontal}',MACRO+'\n\\newcommand{\\figuraDiagramaHorizontal}',1)
    pattern=r'\\begin\{anexohorizontal\}\s*\\begin\{center\}\s*\\includegraphics\[[^\]]*\]\{imagenes/Imagenes de la edt/EDT-EDT completa.drawio.pdf\}\s*\\captionsetup\{hypcap=false\}\s*\\captionof\{figure\}\{([^\n]+)\}\s*\\label\{([^}]+)\}\s*\\end\{center\}\s*\\end\{anexohorizontal\}'
    def repl(m):return '\\figuraEDTLocal{imagenes/Diagramas que faltaban/Revision-local/EDT-completa}{'+str(n)+'}{'+m[1].replace('Vista panorámica','Vista detallada')+'}{'+m[2]+'}'
    text,count=re.subn(pattern,repl,text)
    if not count:
        text,count=re.subn(r'(\\figuraEDTLocal\{imagenes/Diagramas que faltaban/Revision-local/EDT-completa\})\{\d+\}',lambda m:m[1]+'{'+str(n)+'}',text)
    assert count==1
    p.write_text(text,encoding='utf-8')
    expected=set(re.findall(r'^\s*(\d+(?:\.\d+)+)\s*&',(ROOT/'formulario-t15/tablas/tab_T15_2.tex').read_text(encoding='utf-8'),re.M))
    assert len(expected)==227 and expected<=coverage
    (ROOT/'revision/local-20261105/EDT_VECTOR.json').write_text(json.dumps({'laminas':report,'paquetes':227,'sin_omitir':sorted(expected-coverage),'paginas_vista_completa':n,'tipografia_minima_pt':9.5},ensure_ascii=False,indent=2),encoding='utf-8')
    print(json.dumps({'laminas_detalle':len(report),'paginas_detalle':sum(x['paginas'] for x in report),'paginas_completa':n,'paquetes':227}))

if __name__=='__main__':sys.stdout.reconfigure(encoding='utf-8');main()
