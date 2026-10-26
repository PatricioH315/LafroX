"""Comprueba coherencia documental; no sustituye ensayos ni revisión humana.

Uso: python verificar_coherencia_frio.py --sd13 <worktree> --sd3 <worktree>
"""
import argparse
from collections import Counter
import hashlib
import json
import re
import subprocess
from pathlib import Path
import xml.etree.ElementTree as ET

from pypdf import PdfReader

parser = argparse.ArgumentParser()
parser.add_argument('--sd13', type=Path, required=True)
parser.add_argument('--sd3', type=Path, required=True)
args = parser.parse_args()
root4 = Path(__file__).resolve().parents[2]
root13 = args.sd13.resolve() / 'SD13_v_nueva'
root3 = args.sd3.resolve()
checks = []

def check(name, condition):
    checks.append({'comprobacion': name, 'resultado': bool(condition)})
    if not condition:
        raise AssertionError(name)

def text(path):
    return path.read_text(encoding='utf-8')

def git_blob(root, path):
    return subprocess.check_output(['git', '-C', str(root), 'show', 'HEAD:' + path])

def sha(data):
    return hashlib.sha256(data).hexdigest()

body13 = text(root13 / '13_innovaciones/contenido.tex')
t19 = text(root13 / 'T19/contenido.tex')
ann13 = text(root13 / '13_anexos/contenido.tex')
ann4 = text(root4 / '04/anexos/logica/partes/15_anexo_4_1_n_correspondencia_de_componentes_logicos.tex')
for label, data in [('SD13', body13), ('T19', t19), ('Anexo4N', ann4)]:
    check(label + ': volumetría vigente', '30.548' in data and '127.848' in data)
    check(label + ': kit y segundo evaluador', 'B-04' in data and 'B-08' in data and 'C-02' in data)
    check(label + ': dos caminos y persistencia', 'Iridium' in data and 'A2' in data)
    check(label + ': sin volumen anterior', '10.920' not in data)
check('No atribuir ingesta nueva al transporte SBD', '8.120' in body13 and 'no se suman' in body13)
check('Sin inventar cobertura durante pérdida simultánea', 'no se presenta como inmediato el aviso remoto' in body13)
check('Contrato térmico con compartimento e identidad', all(x in ann13 for x in ['SSCC','compartimento','productor/arranque/secuencia','B-02/B-04']))
check('Modelo no reemplaza seguridad ni FEFO', all(x in body13 for x in ['no libera una carga bloqueada','FEFO']) and bool(re.search(r'(?:no|ni) se deshabilita el segundo evaluador',body13,re.I)))

current = text(root3 / 'LAFROX-Formulario-T-12.tex')
previous = git_blob(root3, 'LAFROX-Formulario-T-12.tex').decode('utf-8')
pattern = r'^\s*(?:RF|RNF|RT)-[^ &]+\s*&.*$'
old_rows, new_rows = re.findall(pattern, previous, re.M), re.findall(pattern, current, re.M)
check('T12 conserva las 653 filas', len(old_rows) == len(new_rows) == 653)
delta = [(a,b) for a,b in zip(old_rows,new_rows) if a != b]
check('T12 solo cambia RT-26.01', len(delta) == 1 and delta[0][0].lstrip().startswith('RT-26.01 '))
check('T12 conserva la exigencia literal', delta[0][0].split('&')[1] == delta[0][1].split('&')[1])
check('T12 distingue cobertura documental de ensayos', 'no acredita ensayos ejecutados' in delta[0][1])
states = Counter(row.split('&')[2].strip() for row in new_rows)
check('T12 conserva estados restantes', states == {'Cumple':596,'Cumple parcialmente':35,'No cumple':22})

originals = [
    '04/figuras/logica/capas/ARQL-01_General_definitivo.pdf',
    '04/figuras/logica/capas/ARQL-22_Borde.pdf',
    '04/figuras/fisica/Arquitectura_Fisica_General.png',
]
for relative in originals:
    check('Original conservado: ' + relative, (root4/relative).read_bytes() == git_blob(root4, relative))
relative = 'SD13_v_nueva/13_innovaciones/diagramas/Fig_13-4_Recorrido_INN03.pdf'
check('Original INN03 conservado', (args.sd13/relative).read_bytes() == git_blob(args.sd13,relative))

for path in [root4/'04/figuras/fuentes/ARQL-01_General_frio_vigente.drawio',
             root4/'04/figuras/fuentes/Arquitectura-logica-frio-vigente.drawio',
             root4/'04/figuras/fuentes/Arquitectura_Fisica_General_frio_legible.drawio',
             root13/'13_innovaciones/diagramas/Fig_13-4_Recorrido_INN03_frio_vigente.drawio']:
    tree = ET.parse(path)
    check('Fuente vectorial válida: '+path.name, bool(tree.findall('.//mxCell')))

pdfs = [root4/'entrega/LAFROX-Subdocumento4.pdf',
        root4/'entrega/LAFROX-Subdocumento4-Anexos.pdf',
        root4/'entrega/LAFROX-Formulario-T-11.pdf',
        root13/'LAFROX-Subdocumento13.pdf', root13/'LAFROX-Subdocumento13-Anexos.pdf',
        root13/'LAFROX-Formulario-T-19.pdf', root3/'LAFROX-Formulario-T-12.pdf']
outputs = []
for path in pdfs:
    doc = PdfReader(path)
    check('PDF abierto sin contraseña: '+path.name, not doc.is_encrypted and bool(doc.pages))
    pages = [p.extract_text() or '' for p in doc.pages]
    check('PDF con texto seleccionable: '+path.name, all(bool(p.strip()) for p in pages))
    check('PDF con foliación correlativa: '+path.name,
          all(re.search(r'(?<!\d)'+str(i)+r'\s*$',p) for i,p in enumerate(pages,1)))
    if path.name == 'LAFROX-Subdocumento4.pdf':
        normalized = re.sub(r'\s+',' ','\n'.join(pages))
        check('SD4 sin marcador de revisión humana', not re.search(r'\[\[REVISI[ÓO]N\s+HUMANA',normalized,re.I))
    if path.name == 'LAFROX-Formulario-T-12.pdf':
        compact = re.sub(r'\s+','','\n'.join(pages))
        identifiers = [row.split('&')[0].strip() for row in new_rows]
        check('PDF T12 contiene los 653 identificadores', all(id_ in compact for id_ in identifiers))
    if 'Subdocumento13.pdf' in path.name or 'T-19.pdf' in path.name:
        check('PDF sin volumen térmico antiguo: '+path.name, '10.920' not in '\n'.join(pages))
    outputs.append({'archivo':str(path),'paginas':len(doc.pages),'sha256':sha(path.read_bytes())})

report = {'alcance':'Coherencia SD4/SD13/T19 y RT26.01. No modifica SD7/SD8/SD9 ni concilia su planificación.',
          'limites':'Pruebas documentales automatizadas. No acreditan revisión humana, integración física, compra, certificación, aprobación del CLIENTE ni cumplimiento total de bases.',
          'comprobaciones':checks,'pdf':outputs}
target = root4/'04/revision/VERIFICACION_COHERENCIA_FRIO_2026-10-25.json'
target.write_text(json.dumps(report,ensure_ascii=False,indent=2),encoding='utf-8')
print(f'{len(checks)} comprobaciones correctas. {len(outputs)} PDF. {target}')
