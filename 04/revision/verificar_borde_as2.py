"""Regresión documental AS2; no ejecuta integración ni pruebas de seguridad reales."""
import argparse
from collections import Counter
import hashlib
import json
from pathlib import Path
import re
import subprocess
import xml.etree.ElementTree as ET

from pypdf import PdfReader

parser = argparse.ArgumentParser()
parser.add_argument('--sd3', type=Path, required=True)
args = parser.parse_args()
root = Path(__file__).resolve().parents[2]
checks = []


def check(name, condition):
    checks.append({'comprobacion': name, 'resultado': bool(condition)})
    if not condition:
        raise AssertionError(name)


def source(path):
    return (root / path).read_text(encoding='utf-8')


def digest(path):
    return hashlib.sha256(path.read_bytes()).hexdigest()


connection = source('04/partes/4.2_fisica/02_c_conexiones.tex')
check('Borde dedicado con los cuatro componentes', all(s in connection for s in [
    'distribución CloudFront dedicada', 'AWS WAF', 'Shield Advanced', 'ALB de origen']))
check('Origen restringido en red y aplicación', all(s in connection for s in [
    'lista administrada de prefijos', 'encabezado de origen secreto', 'predeterminada devuelve 403']))
check('Sin tareas públicas ni secreto en Git', all(s in connection for s in [
    'sin dirección pública', 'no se escribe en Git', 'Secrets Manager']))
check('Sin caché, compresión ni cambio de MIME', all(s in connection for s in [
    'deshabilita caché y compresión', 'conserva sin transformación el cuerpo MIME']))
check('No se confunde WAF con descifrado de EDI', 'no se presenta como análisis del EDI cifrado completo' in connection)
check('WAF no se omite ni impone retos de navegador', all(s in connection for s in [
    'no utiliza CAPTCHA', 'No hay una regla de permiso temprano', 'se limitan al comportamiento AS2']))
check('Ambos MDN, duplicados, tamaño y timeout definidos', all(s in connection for s in [
    '32 MiB', '30 s', '60 s', 'MDN asíncrono', 'Message-ID', 'deduplica']))
controls = source('04/anexos/logica/partes/21_anexo_4_1_r_controles_seguridad.tex')
check('TLS 1.3 por salto, no una sola terminación', all(s in controls for s in [
    'cadena--CloudFront', 'CloudFront--ALB', 'ALB--OpenAS2']) and 'deshabilita TLS 1.2' in connection)
check('Aceptación no se presenta como ejecución', 'no resultados de ensayos ejecutados' in connection)
check('Superficie AS2 ya no publica NLB', 'Network Load Balancer, TCP 443' not in connection)

inventory = source('04/formularios/T11/15_anexo_t11.tex')
check('T11 cuenta distribución, ACL y ALB', all(s in inventory for s in [
    '1 ALB por región habilitada', '1 distribución CloudFront', '1 ACL WAF global de AS2']))
check('T11 conserva las dos tareas y no supone coste cero', all(s in inventory for s in [
    '2 tareas en 2 zonas', 'deben trasladarse al costeo', 'sin atribuirles costo cero']))
for filename in ['02_0_arquitectura_fisica.tex', '02_b_servicios_nube.tex', '11_j_despliegue.tex']:
    s = source('04/partes/4.2_fisica/' + filename)
    check(filename + ': sin NLB activo', 'Network Load Balancer' not in s and 'AS2' in s)
check('ADR11 descarta el ingreso anterior', 'se descarta como entrada pública AS2' in source(
    '04/anexos/logica/partes/18_anexo_4_1_o_decisiones_logicas.tex'))
check('4N corresponde con el nuevo borde', 'CloudFront/WAF/Shield, ALB restringido' in source(
    '04/anexos/logica/partes/15_anexo_4_1_n_correspondencia_de_componentes_logicos.tex'))

for filename in ['Arquitectura_Fisica_General_frio_legible.drawio', 'Arquitectura_Fisica_Nube_AS2_vigente.drawio']:
    tree = ET.parse(root / '04/figuras/fuentes' / filename)
    values = ' '.join(c.get('value', '') for c in tree.findall('.//mxCell'))
    check(filename + ': XML y ruta vigente', 'ALB' in values and 'NLB' not in values)
for path in ['04/figuras/fisica/Arquitectura_Fisica_General.png',
             '04/figuras/fisica/Arquitectura_Fisica_Nube.png']:
    head = subprocess.check_output(['git', '-C', str(root), 'show', 'HEAD:' + path])
    check(path + ': original conservado', (root / path).read_bytes() == head)
for filename in ['Arquitectura_Fisica_General.drawio', 'Arquitectura_Fisica_Nube.drawio']:
    check(filename + ': fuente original disponible en disco (no versionada en HEAD)',
          (root / 'drawio/4.2_fisica' / filename).is_file())

previous = subprocess.check_output(['git', '-C', str(args.sd3), 'show', 'HEAD:LAFROX-Formulario-T-12.tex']).decode('utf-8')
current = (args.sd3 / 'LAFROX-Formulario-T-12.tex').read_text(encoding='utf-8')
pattern = r'^\s*(?:RF|RNF|RT)-[^ &]+\s*&.*$'
old, new = re.findall(pattern, previous, re.M), re.findall(pattern, current, re.M)
check('T12 conserva 653 filas e identificadores en orden', len(old) == len(new) == 653 and
      [s.split('&')[0] for s in old] == [s.split('&')[0] for s in new])
check('T12 no cambia exigencias literales', all(a.split('&')[1] == b.split('&')[1] for a, b in zip(old, new)))
changed = {b.split('&')[0].strip() for a, b in zip(old, new) if a != b}
check('Solo RT26.01 previo y RT11.07 actual cambian contra HEAD', changed == {'RT-26.01', 'RT-11.07'})
check('T12 cuenta 597/34/22', Counter(s.split('&')[2].strip() for s in new) == {
    'Cumple': 597, 'Cumple parcialmente': 34, 'No cumple': 22})
for id_ in ['RT-11.04', 'RT-11.08', 'RT-12.03', 'RF-15.03']:
    row = next(s for s in new if s.split('&')[0].strip() == id_)
    check(id_ + ': no se cierra sin decisión/evidencia', row.split('&')[2].strip() == 'Cumple parcialmente')

historical = json.loads(source('04/revision/VERIFICACION_COHERENCIA_FRIO_2026-10-25.json'))
for item in historical['pdf']:
    if 'SD13_v_nueva' in item['archivo']:
        p = Path(item['archivo'])
        check(p.name + ': conserva corrección de frío', digest(p) == item['sha256'])

pdfs = [root / 'entrega' / (name + '.pdf') for name in [
    'LAFROX-Subdocumento4', 'LAFROX-Subdocumento4-Anexos', 'LAFROX-Formulario-T-11']]
pdfs.append(args.sd3 / 'LAFROX-Formulario-T-12.pdf')
metadata = []
for p in pdfs:
    doc = PdfReader(p)
    check(p.name + ': PDF legible sin contraseña', not doc.is_encrypted and len(doc.pages) > 0)
    metadata.append({'archivo': str(p), 'paginas': len(doc.pages), 'sha256': digest(p)})
    if 'T-12' in p.name:
        text = re.sub(r'\s+', '', ' '.join(page.extract_text() or '' for page in doc.pages))
        ids = [s.split('&')[0].strip() for s in new]
        check('PDF T12 conserva los 653 IDs', all(id_ in text for id_ in ids))

report = {'alcance': 'Cierre documental del borde AS2 y regresión T12/frío; no revisión completa de admisibilidad.',
          'limites': 'No ensayos de AS2, despliegue, aprobación humana/CLIENTE ni costeo. SD7/SD8/SD9 excluidos.',
          'comprobaciones': checks, 'pdf': metadata}
target = root / '04/revision/VERIFICACION_BORDE_AS2_2026-10-25.json'
target.write_text(json.dumps(report, ensure_ascii=False, indent=2) + '\n', encoding='utf-8')
print(f'{len(checks)} comprobaciones documentales correctas; {target}')
