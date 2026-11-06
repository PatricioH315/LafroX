from pathlib import Path
import json,re,hashlib
r=Path(__file__).resolve().parents[1]
baseline=json.loads((r/'tmp/tarea4-baseline.json').read_text(encoding='utf-8'))
old=baseline['original'];now={p:(r/p).read_text(encoding='utf-8') for p in old}
form='LAFROX-Formulario-T-16.tex';ann='LAFROX-Subdocumento8-Anexos.tex';body='08_plan_riesgos/contenido.tex'
def registry(s):return {l.split(' & ')[0]:l.split(' & ') for l in s.splitlines() if re.match(r'R-\d{3} &',l)}
prev,current=registry(old[form]),registry(now[form])
assert len(current)==40 and current.keys()==prev.keys()
changed=set()
for rid,c in current.items():
 assert c[:6]==prev[rid][:6] and c[7:]==prev[rid][7:],rid
 if c[6]!=prev[rid][6]:changed.add(rid)
assert changed=={'R-016','R-018','R-019','R-034'}
first={}
for l in now[ann].splitlines():
 if re.match(r'R-\d{3} &',l) and len(c:=l.split(' & '))==4:first[c[0]]=c
for rid in changed:
 expected=current[rid][6]+(' Evidencia y detalle: Tabla 8.A.2.' if rid in {'R-016','R-018'} else '')
 assert first[rid][2]==expected,rid
for p in old:
 assert [l for l in old[p].splitlines() if 'contenido academico' in l]==[l for l in now[p].splitlines() if 'contenido academico' in l]
def bc(s):
 s=s[s.index('\\section{Anexo 8.B:'):]
 endpoint=s.index('\\section{Anexo 8.D:') if '\\section{Anexo 8.D:' in s else s.index('\\section*{Referencias}')
 return s[:endpoint].strip().removesuffix('\\clearpage').strip()
assert bc(old[ann])==bc(now[ann]),'Contenido de B/C alterado'
trace=[l.split(' & ') for l in now[ann].splitlines() if re.match(r'TR-\d{2} &',l)]
gaps=[l.split(' & ') for l in now[ann].splitlines() if re.match(r'B-S[47]-\d{2} &',l)]
assert len(trace)==14 and all(len(c)==5 and all(x.strip() for x in c) for c in trace)
assert len(gaps)==4 and all(len(c)==5 and all(x.strip() for x in c) for c in gaps)
assert {c[0] for c in gaps}=={'B-S4-01','B-S4-02','B-S4-03','B-S7-01'}
assert not re.search(r'^R-0(4[1-9]|[5-9]\d) &',now[form],re.M)
for tok in ['11--15','11--12','13--15','70\\%','100','IMP','DAT']:assert tok in current['R-034'][6]
for tok in ['15 min','30 min']:assert tok in current['R-018'][6]
for tok in ['Starlink','Concepción','Los Ángeles','30 s','3 h']:assert tok in current['R-019'][6]
for tok in ['75 min','AL-OFF-01','AL-DTE-01','AL-DR-01','AL-STOCK-01']:assert tok in now[ann]+now[body]
assert '85 minutos' not in now[body]
assert 'rotación anual del 38\\%' in now[ann] and 'no p0' in now[ann]
assert '7.1.2' in now[ann] and '13--56' in now[ann] and '22:00--06:00' in now[ann]
base=r.parent/'Informe propuesta tecnica/Informe_2_LafroX'
for p,h in baseline['source_hashes'].items():assert hashlib.sha256((base/p).read_bytes()).hexdigest()==h,p
print('OK: 14 cruces, 4 brechas únicas y fuentes S4/S7/S13/T14/T15 intactas.')
print('OK: sólo 4 respuestas ajustadas y sincronizadas; 40 eventos y valoraciones conservados; anexos B/C y citas protegidas intactos.')
print('OK: paquete/piloto R-034, autorización 15/30 min, enlaces por sitio, pruebas diferenciadas y rotación sin duplicación.')
