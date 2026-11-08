from pathlib import Path
import re,json,collections,hashlib
root=Path(__file__).resolve().parents[1]
before={n.replace('\\','/'):s for n,s in json.loads((root/'tmp/limpieza-s8-base.json').read_text(encoding='utf-8')).items()}
after={n:(root/n).read_text(encoding='utf-8') for n in before if (root/n).exists()}
def table(s,id):
 token='\\renewcommand{\\thetable}{'+id+'}'
 a=s.index(token);b=s.index('\\end{tablalafrox}',a)
 return [line for line in s[a:b].splitlines() if re.match(r'(R-\d{3}|\d+ &)',line)]
for n,s in after.items():
 assert [l for l in s.splitlines() if 'contenido academico' in l]==[l for l in before[n].splitlines() if 'contenido academico' in l],n
 assert not re.search(r'CI-\d|8\.I\.[12]|411,82|1\.594,93|1\.600|Informe 2|renumer|sincroniza(?:r|ción externa)|B-S[47]-|reclasificados|asuntos retirados|ID vigentes',s),n
for n in ['08_plan_riesgos/anexo-f-respuestas.tex','08_plan_riesgos/anexo-g-fmea.tex']:
 assert [l for l in before[n].splitlines() if l.startswith('R-')]==[l for l in after[n].splitlines() if l.startswith('R-')],n
n='08_plan_riesgos/figuras/rbs.tex';assert before[n]==after[n]
for id in ['8.1','8.5','8.6']:
 n='08_plan_riesgos/contenido.tex';assert table(before[n],id)==table(after[n],id),id
n='LAFROX-Subdocumento8-Anexos.tex'
for id in ['8.A.2','8.B.1','8.C.1']:
 assert table(before[n],id)==table(after[n],id),id
old=table(before[n],'8.A.1');new=table(after[n],'8.A.1');assert len(old)==len(new)==35
for a,b in zip(old,new):
 for suffix in [' Evidencia y detalle: Tabla 8.A.2.',' Evidencia y coordinación: Tabla 8.A.2.',' Plazos completos y HH: 8.F.1; residual: 8.F.2.']:
  a=a.replace(suffix,'')
 assert a==b,(a[:30],b[:30])
def nums(s):return re.findall(r'(?<![A-Za-z])\d+(?:[.,]\d+)?',s)
for a,b in zip(table(before[n],'8.B.2'),table(after[n],'8.B.2')):
 # Source column may lose the editorial report number; probability and O/M/P unchanged.
 for i,old in enumerate(['009','010','023','024','025','026','027','034','035','036','037','038','040','047','048','050'],1):
  a=a.replace('CI-'+old,f'CT-{i:02}')
 assert nums(' & '.join(a.split(' & ')[:4]))==nums(' & '.join(b.split(' & ')[:4]))
n='LAFROX-Formulario-T-16.tex'
for a,b in zip(table(before[n],'T-16.1'),table(after[n],'T-16.1')):
 assert a.replace(' Plazos, HH y contingencia: 8.F.1; residual proyectado: 8.F.2.','')==b
for id in ['T-16.1','T-16.2']:
 rows=table(after[n],id);assert [r.split(' & ')[0] for r in rows]==[f'R-{i:03}' for i in range(1,36)]
for a,b in zip(table(before[n],'T-16.2'),table(after[n],'T-16.2')):
 assert a.split(' & ')[:4]==b.split(' & ')[:4]
 assert a.split(' & ')[4]==b.split(' & ')[4].removesuffix(' \\\\')
n='08_plan_riesgos/anexo-h-reservas.tex'
for id in ['8.H.2','8.H.3']:assert table(before[n],id)==table(after[n],id)
n='08_plan_riesgos/anexo-e-controles.tex'
codes=re.findall(r'^(CT-\d{2}) &',after[n],re.M);assert codes==[f'CT-{i:02}' for i in range(1,17)]
for a,b in zip([l for l in before[n].splitlines() if l.startswith('CI-')],[l for l in after[n].splitlines() if l.startswith('CT-')]):
 assert nums(' & '.join(a.split(' & ')[2:]))==nums(' & '.join(b.split(' & ')[2:])),b[:20]
public='\n'.join(after.values())
assert set(re.findall(r'R-\d{3}',public))=={f'R-{i:03}' for i in range(1,36)}
assert '\\input{08_plan_riesgos/anexo-i-trazabilidad.tex}' not in public
assert (root/'odd/tasks/interno-s8/trazabilidad-y-equivalencias.tex').exists()
assert (root/'odd/tasks/interno-s8/matriz-cierre-s8.md').exists()
prior=json.loads((root/'tmp/cierre-s8-base.json').read_text(encoding='utf-8'))
for name,digest in prior['sources'].items():
 assert hashlib.sha256((root.parent/name).read_bytes()).hexdigest()==digest,name
report='Comprobado: 35 ID; 16 CT; igualdad de valoraciones, estimaciones, respuestas, FMEA, costo-beneficio, residual, distribución de HH y RBS; citas protegidas intactas. Material de coordinación fuera de publicación.'
(root/'tmp/limpieza-s8-build/verificacion.txt').write_text(report,encoding='utf-8')
print(report)
