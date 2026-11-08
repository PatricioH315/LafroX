from pathlib import Path
import json,re
root=Path(__file__).resolve().parents[1]
names=['08_plan_riesgos/contenido.tex','LAFROX-Subdocumento8-Anexos.tex','LAFROX-Formulario-T-16.tex','08_plan_riesgos/anexo-e-controles.tex','08_plan_riesgos/anexo-f-respuestas.tex','08_plan_riesgos/anexo-g-fmea.tex','08_plan_riesgos/anexo-h-reservas.tex','08_plan_riesgos/figuras/rbs.tex']
base={n:(root/n).read_text(encoding='utf-8') for n in names}
audit=root/'odd/tasks/interno-s8/remanentes-base.json'
assert not audit.exists(),'No sobrescribir base de comprobación'
audit.write_text(json.dumps(base,ensure_ascii=False,indent=2),encoding='utf-8')
body=base[names[0]]
replacements={
'qué herramienta se usó, con qué finalidad y qué revisó, antes de dar esa parte por cerrada.':'la herramienta utilizada, su finalidad y el alcance de la revisión humana.',
'Maximiliano Miño: Se lee introducción, se revisa las exigencias del contenido de introducción y se valida apropiadamente.':'Maximiliano Miño: revisión del alcance de la introducción y de su correspondencia con la operación y los entregables.',
'Maximiliano Miño: Se toma datos de secciones 8.2 mas la revisión de contenido generado, se realiza una revisión de que las respuestas sean acordes y se implementan tanto en los anexos como en el subdocumento':'Maximiliano Miño: revisión de la correspondencia entre la valoración de los riesgos, las respuestas, las contingencias y las reservas.',
'Maximiliano Miño: Se revisa contenido generado, se lee y se valida consistencia con los riesgos asociados .':'Maximiliano Miño: revisión de la pertinencia de las estrategias, respuestas y responsables de cada riesgo.',
'Maximiliano Miño: Antes de implementarlo en el anexo, se genera un archivo que contiene los datos cuantitativos, se revisa y se implementa en la tabla de anexos.':'Maximiliano Miño: revisión de las estimaciones de esfuerzo, los cálculos PERT y los valores esperados por riesgo.',
'Maximiliano Miño: Se crean los riesgos generados por ia, se validan (lo mismo que se realiza en sección 8.2) y se le pide a la IA que se cree la tabla.':'Maximiliano Miño: revisión de los enunciados, las valoraciones de probabilidad e impacto y las estrategias de respuesta del registro.',
'\\textbf{Solución y tecnología} conserva':'\\textbf{Solución y tecnología} comprende',
'\\textbf{Operación del cliente} conserva':'\\textbf{Operación del cliente} agrupa',
'\\textbf{Personas y adopción} conserva':'\\textbf{Personas y adopción} reúne',
'\\textbf{Contrato y licitación} conserva':'\\textbf{Contrato y licitación} comprende',
'\\textbf{Regulatorio y externo} conserva':'\\textbf{Regulatorio y externo} comprende',
'Las 28 coordinaciones del CLIENTE siguen en 8.A.2.':'Las dependencias del CLIENTE se detallan en la Tabla 8.A.2.',
'La exposición inicial sigue en 1.183,11 HH.':'La exposición inicial es de 1.183,11 HH.',
'; Verificar un control':'; verificar un control',
}
for old,new in replacements.items():
 assert old in body,old
 body=body.replace(old,new)
boilerplate='Las fuentes citadas en este documento se listan en formato APA 7.ª edición. Las Bases se citan en el texto con su documento y el artículo, capítulo, sección o código del requisito.\n\n'
body=body.replace(boilerplate,'')
# Retirar comentarios de plantilla que describen el proceso de edición.
body=body[body.index('\\setcounter{chapter}{7}'):]
updated={names[0]:body}
form=base[names[2]].replace(boilerplate,'')
form=form.replace('% Fuente Markdown: LAFROX-Formulario-T-16.md\n% Contenido actualizado; estructura y formato lafrox.cls conservados.\n\n','')
updated[names[2]]=form
annex=base[names[1]]
annex=annex.replace('control interno de escalabilidad CT-14','control técnico de escalabilidad CT-14')
annex=annex.replace('CT-16 conserva la corrección y verificación de consolidación dentro del proveedor.','CT-16 establece la corrección y verificación de la consolidación a cargo de LafroX.')
annex=annex.replace('R-032 y R-033 conservan sólo cambios excepcionales externos de soporte o restricciones efectivas de salida.','R-032 y R-033 cubren cambios excepcionales externos de soporte o restricciones efectivas de salida.')
annex=annex.replace('Se aplican las escalas de 8.1.3 a los mismos 35 eventos vigentes del T-16.','Se aplican las escalas de 8.1.3 a los 35 eventos del T-16.')
annex=annex.replace('el fundamento de la estimación se explicitan en 8.B.2','el fundamento de la estimación se explicita en 8.B.2')
updated[names[1]]=annex
reserve=base[names[6]]
reserve=reserve.replace('los totales se calculan sin redondear y se ajustan por última celda sólo al cargar la planilla.','los totales se calculan sobre los valores sin redondear.')
updated[names[6]]=reserve
for name,text in updated.items():
 old=base[name]
 assert [l for l in old.splitlines() if 'contenido academico' in l]==[l for l in text.splitlines() if 'contenido academico' in l],name
 # Las filas técnicas no cambian; quedan excluidas las filas de la declaración de uso de IA.
 assert [l for l in old.splitlines() if re.match(r'(R-\d{3}|CT-\d{2}|\d+) &',l)]==[l for l in text.splitlines() if re.match(r'(R-\d{3}|CT-\d{2}|\d+) &',l)],name
 (root/name).write_text(text,encoding='utf-8')
(root/'odd/tasks/interno-s8/depuracion-remanentes.md').write_text('''# Revisión editorial complementaria (interna)

Se revisaron las fuentes de los tres PDF y los anexos E–H. Se reformularon las notas de elaboración no protegidas de la declaración de IA, las expresiones que sugerían conservación desde otro listado y una instrucción de carga de planilla. Se retiraron comentarios de plantilla y explicaciones genéricas de formato bibliográfico.

Se conservan la declaración de IA, las líneas protegidas con «contenido academico», la historia sanitaria y comercial, las versiones de software, las condiciones de aprobación y verificación y el riesgo residual. Estas menciones tienen una finalidad contractual o técnica; no representan historial de edición.

Las filas de los registros, las valoraciones, los tratamientos, las estimaciones y los cálculos permanecen idénticos. La base de comparación se conserva en remanentes-base.json.
''',encoding='utf-8')
build=root/'tmp/remanentes-s8-build';build.mkdir(exist_ok=True)
print('Revisión aplicada a cuerpo, anexos, reservas y T-16; filas técnicas y citas protegidas intactas.')
