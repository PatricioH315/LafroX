"""Convierte cuerpo SD8, anexos y T-16; no modifica Markdown ni clase."""
import argparse,hashlib,json,math,re
from pathlib import Path
ap=argparse.ArgumentParser()
ap.add_argument('--root',type=Path,default=Path(__file__).resolve().parent)
ap.add_argument('--apply',action='store_true')
args=ap.parse_args()
ROOT=args.root.resolve()
assert ROOT==Path(r'C:\Users\henri\OneDrive\Documentos\Universidad 2026S2\FEP\Bases PTE\Subdoc\LafroX').resolve()
SOURCE=ROOT.parent.parent/'Git Markdown'/'LafroX'/'08_plan_riesgos'
DEST=ROOT/'08_plan_riesgos'
BT=chr(96)
def esc(text):
    mp={'\\':r'\textbackslash{}','&':r'\&','%':r'\%','$':r'\$','#':r'\#','_':r'\_','{':r'\{','}':r'\}','~':r'\textasciitilde{}','^':r'\textasciicircum{}',
        '≤':r'\ensuremath{\leq}','≥':r'\ensuremath{\geq}','×':r'\ensuremath{\times}','−':r'\ensuremath{-}','→':r'\ensuremath{\rightarrow}','≈':r'\ensuremath{\approx}',
        'Σ':r'\ensuremath{\Sigma}','λ':r'\ensuremath{\lambda}','μ':r'\ensuremath{\mu}','Φ':r'\ensuremath{\Phi}','σ':r'\ensuremath{\sigma}',
        '⌈':r'\ensuremath{\lceil}','⌉':r'\ensuremath{\rceil}'}
    return ''.join(mp.get(c,c) for c in text)
def inline(text):
    tokens=[]
    def save(m):
        tokens.append(r'\texttt{'+esc(m[1])+'}')
        return f'ZZTOKEN{len(tokens)-1}ZZ'
    text=re.sub(BT+'([^'+BT+']+)'+BT,save,text); text=esc(text)
    text=re.sub(r'\*\*(.+?)\*\*',r'\\textbf{\1}',text)
    text=re.sub(r'\*([^*]+)\*',r'\\emph{\1}',text)
    for i,v in enumerate(tokens): text=text.replace(f'ZZTOKEN{i}ZZ',v)
    return text
def convert(name,kind):
    lines=(SOURCE/name).read_text(encoding='utf-8-sig').splitlines()
    out=['% Fuente Markdown: '+name,'% Contenido conservado; formato lafrox.cls.']
    ledger=[]; i=1; nt=0; pending=None; scope='Plan de riesgos'; inlist=False
    while i<len(lines):
        s=lines[i].strip()
        if inlist and not s.startswith('- '): out.append(r'\end{itemize}'); inlist=False
        fence=re.match('^('+BT*3+r'|~~~)(\w*)',s)
        if fence:
            mark,lang=fence.groups(); i+=1; block=[]
            while i<len(lines) and not lines[i].strip().startswith(mark): block.append(lines[i]); i+=1
            assert i<len(lines),'Bloque de codigo sin cierre'
            if lang=='mermaid': out.append(r'\parte{figuras/rbs}')
            else:
                out.append(r'\begin{Verbatim}[fontsize=\footnotesize,breaklines=true,breakanywhere=true,breaksymbolleft={}]')
                out+=block; out.append(r'\end{Verbatim}'); ledger.append(('code','\n'.join(block)))
            i+=1; continue
        if s.startswith('**Figura 8.1'): i+=1; continue
        cap=re.fullmatch(r'\*\*Tabla ([\w.]+)\s*[—–-]\s*(.*?)\*\*',s)
        if cap: pending=cap.groups(); i+=1; continue
        if s.startswith('|'):
            rows=[]
            while i<len(lines) and lines[i].strip().startswith('|'):
                cs=[c.strip() for c in lines[i].strip().strip('|').split('|')]
                if not all(re.fullmatch(r':?-+:?',c) for c in cs): rows.append(cs)
                i+=1
            n=len(rows[0]); nt+=1; assert all(len(r)==n for r in rows)
            fallback = ('8.IA.1','Declaración de uso de IA') if kind=='cuerpo' else ('8.A.1','Glosario de códigos') if kind=='anexos' and nt==1 else ('8.IA.2','Declaración de uso de IA') if kind=='anexos' else (f'T-16.{nt}',scope)
            number,title=pending or fallback
            landscape=kind in ('anexos','t16') and n>=7
            if landscape: out.append(r'\begin{landscape}')
            out.append(r'\begingroup'); out.append(r'\renewcommand{\thetable}{'+number+'}')
            weights=[max(1.,math.sqrt(sum(len(r[c]) for r in rows)/len(rows))) for c in range(n)]
            if kind=='t16' and n==8: weights=[1.4,3,1.8,1,1.1,1.1,6.5,2.2]
            weights=[w*n/sum(weights) for w in weights]
            cols=' '.join(r'>{\hsize='+f'{w:.5f}'+r'\hsize\linewidth=\hsize\RaggedRight\arraybackslash}X' for w in weights)
            out.append(r'\begin{tablalafrox}{'+inline(title)+'}{tab:sd8-'+kind+'-'+str(nt)+'}{'+cols+'}{'+' & '.join(r'\cab{'+inline(c)+'}' for c in rows[0])+'}')
            out+=[' & '.join(inline(c) for c in r)+r' \\' for r in rows[1:]]
            out.append(r'\end{tablalafrox}'); out.append(r'\endgroup')
            if landscape: out.append(r'\end{landscape}')
            ledger += [('inline',c) for r in rows for c in r]
            pending=None; continue
        hd=re.match(r'(#+)\s+(.+)',s)
        if hd:
            lev,title=len(hd[1]),hd[2]; scope=title
            if kind=='cuerpo' and title=='Introducción a los Riesgos': i+=1; continue
            if kind=='cuerpo' and re.match(r'^8\.\d',title):
                title=re.sub(r'^8\.\d+(?:\.\d+)*\s+','',title)
                cmd={2:'section',3:'subsection',4:'subsubsection'}.get(lev,'paragraph')
                out.append('\\'+cmd+'{'+inline(title)+'}')
            else:
                cmd={1:'section',2:'section',3:'subsection',4:'subsubsection'}.get(lev,'paragraph')
                if title.startswith('Anexo 8.'): out.append(r'\clearpage')
                out.append('\\'+cmd+'*{'+inline(title)+'}')
                out.append(r'\addcontentsline{toc}{'+cmd+'}{'+inline(title)+'}')
            i+=1; continue
        if s.startswith('- '):
            if not inlist: out.append(r'\begin{itemize}[leftmargin=*,itemsep=3pt]'); inlist=True
            out.append(r'\item '+inline(s[2:])); ledger.append(('inline',s[2:]))
        elif s=='---': out.append(r'\medskip')
        elif s: out.append(inline(s)); ledger.append(('inline',s))
        else: out.append('')
        i+=1
    if inlist: out.append(r'\end{itemize}')
    tex='\n'.join(out)+'\n'
    for typ,v in ledger: assert (v if typ=='code' else inline(v)) in tex,(name,v)
    return tex,{'source':name,'sha256':hashlib.sha256((SOURCE/name).read_bytes()).hexdigest(),'tables':nt,'verified_items':len(ledger)}
outputs={}; checks=[]
for name,kind,path in [('LAFROX-Subdocumento8.md','cuerpo','partes/cuerpo.tex'),('LAFROX-Subdocumento8-Anexos.md','anexos','anexos/anexos.tex'),('LAFROX-Formulario-T-16.md','t16','formularios/t16.tex')]:
    outputs[DEST/path],check=convert(name,kind); checks.append(check)
outputs[DEST/'soporte.tex']=r'''\usepackage{fvextra}
\usepackage{pdflscape}
'''
outputs[DEST/'contenido.tex']=r'''\chapter{Introducción a los Riesgos}
\label{cap:sd8}
\parte{partes/cuerpo}
'''
outputs[DEST/'entrada-anexos.tex']=r'''\setcounter{chapter}{8}
\chapter*{Anexos del Subdocumento 8}
\addcontentsline{toc}{chapter}{Anexos del Subdocumento 8}
\parte{anexos/anexos}
'''
outputs[DEST/'entrada-t16.tex']=r'''\setcounter{chapter}{8}
\chapter*{Formulario T-16: Plan de riesgos}
\addcontentsline{toc}{chapter}{Formulario T-16: Plan de riesgos}
\parte{formularios/t16}
'''
def wrapper(document,title,name,entry):
    return r'''\documentclass[carta,firma,sinnotas]{lafrox}
\input{08_plan_riesgos/soporte.tex}
\datoslafrox{
  documento = {'''+document+r'''},
  subtitulo = {'''+title+r'''},
  alcance = {Gestión de riesgos de la propuesta LafroX},
  formulario = {T-16: Plan de riesgos},
  fecha = {},
  version = {0.1},
  nomenclatura = {'''+name+r'''},
}
\begin{document}
\portadalafrox
\preliminareslafrox
\setcounter{chapter}{7}
'''+entry+r'''
\end{document}
'''
body=wrapper('Subdocumento 8: Plan de riesgos','Plan de riesgos','LAFROX-Subdocumento8',r'\subdocumento{08_plan_riesgos}')
outputs[ROOT/'main.tex']=body
outputs[DEST/'LAFROX-Subdocumento8.tex']=body
outputs[DEST/'LAFROX-Subdocumento8-Anexos.tex']=wrapper('Subdocumento 8: Anexos','Anexos 8.A--8.F','LAFROX-Subdocumento8-Anexos',r'\import{08_plan_riesgos/}{entrada-anexos.tex}')
outputs[DEST/'LAFROX-Formulario-T-16.tex']=wrapper('Formulario T-16: Plan de riesgos','Registro de las 32 amenazas','LAFROX-Formulario-T-16',r'\import{08_plan_riesgos/}{entrada-t16.tex}')
fig=(DEST/'figuras/rbs.tex').read_text(encoding='utf-8')
fig=fig.replace(r'\small',r'\fontsize{9.5}{11.5}\selectfont').replace('text width=4.7cm','text width=4.05cm')
fig=fig.replace('(-5.3,','(-4.75,').replace('(5.3,','(4.75,').replace('(-0.25,0)','(-0.18,0)')
fig=fig.replace('draw=lafroxNaranja,rounded corners,fill=lafroxNaranja!7','draw=lafroxGris,rounded corners')
fig=fig.replace('inner sep=8pt','inner sep=5pt').replace('inner sep=7pt','inner sep=5pt')
fig=fig.replace(',-5.6)',',-6.0)').replace(',-7.3)',',-8.0)')
fig=fig.replace('R8-02 · R8-04 · R8-06 · R8-08'+chr(92)*2+'R8-09 · R8-27 · R8-30','R8-02 · R8-04 · R8-06'+chr(92)*2+'R8-08 · R8-09 · R8-27'+chr(92)*2+'R8-30')
for group in ['R8-01 · R8-03 · R8-05 · R8-23','R8-11 · R8-14 · R8-15 · R8-31','R8-20 · R8-21 · R8-25 · R8-29']:
    words=group.split(' · ')
    fig=fig.replace(group,' · '.join(words[:2])+chr(92)*2+' · '.join(words[2:]))
fig=re.sub(r'(?<!\{)(R8-\d\d)',lambda m:chr(92)+'mbox{'+m[1]+'}',fig)
assert sorted(set(re.findall(r'R8-\d\d',fig)))==[f'R8-{i:02}' for i in range(1,33)]
outputs[DEST/'figuras/rbs.tex']=fig
outputs[DEST/'README.md']='''# Subdocumento 8 — Plan de riesgos

Las fuentes LaTeX reproducen el cuerpo, los Anexos 8.A–8.F y el T-16 vigentes.
Se conservan texto, cifras y los 18 campos pendientes de revisión humana.
La RBS se dibuja en TikZ y el modelo Python se mantiene literal con ajuste de líneas.

## Entradas independientes

Compilar desde la raíz del proyecto con LuaLaTeX:

~~~powershell
lualatex --interaction=nonstopmode --halt-on-error --jobname=LAFROX-Subdocumento8 08_plan_riesgos/LAFROX-Subdocumento8.tex
lualatex --interaction=nonstopmode --halt-on-error --jobname=LAFROX-Subdocumento8-Anexos 08_plan_riesgos/LAFROX-Subdocumento8-Anexos.tex
lualatex --interaction=nonstopmode --halt-on-error --jobname=LAFROX-Formulario-T-16 08_plan_riesgos/LAFROX-Formulario-T-16.tex
~~~

Repetir hasta estabilizar índices y referencias. main.tex monta sólo el cuerpo:
anexos y formulario son independientes. Se conservan la clase lafrox.cls,
la portada, los logotipos y la configuración común. Las tablas extensas de
anexos/formulario usan páginas horizontales con encabezado repetido; el cuerpo
permanece vertical. La fecha de entrega no se inventa y queda vacía.

## Actualizar desde Markdown

~~~powershell
python convertir_sd8.py --apply
~~~

Sin --apply, el conversor verifica párrafos, celdas y código sin escribir.
La presentación se valida compilando y revisando el PDF. Los marcadores de
revisión humana sólo se completan después de una revisión real.
'''
outputs[ROOT/'convertir_sd8.py']=Path(__file__).read_text(encoding='utf-8')
if args.apply:
    for path,text in outputs.items():
        path.parent.mkdir(parents=True,exist_ok=True)
        path.write_text(text,encoding='utf-8',newline='\n')
print(json.dumps({'mode':'applied' if args.apply else 'dry_run','checks':checks,'files':[str(x.relative_to(ROOT)) for x in outputs],
'human_cells':sum(s.count('[[REVISIÓN HUMANA]]') for path,s in outputs.items() if path.name in ['cuerpo.tex','anexos.tex','t16.tex']),
'current_contingency':'35.219,98' in outputs[DEST/'partes/cuerpo.tex'],
'code_lines':len(re.search(r'~~~python\n(.*?)\n~~~',(SOURCE/'LAFROX-Subdocumento8-Anexos.md').read_text(encoding='utf-8'),re.S)[1].splitlines())},ensure_ascii=False))
