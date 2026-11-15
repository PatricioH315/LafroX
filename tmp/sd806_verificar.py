from pathlib import Path
import subprocess,re,json,hashlib
r=Path(__file__).resolve().parents[1]
read=lambda p:(r/p).read_text(encoding='utf-8')
git=lambda *args:subprocess.check_output(['git',*args],cwd=r,text=True,encoding='utf-8')
assert git('branch','--show-current').strip()=='Lafrox_Subdocumento_8_Latex_Revision'
manifest=json.loads(read('tmp/sd806-backup/manifest.json'))
unchanged=['08_plan_riesgos/anexo-f-respuestas.tex','08_plan_riesgos/anexo-g-fmea.tex','08_plan_riesgos/anexo-h-reservas.tex',
           '08_plan_riesgos/figuras/rbs.tex','08_plan_riesgos/figuras/LafroX_RBS_36_riesgos_S8_v4.drawio','08_plan_riesgos/figuras/LafroX_RBS_36_riesgos_S8_v4.pdf']
for p in unchanged:assert hashlib.sha256((r/p).read_bytes()).hexdigest()==manifest[p],p
for p in ['LAFROX-Subdocumento8-Anexos.tex','LAFROX-Formulario-T-16.tex']:
    row=lambda s:[l for l in s.splitlines() if re.match(r'R-\d{3}( /[^&]*)? &',l)]
    assert row(read(p))==row(read('tmp/sd806-backup/'+p)),p
e=read('08_plan_riesgos/anexo-e-controles.tex')
assert len(re.findall(r'^CT-\d{2} &',e,re.M))==15
assert 'Al excluir del diseño previsto el control de identidad sin conexión' not in e
assert 'no a pruebas habilitantes del CT-03 vigente' not in e
assert 'el antiguo CT-15 de identidad fue retirado' not in e
for phrase in ['26 h','25 h','8 y 16 h','14,5 h','16 h','hora confiable','cuarentena','PIN y secretos']:
    assert phrase in e,phrase
a=read('LAFROX-Subdocumento8-Anexos.tex')
assert a.count('{tab:sd806-correspondencia}')==1
for prefix in ['ERP / R-034 &','Stock / CT-15 &','Identidad / CT-03 &']:
    assert prefix in a,prefix
assert 'SD8-06 permanece parcial' in a
for branch,files in {
 'LafroX-Subdoc4-LateX-corrigiendo':['04/anexos/logica/partes/14_anexo_4_1_m_verificacion_de_continuidad_logica.tex','04/anexos/logica/partes/25_anexo_4_1_v_aceptacion_y_dependencias.tex'],
 'LafroX-Subdoc9-LateX-corrigiendo':['SD9_v_nueva/T13/contenido.tex','SD9_v_nueva/T17/contenido.tex']}.items():
    text='\n'.join(git('show',branch+':'+p) for p in files)
    for token in ['R-034','CT-15','CT-03','AL-ID-01','AL-STOCK-01','AL-DTE-01','AL-DR-01','3.8.5/3.9.4']:
        assert token in text,(branch,token)
    names=git('diff-tree','--no-commit-id','--name-only','-r',branch).splitlines()
    assert all(not p.startswith('tmp/') for p in names),branch
print('SD8-04/05 preservados: fichas, FMEA, reservas, RBS y filas de los 36 riesgos intactos.')
print('15 controles conservados; CT-03 conectado/local; CT-15 stock; correspondencia recíproca en SD4/SD9.')
print('Evidencia de implementación, ejecución y aceptación declarada pendiente, sin resultados fabricados.')
