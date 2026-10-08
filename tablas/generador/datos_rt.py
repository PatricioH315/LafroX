from pathlib import Path
import re
def cargar():
    base=Path(__file__).resolve().parents[3]/"Bases"/"Bases_Tecnicas_Transversales.md"
    out=[]
    for line in base.read_text(encoding="utf8").splitlines():
        m=re.match(r"\|\s*\*\*(RT-\d\d\.\d\d)\*\*\s*\|(.*)\|\s*\*\*(.*?)\*\*\s*\|",line)
        if m: out.append(dict(id=m[1],desc=m[2].strip(),car=m[3]))
    assert out and len(out)==len({x['id'] for x in out})
    return out
