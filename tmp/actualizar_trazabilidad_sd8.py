from pathlib import Path
import ast,runpy,re,json,hashlib

r=Path(__file__).resolve().parents[1]
folder=r/'Trazabilidad-Informe2'
script=folder/'generar_tablas.py'; table=folder/'partes/tablas.tex'
out=r/'tmp/trazabilidad-sd8';out.mkdir(parents=True,exist_ok=True)
base=table.read_text(encoding='utf-8')
(out/'tablas-antes.tex').write_text(base,encoding='utf-8')
(out/'generador-antes.py').write_bytes(script.read_bytes())
updates={
1:('El T-16 reúne 36 riesgos y 8.E.1 define 15 controles CT-01 a CT-15, con responsables y evidencia de cierre. CT-03 integra identidad conectada/local y CT-15 conserva stock. ERP, stock e identidad se sincronizan documentalmente con SD4/SD9; faltan implementación, eficacia y las restantes dependencias de diseño/prueba de SD4, SD9 y SD13.',
   'SD8, 8.2.1; SD8-Anexos, 8.D.3 y 8.E.1; T-16'),
3:('Se proyecta la valoración posterior de los 36 riesgos: 1 crítico, 4 altos, 20 medios y 11 bajos. p1 depende de ejecutar el tratamiento completo y verificar evidencia; sin ella se conserva la valoración inicial. No se acredita eficacia observada.',
   'SD8, 8.3.1; SD8-Anexos, 8.F.2; T-16, resumen residual'),
4:('R-002 permanece Crítica; R-006, R-029, R-030 y R-031, Altos. Se completan las cinco fichas y la matriz 8.F.2a con prueba, evidencia, verificador, disparador, plazo y decisión. Sólo evidencia satisfactoria permite proponer reevaluación; resultado insuficiente o fallido mantiene el bloqueo y exige corregir/repetir. Se distingue valoración inicial, objetivo condicionado y eficacia acreditada; se revisa suficiencia de HH sin duplicaciones. Falta acreditar eficacia y nivel manejable.',
   'SD8, 8.3.1; SD8-Anexos, 8.F.1, 8.F.2 y 8.F.2a; 8.G.1; T-16'),
5:('La matriz 8.D.2 coteja los diez temas: R-014, R-017 y R-028 a R-035, más R-036 por divergencia del perfil real de carga. R-036 es Medio (p0=p1=30 %, I=4, E=0,12), sin descuento por eficacia futura. CT-14 conserva el peak conocido, crecimiento comprometido y corrección del diseño a cargo de LafroX. Se actualizan RBS, análisis y reservas para 36 riesgos, sin duplicar HH. Cobertura documental completada; faltan validar el perfil, ejecutar pruebas y acreditar eficacia.',
   'SD8-Anexos, 8.D.2, 8.B.1–8.B.2, 8.E.1 (CT-14), 8.F y 8.H; T-16, R-036; SD8, Figura 8.1'),
6:('R-034 conserva la dependencia del ERP y CT-15 el stock con retención local durable y autoridad única. CT-03 incorpora identidad conectada/local conforme a SD4/SD9, sin renumerar controles. La matriz 8.D.3 enlaza diseño, protocolos, campañas, responsables y evidencia; SD4 y T-13/T-17 incorporan referencias recíprocas. Se conservan los 36 riesgos y sus valoraciones. Sincronización documental completada; faltan evidencia de implementación, resultados de ejecución y actas de aceptación.',
   'SD8-Anexos, 8.D.3 y 8.E.1; T-16, R-034; SD4, Anexos 4-M/4-V (Tabla 4-V.1); SD9, T-13, 7.5 y T-17, 3.1'),
9:('Las 36 fichas fijan responsables, perfiles, HH, plazo preventivo, actuación contingente y evidencia. La distribución mensual por perfil se propone en 8.H.3; requiere nivelación y autorización, no acredita capacidad comprometida ni ejecución.',
   'SD8-Anexos, 8.F.1 y 8.H.2–8.H.3'),
10:('Exposición inicial: 1.199,52 HH, redondeada al final; A=180,00 y p1H0=837,53 (p1C=142,00; p1L=695,53), total posterior 1.017,53 HH. Gestión: 160 HH propuestas fuera de línea base. Las 3.072 HH ya programadas protegen sólo E1, sin sumarlas otra vez a 202.108,62 HH; crédito inicial cero. Falta nivelar y autorizar en T-15.',
    'SD8, 8.3.2; SD8-Anexos, 8.B.1 y 8.H.1–8.H.3; cotejo S7, Tabla 7.4'),
12:('Se unifica la numeración, se usan tablas de cinco columnas y se corrige la fuente RT-20. La RBS se actualiza a 36 riesgos, conservando folio y firma; se mantiene la separación del pie para evitar su superposición.',
    'SD8, 8.1 a 8.3; Figura 8.1 (RBS)')}

source=script.read_text(encoding='utf-8')
tree=ast.parse(source)
assignment=next(n for n in tree.body if isinstance(n,ast.Assign) and any(isinstance(t,ast.Name) and t.id=='GRUPOS' for t in n.targets))
group=next(g for g in assignment.value.elts if isinstance(g.elts[1],ast.Constant) and g.elts[1].value=='SD8')
offsets=[0]
for line in source.splitlines(keepends=True):offsets.append(offsets[-1]+len(line))
# AST columns are UTF-8 byte offsets; convert them before slicing Unicode source.
lines=source.splitlines(keepends=True)
def pos(line,col):return offsets[line-1]+len(lines[line-1].encode('utf-8')[:col].decode('utf-8'))
edits=[]
for i,(response,section) in updates.items():
    row=group.elts[2].elts[i-1]
    for node,value in [(row.elts[2],response),(row.elts[3],section)]:
        edits.append((pos(node.lineno,node.col_offset),pos(node.end_lineno,node.end_col_offset),repr(value)))
for start,end,replacement in sorted(edits,reverse=True):source=source[:start]+replacement+source[end:]
script.write_text(source,encoding='utf-8',newline='\n')
ns=runpy.run_path(str(script));ns['main'](str(out/'generadas.tex'))
generated=(out/'generadas.tex').read_text(encoding='utf-8')
newrows={re.search(r'\\mbox\{(SD8-\d+)\}',line)[1]:line for line in generated.splitlines() if line.startswith(r'\mbox{SD8-')}
updated=[]
for line in base.splitlines():
    match=re.match(r'\\mbox\{SD8-(\d+)\}',line)
    if match and int(match[1]) in updates:
        line=newrows[f'SD8-{int(match[1]):02}']
    updated.append(line)
new='\n'.join(updated)+ ('\n' if base.endswith('\n') else '')
table.write_text(new,encoding='utf-8',newline='\n')
oldstates=re.findall(r'\\mbox\{([^}]+)\}.*?\\textbf\{([^}]+)\}',base)
newstates=re.findall(r'\\mbox\{([^}]+)\}.*?\\textbf\{([^}]+)\}',new)
assert oldstates==newstates and len(oldstates)==152
for old,line in zip(base.splitlines(),new.splitlines()):
    if old!=line:assert re.match(r'\\mbox\{SD8-(01|03|04|05|06|09|10|12)\}',line)
for name in ['tablas_sintesis.tex']:
    assert (out/'generadas_sintesis.tex').read_text(encoding='utf-8')==(folder/'partes'/name).read_text(encoding='utf-8')
print('Actualizadas 8 filas de SD8; restantes filas y 152 estados conservados. Síntesis sin cambios.')
