from pathlib import Path
from pypdf import PdfReader
import shutil,hashlib,json
root=Path(__file__).resolve().parents[1];build=root/'tmp/limpieza-s8-build'
report={}
for name in ['LAFROX-Subdocumento8','LAFROX-Subdocumento8-Anexos','LAFROX-Formulario-T-16']:
 source=build/(name+'.pdf');target=root/(name+'.pdf')
 shutil.copy2(source,target)
 digest=hashlib.sha256(source.read_bytes()).hexdigest()
 assert hashlib.sha256(target.read_bytes()).hexdigest()==digest
 report[name]={'pages':len(PdfReader(target).pages),'sha256':digest}
 print(name,report[name]['pages'],'páginas; copia final verificada')
(build/'entrega.json').write_text(json.dumps(report,indent=2),encoding='utf-8')
(root/'odd/tasks/interno-s8/limpieza-editorial.md').write_text('''# Limpieza editorial de S8, anexos y T-16

Material exclusivamente interno, fuera de los PDF dirigidos al cliente.

- La matriz de observaciones, la equivalencia histórica de riesgos y los antecedentes de coordinación se conservan en esta carpeta; se retiró el Anexo 8.I de la publicación.
- El Anexo 8.D presenta dependencias operativas y continuidad; el Anexo 8.E contiene CT-01–CT-16. La equivalencia de controles se consulta en equivalencia-controles.md.
- Se retiraron las cifras históricas de reservas y las explicaciones de reemplazo. Se mantienen los cálculos actuales y las condiciones reales de autorización, evidencia y programación.
- Se comprobaron por comparación de fuentes los 35 riesgos, sus valoraciones y respuestas, las estimaciones, FMEA, costo-beneficio, residual y distribución de esfuerzo. La RBS y las líneas protegidas con «contenido academico» permanecen intactas.
- Los demás subdocumentos no se modificaron. La coordinación pendiente se consulta en los antecedentes internos; no se presenta como trabajo ejecutado en los entregables.
- Los tres PDF se compilaron con LuaLaTeX hasta estabilizar índices y referencias y se revisaron visualmente todas las páginas mediante hojas de contacto, con ampliación de tablas, RBS, folios y firmas.

La evidencia de comparación y los registros de compilación están en tmp/limpieza-s8-build.
''',encoding='utf-8')
