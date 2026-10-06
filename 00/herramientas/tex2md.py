#!/usr/bin/env python3
"""Convert the three Subdocument 4 LaTeX entry points to Markdown (stdlib only)."""
from __future__ import annotations
import argparse, html, re, urllib.parse
from pathlib import Path

COMMIT = "a422d30baeaf69a3cce14909bf38e549f4f6d5fd"
REPO_URL = "https://raw.githubusercontent.com/PatricioH315/LafroX/" + COMMIT + "/"

def arg(s: str, pos: int) -> tuple[str, int]:
    while pos < len(s) and s[pos].isspace(): pos += 1
    if pos >= len(s) or s[pos] != "{": return "", pos
    depth, i = 1, pos + 1
    while i < len(s) and depth:
        if s[i] == "\\": i += 2; continue
        if s[i] == "{": depth += 1
        elif s[i] == "}": depth -= 1
        i += 1
    return s[pos+1:i-1], i

def commands(s: str, name: str):
    pat = re.compile(r"\\"+re.escape(name)+r"\b")
    for m in pat.finditer(s):
        a, end = arg(s, m.end())
        if end > m.end(): yield m.start(), end, a

def clean_comments(s: str) -> str:
    return re.sub(r"(?<!\\)%[^\n]*", "", s)

def expand(path: Path, stack=()) -> str:
    path = path.resolve()
    if path in stack: return ""
    try: s = clean_comments(path.read_text(encoding="utf-8"))
    except OSError: return ""
    # Expand the actual import/input graph. \parte paths are relative to each
    # assembler's directory; \import carries its own base directory.
    pattern = re.compile(r"\\(import|subimport|input|include|parte)(?![A-Za-z@])")
    out, last = [], 0
    for m in pattern.finditer(s):
        out.append(s[last:m.start()]); pos=m.end(); name=m.group(1)
        if name in ("import", "subimport"):
            base, pos = arg(s,pos); target, pos=arg(s,pos)
            candidate=(path.parent/base/target)
        else:
            target,pos=arg(s,pos)
            candidate=path.parent/target
        if candidate.suffix != ".tex": candidate=candidate.with_suffix(".tex")
        if candidate.exists(): out.append(expand(candidate,stack+(path,)))
        last=pos
    out.append(s[last:]); return "\n".join(out)

def aux_labels(build: Path, stem: str):
    text=(build/(stem+".aux")).read_text(encoding="utf-8",errors="replace")
    result={}
    for m in re.finditer(r"\\newlabel\{([^}]+)\}\{\{([^}]*)\}\{[^}]*\}\{([^}]*)\}",text):
        result[m.group(1)]={"number":m.group(2),"title":re.sub(r"\s+"," ",m.group(3)).strip()}
    return result

def toc_entries(build: Path, stem: str):
    toc_file=build/(stem+".toc")
    if toc_file.exists(): text=toc_file.read_text(encoding="utf-8",errors="replace")
    else:
        aux=build/(stem+".aux")
        aux_text=aux.read_text(encoding="utf-8",errors="replace") if aux.exists() else ""
        chunks=[]
        for _,end,which in commands(aux_text,"@writefile"):
            if which.strip()=="toc":
                chunk,end2=arg(aux_text,end); chunks.append(chunk)
        text="\n".join(chunks)
    es=[]
    for m in re.finditer(r"\\contentsline \{(chapter|section|subsection|subsubsection|paragraph)\}\{(.*?)\}\{[^}]*\}",text):
        val=m.group(2); n=re.match(r"\\numberline \{([^}]*)\}(.*)",val)
        if n: number,title=n.group(1),n.group(2)
        else: number,title="",val
        title=plain(title)
        if title in ("Índice general","Lista de tablas","Lista de figuras"): continue
        es.append((m.group(1),number,title))
    return es

def lof_entries(build: Path, stem: str):
    f=build/(stem+".lof")
    if not f.exists(): return []
    text=f.read_text(encoding="utf-8",errors="replace")
    out=[]
    pat=r"\\contentsline\s*\{figure\}\s*\{\s*\\numberline\s*\{([^}]+)\}\s*\{\\ignorespaces\s*(.*?)\}\s*\{"
    for m in re.finditer(pat,text,re.S): out.append((m.group(1).strip(),re.sub(r"\s+"," ",plain(m.group(2))).strip()))
    return out

def plain(s: str) -> str:
    s=re.sub(r"\\[a-zA-Z@]+\*?", "", s)
    s=s.replace("{","").replace("}","")
    return re.sub(r"\s+"," ",s).strip()

def split_top(s: str, delim: str):
    out=[]; start=0; depth=0; i=0
    while i<len(s):
        if s[i]=="\\": i+=2; continue
        if s[i]=="{": depth+=1
        elif s[i]=="}": depth=max(0,depth-1)
        elif s.startswith(delim,i) and depth==0: out.append(s[start:i]); start=i+len(delim); i+=len(delim); continue
        i+=1
    out.append(s[start:]); return out

def md_inline(s: str, labels, doc, anchor_to_doc, root: Path):
    s=s.replace("~"," ").replace("\\,"," ").replace("\\%","%").replace("\\&","&").replace("\\_","_")
    # Las filas separadoras de tablas GFM ya generadas conservan sus guiones.
    s=re.sub(r"(?m)^(?!\|(?: --- \|)+$).*$",lambda m:m.group(0).replace("---","—").replace("--","–"),s)
    s=s.replace("\\times","×")
    s=s.replace(r"\textdegree{}","°").replace(r"\textdegree","°").replace(r"\N{}","N.º")
    for tex,symbol in ((r"\approx","≈"),(r"\leq","≤"),(r"\geq","≥"),(r"\pm","±"),(r"\div","÷"),(r"\circ","°"),(r"\S","§"),(r"\rightarrow","→"),(r"\Rightarrow","⇒")):
        s=s.replace(tex,symbol)
    s=re.sub(r"\\(?:textbf|bfseries)\s*\{([^{}]*)\}",r"**\1**",s)
    s=re.sub(r"\\(?:textit|emph|itshape)\s*\{([^{}]*)\}",r"*\1*",s)
    s=re.sub(r"\\texttt\s*\{([^{}]*)\}",r"`\1`",s)
    s=re.sub(r"\\cab\s*\{([^{}]*)\}",r"**\1**",s)
    s=re.sub(r"\\minititulo\s*\{([^{}]*)\}",r"\n\n**\1**\n\n",s)
    def label_name(key):
        info=labels.get(key,{"number":"??","title":key}); n=info["number"] or info["title"]
        if key.startswith("anx:") and not n:
            suffix=key.split(":",1)[1]; n="4-W" if suffix=="42A" else "4-"+suffix
        if key.startswith("tab:"): return "Tabla "+n
        if key.startswith("fig:"): return "Figura "+n
        if key.startswith("anx:"): return "Anexo "+n
        return "sección "+n
    # Resolve nested page references before the outer hyperref so Markdown
    # never contains a link inside a link.
    hpat=r"\\hyperref\[([^]]+)\]\{((?:[^{}]|\{[^{}]*\})*)\}"
    def full_hyper(m):
        key=m.group(1); label=label_name(key); text=m.group(2)
        text=re.sub(r"(?:pág\.?|página)\s*\\pageref\*?\s*\{[^}]+\}",label,text)
        text=re.sub(r"\\pageref\*?\s*\{[^}]+\}",label,text)
        text=md_inline(text,labels,doc,anchor_to_doc,root)
        dest=anchor_to_doc.get(key,doc); fn={"cuerpo":"LAFROX-Subdocumento4.md","anexos":"LAFROX-Subdocumento4-Anexos.md","t11":"LAFROX-Formulario-T-11.md"}[dest]
        return f"[{text}]({fn}#{key})"
    s=re.sub(hpat,full_hyper,s)
    s=re.sub(r"(?:pág\.?|página)\s*\\pageref\*?\s*\{([^}]+)\}",lambda m:label_name(m.group(1)),s)
    for cmd in ("ref","autoref","cref","Cref","pageref"):
        def ref(m):
            key=m.group(1); info=labels.get(key,{"number":"??","title":key}); n=info["number"] or info["title"]
            if not n: n=label_name(key)
            if cmd in ("autoref","cref","Cref","pageref"): n=label_name(key)
            dest=anchor_to_doc.get(key,doc); fn={"cuerpo":"LAFROX-Subdocumento4.md","anexos":"LAFROX-Subdocumento4-Anexos.md","t11":"LAFROX-Formulario-T-11.md"}[dest]
            # Pageref intentionally denotes its labeled section/table/figure.
            return f"[{n}]({fn}#{key})"
        s=re.sub(r"\\"+cmd+r"\*?\s*\{([^}]+)\}",ref,s)
    s=re.sub(r"\\href\s*\{([^}]+)\}\s*\{([^{}]*)\}",r"[\2](\1)",s)
    s=re.sub(r"\\url\s*\{([^}]+)\}",r"<\1>",s)
    s=re.sub(r"\\footnote\s*\{([^{}]*)\}",r"[^1]",s)
    s=re.sub(r"\\label\s*\{([^}]+)\}",lambda m:f'<a id="{m.group(1)}"></a>',s)
    s=re.sub(r"\\begin\{(itemize|enumerate)\}|\\end\{(itemize|enumerate)\}","",s)
    s=re.sub(r"\\item(?:\[[^]]*\])?\s*", "\n- ",s)
    # Common text commands with one argument; retain their visible text.
    s=re.sub(r"\\(?:text|mbox|ensuremath|MakeUppercase|MakeLowercase)\s*\{([^{}]*)\}",r"\1",s)
    s=re.sub(r"\\(?:ldots|dots)","…",s).replace("\\rightarrow","→").replace("\\Rightarrow","⇒")
    s=re.sub(r"\\[a-zA-Z@]+\*?(?:\[[^]]*\])?\s*", "",s)
    s=s.replace("\\{","{").replace("\\}","}").replace("\\#","#")
    s=s.replace("$","")
    # Discard TeX grouping braces left by style-only macros, preserving literal
    # braces in inline code spans.
    chunks=re.split(r"(`[^`]*`)",s)
    for i in range(0,len(chunks),2): chunks[i]=chunks[i].replace("{","").replace("}","")
    s="".join(chunks)
    return re.sub(r"[ \t]+"," ",s).strip()

def table_md(raw: str, title: str, number: str, label: str, labels, doc, links, root):
    raw=re.sub(r"\\(toprule|midrule|bottomrule|hline|cline\{[^}]*\})", "",raw)
    rows=[]
    for line in re.split(r"\\\\(?:\s*\[[^]]*\])?",raw):
        line=line.strip()
        if not line or line.startswith("\\end"): continue
        line=re.sub(r"\\(multicolumn|multirow)\s*\{[^}]*\}\s*\{[^}]*\}\s*", "",line)
        cells=[md_inline(c,labels,doc,links,root).replace("\n","<br>") for c in split_top(line,"&")]
        if any(cells): rows.append(cells)
    if not rows: return ""
    width=max(map(len,rows)); rows=[r+([""]*(width-len(r))) for r in rows]
    out=[f"**Tabla {number} — {md_inline(title,labels,doc,links,root)}**", "", "| "+" | ".join(rows[0])+" |", "| "+" | ".join(["---"]*width)+" |"]
    out += ["| "+" | ".join(r)+" |" for r in rows[1:]]
    # El ancla va antes del título: pegada a la última fila, GFM la leería como otra fila.
    if label: out=[f'<a id="{label}"></a>',""]+out
    return "\n".join(out)

def convert(source: str, doc, stem, toc, labels, links, root):
    # The assembled entry points include their preambles; convert document bodies only.
    if r"\begin{document}" in source: source=source.split(r"\begin{document}",1)[1]
    if r"\end{document}" in source: source=source.rsplit(r"\end{document}",1)[0]
    # The class offers this four-argument shorthand even though the current
    # Subdocument 4 sources use explicit figure environments instead.
    while True:
        m=re.search(r"\\figuralafrox\b",source)
        if not m: break
        pos=m.end(); args=[]
        for _ in range(4):
            value,pos=arg(source,pos);args.append(value)
        width,image,caption,label=args; number=labels.get(label,{}).get("number","?")
        rel=Path("04")/image.strip(); block=f"**Figura {number} — {md_inline(caption,labels,doc,links,root)}**"
        if (root/rel).is_file(): block+=f"\n\n![{md_inline(caption,labels,doc,links,root)}]({REPO_URL+urllib.parse.quote(rel.as_posix(),safe='/-._~')})"
        block+=f'\n\nFuente: elaboración propia.\n\n<a id="{label}"></a>'
        source=source[:m.start()]+block+source[pos:]
    # Drop layout-only material and comments already removed during expansion.
    source=re.sub(r"\\(?:clearpage|newpage|FloatBarrier|pagebreak|noindent|centering|smallskip|medskip|bigskip|vspace\*?|hspace\*?)\s*(?:\{[^}]*\})?", "\n",source)
    # Convert custom LafroX tables with a brace-aware reader (the header has
    # nested commands and the column specification may span several lines).
    cursor=0
    while True:
        m=re.search(r"\\begin\{(tablalafrox|tablalarga)\}",source[cursor:])
        if not m: break
        env=m.group(1); start=cursor+m.start(); pos=cursor+m.end(); args=[]
        for _ in range(4):
            value,pos=arg(source,pos); args.append(value)
        endm=re.search(r"\\end\{"+env+r"\}",source[pos:])
        if not endm: break
        end=pos+endm.end(); title,label,cols,header=args
        n=labels.get(label,{}).get("number","?")
        rendered=table_md(header+" \\\\\n"+source[pos:pos+endm.start()],title,n,label,labels,doc,links,root)
        source=source[:start]+"\n\n"+rendered+"\n\n"+source[end:]
        cursor=start+len(rendered)
    # Convert standard table floats as well.
    def standard_table(m):
        b=m.group(0); cm=re.search(r"\\caption\s*\{([^{}]*)\}",b); lm=re.search(r"\\label\s*\{([^}]+)\}",b)
        if not cm: return ""
        label=lm.group(1) if lm else ""; info=labels.get(label,{"number":"?"})
        tm=re.search(r"\\begin\{(?:tabular|tabularx|longtable)\}.*?\\end\{(?:tabular|tabularx|longtable)\}",b,re.S)
        return table_md(tm.group(0) if tm else "",cm.group(1),info["number"],label,labels,doc,links,root)
    source=re.sub(r"\\begin\{table\*?\}.*?\\end\{table\*?\}",standard_table,source,flags=re.S)
    # Captions/labels/graphics in figure blocks, including captionof figures.
    def fig(m):
        b=m.group(0); cm=re.search(r"\\caption(?:of\s*\{figure\})?\s*\{([^{}]*)\}",b)
        gm=re.search(r"\\includegraphics(?:\[[^]]*\])?\s*\{([^}]+)\}",b)
        lm=re.search(r"\\label\s*\{([^}]+)\}",b)
        if not cm: return ""
        label=lm.group(1) if lm else ""; info=labels.get(label,{"number":"?"}); num=info["number"]
        if not gm:
            # Native TikZ drawings have no committed raster/vector asset. Keep
            # their compiled title and anchor in document order.
            return f"\n\n**Figura {num} — {md_inline(cm.group(1),labels,doc,links,root)}**\n\nFuente: elaboración propia.\n\n"+(f'<a id="{label}"></a>' if label else "")
        rel=Path("04")/gm.group(1).strip()
        if not (root/rel).exists():
            # graphicspath is 04/ for this document; referenced paths are repo-relative.
            rel=Path("04")/gm.group(1).strip()
        url=REPO_URL+urllib.parse.quote(rel.as_posix(),safe="/-._~")
        source_line=""
        fm=re.search(r"\\fuentefigura(?:\s*\[([^]]*)\])?",b)
        if fm: source_line="\n\nFuente: "+(fm.group(1) or "elaboración propia")+"."
        return f"\n\n**Figura {num} — {md_inline(cm.group(1),labels,doc,links,root)}**\n\n![{html.escape(md_inline(cm.group(1),labels,doc,links,root))}]({url}){source_line}\n\n"+(f'<a id="{label}"></a>' if label else "")
    source=re.sub(r"\\begin\{figure\*?\}.*?\\end\{figure\*?\}",fig,source,flags=re.S)
    # Diagrams in the logical chapter use captionof inside center, not a float.
    cursor=0
    while True:
        gm=re.search(r"\\includegraphics(?:\[[^]]*\])?\s*\{([^}]+)\}",source[cursor:])
        if not gm: break
        start=cursor+gm.start(); gend=cursor+gm.end(); tail=source[gend:]
        cm=re.search(r"\\captionof\s*\{figure\}\s*\{([^{}]*)\}",tail)
        if not cm:
            cursor=gend; continue
        cstart=gend+cm.start(); cend=gend+cm.end()
        labelm=re.search(r"\\label\s*\{([^}]+)\}",source[cend:cend+180])
        label=labelm.group(1) if labelm else ""
        end=cend+(labelm.end() if labelm else 0)
        num=labels.get(label,{}).get("number","?"); caption=md_inline(cm.group(1),labels,doc,links,root)
        rel=Path("04")/gm.group(1).strip(); url=REPO_URL+urllib.parse.quote(rel.as_posix(),safe="/-._~")
        fm=re.search(r"\\fuentefigura(?:\s*\[([^]]*)\])?",source[end:end+160])
        src_line="\n\nFuente: "+(fm.group(1) or "elaboración propia")+"." if fm else ""
        replacement=f"**Figura {num} — {caption}**\n\n![{caption}]({url}){src_line}"+(f'\n\n<a id="{label}"></a>' if label else "")
        source=source[:start]+replacement+source[end:]; cursor=start+len(replacement)
    # tablalafrox custom command is title,label,column spec,header followed by rows.
    pattern=r"\\begin\{tablalafrox\}\s*\{([^{}]*)\}\s*\{([^{}]*)\}\s*\{[^{}]*\}\s*\{(.*?)\}(.*?)\\end\{tablalafrox\}"
    def custom_table(m):
        label=m.group(2); return "\n\n"+table_md(m.group(4),m.group(1),labels.get(label,{}).get("number","?"),label,labels,doc,links,root)+"\n\n"
    source=re.sub(pattern,custom_table,source,flags=re.S)
    for env in ("longtable","tabularx","tabular"):
        pat=r"\\begin\{"+env+r"\}(?:\[[^]]*\])?(?:\{[^{}]*\}){0,2}(.*?)\\end\{"+env+r"\}"
        source=re.sub(pat,lambda m:"\n\n"+table_md(m.group(1),"", "?", "",labels,doc,links,root)+"\n\n",source,flags=re.S)
    # Headings: use the compiled TOC entry sequence as numbering authority.
    normtitle=lambda x:re.sub(r"\s+"," ",plain(x).replace("—","-").replace("–","-").replace("--","-")).strip().casefold()
    toc_by_title={normtitle(t): (lev,num,t) for lev,num,t in toc}
    for cmd,level in (("chapter",1),("section",2),("subsection",3),("subsubsection",4),("paragraph",5)):
        pat=r"\\"+cmd+r"\*?\s*\{([^{}]*)\}"
        def heading(m):
            title=md_inline(m.group(1),labels,doc,links,root)
            hit=toc_by_title.get(normtitle(m.group(1)))
            if not hit: return "\n\n**"+title+"**\n\n"
            n=hit[1]
            h="#"*level+" "+((n+" ") if n else "")+title
            return "\n\n"+h+"\n\n"
        source=re.sub(pat,heading,source)
    source=re.sub(r"\\label\s*\{([^}]+)\}",lambda m:f'<a id="{m.group(1)}"></a>',source)
    # Render visible residual plain text and references/citations.
    source=re.sub(r"\\(ref|autoref|cref|Cref|pageref)\*?\s*\{([^}]+)\}",lambda m:md_inline("\\"+m.group(1)+"{"+m.group(2)+"}",labels,doc,links,root),source)
    source=re.sub(r"\\cite(?:\[[^]]*\]){0,2}\s*\{([^}]+)\}",lambda m:"("+m.group(1).replace(";",", ")+")",source)
    source=re.sub(r"\\begin\{(itemize|enumerate|description)\}|\\end\{(itemize|enumerate|description)\}","\n",source)
    source=re.sub(r"\\item(?:\[[^]]*\])?\s*", "\n- ",source)
    # Remove control-only environments and format declarations. Strip comments before this point.
    source=re.sub(r"\\begin\{[^}]+\}(?:\[[^]]*\])?|\\end\{[^}]+\}","",source)
    source=re.sub(r"\\(addcontentsline|markboth|setcounter|addtocounter|renewcommand|providecommand|captionsetup|label|phantomsection|centering|raggedright|small|footnotesize|scriptsize|normalsize|LFXcuerpotabla|LFXcuerpofigura|intersemibold|cab|fuente[A-Za-z]+)\*?(?:\[[^]]*\])?\s*(?:\{[^{}]*\}){1,3}","",source)
    source=md_inline(source,labels,doc,links,root)
    source=source.replace("Anexo / página","Anexo / referencia").replace("muestra la página de inicio","identifica el anexo de inicio")
    source=re.sub(r"\n\s*\n\s*\n+","\n\n",source)
    # TOC-based headings and usable document index.
    heads=re.findall(r"^(#{1,4}) (.+)$",source,re.M)
    index="\n".join(f"- [{t}](#{slug(t)})" for _,t in heads)
    return source.strip(),index

def slug(s):
    s=s.lower(); s=re.sub(r"[^\w\s-]","",s,flags=re.UNICODE); return re.sub(r"[\s]+","-",s).strip("-")

def main():
    ap=argparse.ArgumentParser(); ap.add_argument("--salida",required=True); a=ap.parse_args()
    root=Path(__file__).resolve().parents[2]; build=root/"entrega"/"_build"; dest=Path(a.salida).resolve(); dest.mkdir(parents=True,exist_ok=True)
    docs=[("cuerpo","main.tex","LAFROX-Subdocumento4","# LafroX — Subdocumento 4"),("anexos","04/anexos_logica.tex","LAFROX-Subdocumento4-Anexos","# LafroX — Anexos del Subdocumento 4"),("t11","04/formulario_T11.tex","LAFROX-Formulario-T-11","# LafroX — Formulario T-11")]
    all_labels={d:aux_labels(build,d) for d in [x[2] for x in docs]}
    labels={k:v for x in all_labels.values() for k,v in x.items()}; owners={k:d[0] for d in docs for k in all_labels[d[2]]}
    names=["LAFROX-Subdocumento4.md","LAFROX-Subdocumento4-Anexos.md","LAFROX-Formulario-T-11.md"]
    nav=f"[Cuerpo]({names[0]}) · [Anexos]({names[1]}) · [T-11]({names[2]})"
    for doc,entry,stem,title in docs:
        src=expand(root/entry); toc=toc_entries(build,stem); body,index=convert(src,doc,stem,toc,labels,owners,root)
        if doc == "cuerpo":
            # Every compiled list-of-figures entry gets a Markdown figure block.
            # TikZ figures have no committed image asset, so their rendered title
            # remains represented, while raster/PDF assets use the pinned raw URL.
            additions=[]
            for number,ftitle in lof_entries(build,stem):
                if re.search(r"^\s*\*\*Figura\s+"+re.escape(number)+r"\s+—",body,re.M): continue
                label=next((k for k,v in all_labels[stem].items() if k.startswith("fig:") and v["number"]==number),"")
                image_path=""
                if label:
                    lm=re.search(r"\\label\s*\{"+re.escape(label)+r"\}",src)
                    if lm:
                        figure_start=max(src.rfind(r"\begin{figure}",0,lm.start()),src.rfind(r"\begin{figure*}",0,lm.start()))
                        prev=list(re.finditer(r"\\includegraphics(?:\[[^]]*\])?\s*\{([^}]+)\}",src[max(0,figure_start):lm.start()]))
                        if prev: image_path=prev[-1].group(1).strip()
                title_md=md_inline(ftitle,labels,doc,owners,root)
                block=f"**Figura {number} — {title_md}**"
                if image_path:
                    rel=Path("04")/image_path
                    if (root/rel).is_file(): block+=f"\n\n![{title_md}]({REPO_URL+urllib.parse.quote(rel.as_posix(),safe='/-._~')})"
                block+="\n\nFuente: elaboración propia."
                if label: block+=f'\n\n<a id="{label}"></a>'
                additions.append(block)
            if additions: body += "\n\n"+"\n\n".join(additions)
        text=title+"\n\n"+nav+"\n\n## Índice\n\n"+index+"\n\n"+body+"\n"
        (dest/names[[x[0] for x in docs].index(doc)]).write_text(text,encoding="utf-8")
    print(f"Generados 3 documentos desde {root} en {dest}")

if __name__=="__main__": main()
