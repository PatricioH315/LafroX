"""Edit text glyphs in vector PDFs, retaining drawing operations and geometry."""
from pathlib import Path
import json,re,sys
from pypdf import PdfReader,PdfWriter
from pypdf._cmap import get_encoding
from pypdf.generic import ByteStringObject, TextStringObject

ROOT=Path(__file__).resolve().parents[2]
MD=ROOT.parent/'LafroX-alvaro-md/04_arquitectura/LAFROX-Subdocumento4.md'
QA=ROOT/'entrega/_build/qa_puntuacion_sd4'
text=MD.read_text(encoding='utf-8')
targets=[]
for m in re.finditer(r'^\*\*Figura (\d+) — (.+)\*\*\n\n(?:!\[[^]]*\]|\[[^]]*\])\(([^)]+)\)',text,re.M):
    number=int(m[1]);url=m[3]
    if number not in [1,2,3,4,5,6,7,13,17,25,26]:continue
    path=ROOT/'04'/url.split('/04/',1)[1]
    targets.append((number,path))

def words(s):return re.findall(r'\w+',s.casefold())

records=[]
for number,path in targets:
    reader=PdfReader(path)
    original='\n'.join(p.extract_text() for p in reader.pages)
    assert original.count(';')==(2 if number==13 else 1),(number,original.count(';'))
    writer=PdfWriter();writer.clone_document_from_reader(reader)
    total=0;pending=False
    for page in writer.pages:
        fonts={}
        for name,obj in page['/Resources']['/Font'].items():
            encoding,cmap=get_encoding(obj.get_object())
            if encoding=='utf-16-be':
                lookup={k:v for k,v in cmap.items() if isinstance(k,str) and isinstance(v,str)}
                reverse={v:k for k,v in lookup.items()}
                fonts[name]=(encoding,lookup,reverse)
            else:
                lookup={chr(k):v for k,v in encoding.items()} if isinstance(encoding,dict) else {chr(i):bytes([i]).decode(encoding,errors='replace') for i in range(256)}
                reverse={v:k for k,v in lookup.items()};fonts[name]=('latin-1',lookup,reverse)
        content=page.get_contents();current=None
        def patch(value):
            global pending,total
            if not isinstance(value,(TextStringObject,ByteStringObject)):return value
            assert current in fonts,current
            encoding,lookup,reverse=fonts[current]
            raw=value.original_bytes if isinstance(value,TextStringObject) else bytes(value)
            codes=list(raw.decode(encoding))
            changed=False
            for i,code in enumerate(codes):
                char=lookup.get(code,code)
                if char==';':
                    assert '.' in reverse,(path,current,'period missing')
                    codes[i]=reverse['.'];changed=True;total+=1;pending=True
                elif pending and char.strip():
                    if char.isalpha() and char.islower():
                        assert char.upper() in reverse,(path,current,'uppercase missing',char)
                        codes[i]=reverse[char.upper()];changed=True
                    pending=False
            return ByteStringObject(''.join(codes).encode(encoding)) if changed else value
        for args,operator in content.operations:
            if operator==b'Tf':current=args[0]
            elif operator==b'Tj':args[0]=patch(args[0])
            elif operator==b'TJ':
                for i,value in enumerate(args[0]):args[0][i]=patch(value)
        page.replace_contents(content)
    assert total==original.count(';'),(path,total,original.count(';'))
    backup=QA/'antes'/path.relative_to(ROOT.parent)
    backup.parent.mkdir(parents=True,exist_ok=True)
    if not backup.exists():backup.write_bytes(path.read_bytes())
    with path.open('wb') as output:writer.write(output)
    after='\n'.join(p.extract_text() for p in PdfReader(path).pages)
    assert ';' not in after,path
    assert words(original)==words(after),(path,'word sequence changed')
    records.append({'figure':number,'path':str(path.relative_to(ROOT)),'replaced':total})

# Synchronize only literal text in the editable diagram sources. Styles,
# coordinates, routes and entities such as &#10; are kept byte-for-byte.
pairs=[
 ('integración; la etiqueta','integración. La etiqueta'),
 ('general; el apartado','general. El apartado'),
 ('eventos y datos; no es','eventos y datos. No es'),
 ('XML definitivo; los módulos','XML definitivo. Los módulos'),
 ('26 h; renovación','26 h. Renovación'),
 ('sus nombres; las relaciones','sus nombres. Las relaciones'),
 ('se conservan; no se asignan','se conservan. No se asignan'),
 ('PedidoConfirmado; M6','PedidoConfirmado. M6'),
 ('Propietarios y eventos; el detalle','Propietarios y eventos. El detalle'),
 ('cada región; datos locales durables','cada región. Datos locales durables'),
 ('recursos preparados; el outbox','recursos preparados. El outbox')]
for path in list((ROOT/'04/figuras/fuentes').glob('*.xml'))+[ROOT/'04/herramientas/red_legible_sd4.py']:
    before=path.read_text(encoding='utf-8-sig');after=before
    for old,new in pairs:after=after.replace(old,new)
    if before!=after:
        assert words(before)==words(after),path
        backup=QA/'antes'/path.relative_to(ROOT.parent)
        backup.parent.mkdir(parents=True,exist_ok=True)
        if not backup.exists():backup.write_bytes(path.read_bytes())
        path.write_text(after,encoding='utf-8',newline='\n')
(QA/'figuras.json').write_text(json.dumps(records,ensure_ascii=False,indent=2),encoding='utf-8',newline='\n')
print(json.dumps(records,ensure_ascii=False))
