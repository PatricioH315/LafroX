from pathlib import Path
import json,re
root=Path(__file__).resolve().parents[1]
snap=json.loads((root/'tmp/tarea3-baseline.json').read_text(encoding='utf-8'))
original={k.replace(chr(92),'/'):v for k,v in snap['original'].items()};expected=set(snap['client_ids'])
texts={p:(root/p).read_text(encoding='utf-8') for p in original}
f='LAFROX-Formulario-T-16.tex';a='LAFROX-Subdocumento8-Anexos.tex'
def rows(s):return {l.split(' & ')[0]:l.split(' & ') for l in s.splitlines() if re.match(r'R-\d{3} &',l)}
before=rows(original[f]);after=rows(texts[f])
assert len(after)==40 and before.keys()==after.keys()
changed=set()
for rid,c in after.items():
 assert c[:6]==before[rid][:6] and c[7:]==before[rid][7:],rid
 if c[6]!=before[rid][6]:changed.add(rid)
assert changed==expected
ann=texts[a];dep=ann[ann.index('\\begin{tablalafrox}{Contrapartes, solicitudes'):ann.index('\\section{Anexo 8.B:')]
deprows=[l.split(' & ') for l in dep.splitlines() if re.match(r'R-\d{3} /',l)]
assert len(deprows)==20
assert {c[0].split(' / ')[0] for c in deprows}==expected
for c in deprows:
 assert len(c)==5 and all(x.strip() for x in c)
 assert any(x in c[3] for x in ['mes','D-5','despacho','cambio','actividad'])
 assert any(x in c[4].lower() for x in ['escalar','jp notifica','notificar inmediatamente'])
 # Every summary in the form is exactly reproduced in the first response matrix.
 rid=c[0].split(' / ')[0]
 first=next(l for l in ann.splitlines() if l.startswith(rid+' &')).split(' & ')
 assert first[2]==after[rid][6]+' Evidencia y detalle: Tabla 8.A.2.'
for p in original:
 old=original[p];new=texts[p]
 assert [l for l in old.splitlines() if 'contenido academico' in l]==[l for l in new.splitlines() if 'contenido academico' in l]
if True:
 old=original[a][original[a].index('\\section{Anexo 8.B:'):]
 new=texts[a][texts[a].index('\\section{Anexo 8.B:'):]
 assert old==new,'Anexos B/C alterados'
assert 'diez días hábiles de revisión y diez de subsanación' in texts['08_plan_riesgos/contenido.tex']
assert 'instancia extraordinaria al Comité Ejecutivo' in texts['08_plan_riesgos/contenido.tex']
assert 'no aprueba datos, cambios' in texts['08_plan_riesgos/contenido.tex']
print('OK: 20 dependencias con cinco campos completos, consistencia exacta de respuestas entre T-16 y 8.A.1.')
print('OK: 40 riesgos y valoraciones conservados; anexos 8.B/8.C y citas protegidas intactos; protocolo y límites contractuales presentes.')
