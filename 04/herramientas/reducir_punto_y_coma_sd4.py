"""Conservative punctuation reduction in active SD4 sources and their MD mirror."""
from pathlib import Path
import argparse, importlib.util, json, re, sys
sys.dont_write_bytecode=True
ROOT=Path(__file__).resolve().parents[2]
MD=ROOT.parent/'LafroX-alvaro-md'
QA=ROOT/'entrega/_build/qa_puntuacion_sd4'
SPEC=importlib.util.spec_from_file_location('tex2md',ROOT/'00/herramientas/tex2md.py')
conv=importlib.util.module_from_spec(SPEC);SPEC.loader.exec_module(conv)
SOURCE=re.compile(r'Bases(?: Técnicas| Administrativas)|Amazon Web Services|\bAWS\b|\bNIST\b|\bISO\b|International Organization|OWASP|Servicio de Impuestos|\bSII\b|LafroX,|\bAngular,|\bLaravel,|\bPHP,|\bPostgreSQL,|\bRabbitMQ,|\bW3C\b|World Wide Web|\bLey N',re.I)
VERB=re.compile(r'\b(?:es|son|sea|será|serán|se|mantiene|mantienen|conserva|conservan|usa|usan|utiliza|utilizan|permite|permiten|requiere|requieren|tiene|tienen|recibe|reciben|incluye|incluyen|ejecuta|ejecutan|queda|quedan|puede|pueden|debe|deben|atiende|atienden|alcanza|alojan|aloja|registra|registran|proporciona|emite|sigue|siguen|garantiza|procesa|define|acredita|presenta|representa|evita|contiene|sincroniza|publica|cumple|desarrolla|corresponde|corresponden|cubren|cubre|activa|captura|lee|calcula|sostiene|fija|verifica|traduce|entrega|enlaza|orienta|trabaja|opera|trabajan|operan|protege|protegen|informa|crece|crecen)\b',re.I)
VERB=re.compile(r'(?:'+VERB.pattern+r'|\b(?:valida|validan|persiste|recoge|obtiene|obtienen|exige|descarga|envía|suma|suman|crea|crean|consolida|antecede|declara|muestra|representan|aplica|dispone)\b)',re.I)
COMPLEX=('El identificador único del evento se denomina','El perfil local de bodega se identifica','STRIDE se aplica por módulo','Las integraciones internas heredan los controles','La tabla de carga es:','Broker = 0,5','Pruebas de contrato, CR-02/03')

def words(s):
    return re.findall(r'\w+',s.casefold())

def plain(s):
    s=re.sub(r'\[([^]]+)\]\([^)]*\)',r'\1',s)
    s=re.sub(r'\\(?:textbf|textit|emph|texttt|cab)\{([^{}]*)\}',r'\1',s)
    return s.replace('**','').replace('`','')

def cap(s):
    # Code, UUIDs, resource names and macro arguments remain case-sensitive.
    m=re.match(r'(\s*(?:\*\*|\*)?(?:\\(?:textbf|textit|emph)\{)?)([a-záéíóúüñ]+)(?=\s|[,.:}]|$)',s)
    if not m:return s
    word=m[2]
    if word in {'outbox','peak','wms','erp','shipper','shippers','sa','us'}:return s
    return s[:m.start(2)]+word[0].upper()+word[1:]+s[m.end(2):]

def transform(line,tex=False,tikz=False):
    if not ';' in line:return line,[]
    if any(marker in plain(line) for marker in COMPLEX):return line,[]
    semis=[m.start() for m in re.finditer(';',line)]
    table=(bool(re.search(r'(?<!\\)&',line)) if tex else line.lstrip().startswith('|'))
    separators=[m.start() for m in re.finditer(r'(?<!\\)&' if tex else r'\|',line)] if table else []
    operations=[]
    for pos in semis:
        if tex and tikz and pos==len(line.rstrip())-1:continue
        if re.search(r'&(?:[a-zA-Z]+|#\w+)$',line[:pos]):continue
        stack=[]
        for i,ch in enumerate(line[:pos]):
            if ch=='(':stack.append(i)
            elif ch==')' and stack:stack.pop()
        lo=max([x for x in separators if x<pos]+[-1])+1
        hi=min([x for x in separators if x>pos]+[len(line)])
        left=plain(line[lo:pos].rsplit(';',1)[-1]).strip()
        right=plain(line[pos+1:hi].split(';',1)[0]).strip()
        reason='frases relacionadas'
        replacement='.'
        if stack:
            start=stack[-1];end=line.find(')',pos)
            group=line[start+1:end if end>=0 else hi]
            before=group[:pos-start-1];after=group[pos-start:].split(';',1)[0]
            # Keep the separator between distinct cited works or between
            # complete requirement/source pairs, rather than between a code
            # and its own source/localizer.
            left=plain(before.rsplit(';',1)[-1]).strip()
            right=plain(after).strip()
            if SOURCE.search(left) and SOURCE.search(right):continue
            if SOURCE.search(before) and re.match(r'\s*(?:RT|RF|RNF)-',after):continue
            if SOURCE.search(before) and re.match(r'\s*(?:Anexo|sección|apartado|Tabla|Figura)',after,re.I):continue
            replacement=',';reason='componentes de una referencia o enumeración parentética'
        elif re.match(r'(?:el\s+4-|los\s+4-|y\s+el\s+4-)',right,re.I):
            continue # Complex catalogue with internal commas and ellipses.
        elif re.match(r'\s*(?:\*\*|\\textbf\{)(?:Componentes|Dónde corre|Escala por|Región)',line[pos+1:],re.I):
            replacement='.';reason='campos rotulados separados'
        elif not VERB.search(right) and not VERB.search(left):
            if ',' in left and ',' in right:continue
            replacement=',';reason='elementos nominales simples'
        elif table and not VERB.search(right):
            if ',' in left and ',' in right:continue
            replacement=',';reason='atributos de una celda'
        operations.append((pos,replacement,reason))
    result=line
    # Moving from right to left preserves the original positions.
    for pos,replacement,reason in reversed(operations):
        tail=result[pos+1:]
        if replacement=='.':tail=cap(tail)
        result=result[:pos]+replacement+tail
    assert words(line)==words(result),('word changes',line,result)
    return result,operations

def active(path,seen):
    path=path.resolve()
    if path in seen or not path.is_file():return
    seen.add(path)
    s=conv.clean_comments(path.read_text(encoding='utf-8-sig'))
    for m in re.finditer(r'\\(import|subimport|input|include|parte)(?![A-Za-z@])',s):
        name=m[1];pos=m.end()
        if name in ('import','subimport'):
            folder,pos=conv.arg(s,pos);target,pos=conv.arg(s,pos);candidate=path.parent/folder/target
        else:
            target,pos=conv.arg(s,pos);candidate=path.parent/target
        if candidate.suffix!='.tex':candidate=candidate.with_suffix('.tex')
        active(candidate,seen)

def save(path,before,after):
    if before==after:return
    dest=QA/'antes'/path.relative_to(ROOT.parent)
    dest.parent.mkdir(parents=True,exist_ok=True)
    if not dest.exists():dest.write_bytes(path.read_bytes())
    path.write_text(after,encoding='utf-8',newline='\n')

def main():
    parser=argparse.ArgumentParser();parser.add_argument('--apply',action='store_true');args=parser.parse_args()
    paths=set()
    for entry in ['main.tex','04/anexos_logica.tex','04/formulario_T11.tex']:active(ROOT/entry,paths)
    paths={p for p in paths if '/04/' in p.as_posix() and p.suffix=='.tex'}
    paths.update((MD/'04_arquitectura').glob('*.md'))
    reports=[]
    for p in sorted(paths):
        before=p.read_text(encoding='utf-8-sig');lines=[];edits=[];tikz=False
        for n,line in enumerate(before.splitlines(),1):
            if r'\begin{tikzpicture}' in line:tikz=True
            # Do not mutate comments, URLs, labels or structural commands.
            if p.suffix=='.tex' and (line.lstrip().startswith('%') or re.match(r'\s*\\(?:url|href|label|newcommand|renewcommand|draw|path|fill|clip)\b',line)):
                new,ops=line,[]
            else:
                cut=re.search(r'(?<!\\)%',line) if p.suffix=='.tex' else None
                visible=line[:cut.start()] if cut else line
                new,ops=transform(visible,p.suffix=='.tex',tikz)
                if cut:new+=line[cut.start():]
            if r'\end{tikzpicture}' in line:tikz=False
            lines.append(new)
            if ops:edits.append({'line':n,'before':line,'after':new,'replaced':len(ops)})
        after='\n'.join(lines)+'\n'
        assert words(before)==words(after),p
        if edits:
            reports.append({'path':str(p.relative_to(ROOT.parent)),'before_count':before.count(';'),'after_count':after.count(';'),'edits':edits})
            if args.apply:save(p,before,after)
    QA.mkdir(parents=True,exist_ok=True)
    (QA/('aplicacion.json' if args.apply else 'propuesta.json')).write_text(json.dumps(reports,ensure_ascii=False,indent=2),encoding='utf-8',newline='\n')
    mdrows=[r for r in reports if r['path'].endswith('.md')]
    print(json.dumps({'apply':args.apply,'files':len(reports),'markdown':[{'file':r['path'],'before':r['before_count'],'after':r['after_count']} for r in mdrows]},ensure_ascii=False))
    for r in mdrows:
        print(json.dumps({'sample':r['path'],'rows':r['edits'][:7]},ensure_ascii=False))

if __name__=='__main__':main()
