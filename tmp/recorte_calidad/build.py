from pathlib import Path
from copy import deepcopy
from lxml import etree as E
import zipfile,json,hashlib,posixpath,collections,io,re
from decimal import Decimal

ROOT=Path(__file__).resolve().parents[2]
SOURCE=ROOT/'Presentaciones/Actualizada/LafroX - Informe 2 - transicion Gantt y EDT refinadas.pptx'
OUT=ROOT/'tmp/recorte_calidad/candidate.pptx'
NS={'p':'http://schemas.openxmlformats.org/presentationml/2006/main','a':'http://schemas.openxmlformats.org/drawingml/2006/main','r':'http://schemas.openxmlformats.org/officeDocument/2006/relationships'}
def q(s):
    p,n=s.split(':');return '{'+NS[p]+'}'+n
with zipfile.ZipFile(SOURCE) as z:
    infos=z.infolist();data={i.filename:z.read(i.filename) for i in infos}
original=data.copy();roots={}
def root(name):
    if name not in roots:roots[name]=E.fromstring(data[name])
    return roots[name]
def slide(i):return root(f'ppt/slides/slide{i}.xml')
def obj(i,id):return slide(i).xpath(f'//p:cNvPr[@id="{id}"]',namespaces=NS)[0].getparent().getparent()
def box(i,id,x=None,y=None,w=None,h=None):
    sp=obj(i,id);tf=sp.find('p:spPr/a:xfrm',NS)
    for values,node in [({'x':x,'y':y},tf.find('a:off',NS)),({'cx':w,'cy':h},tf.find('a:ext',NS))]:
        for k,v in values.items():
            if v is not None:node.set(k,str(round(v*12700)))
def text(i,id,value,size=None,color=None,bold=None):
    sp=obj(i,id);body=sp.find('p:txBody',NS);old=body.findall('a:p',NS);templates=[deepcopy(p) for p in old]
    for p in old:body.remove(p)
    for j,line in enumerate(value.split('\n')):
        t=templates[min(j,len(templates)-1)];pp=t.find('a:pPr',NS);rp=t.find('a:r/a:rPr',NS)
        if rp is None:rp=templates[0].find('a:r/a:rPr',NS)
        rp=deepcopy(rp) if rp is not None else E.Element(q('a:rPr'),lang='es-CL',sz='1800')
        if size is not None:rp.set('sz',str(round(size*100)))
        if bold is not None:rp.set('b','1' if bold else '0')
        if color:
            for f in rp.findall('a:solidFill',NS):rp.remove(f)
            f=E.Element(q('a:solidFill'));E.SubElement(f,q('a:srgbClr'),val=color);rp.insert(0,f)
        p=E.SubElement(body,q('a:p'))
        if pp is not None:p.append(deepcopy(pp))
        r=E.SubElement(p,q('a:r'));r.append(rp);E.SubElement(r,q('a:t')).text=line
        E.SubElement(p,q('a:endParaRPr'),lang='es-CL',sz=rp.get('sz','1800'))
def remove(i,id):
    s=obj(i,id);s.getparent().remove(s)
def extra(i,template,id,value,x,y,w,h,size,color='606060',bold=False):
    s=deepcopy(obj(i,template));c=s.find('p:nvSpPr/p:cNvPr',NS);c.set('id',str(id));c.set('name',f'Calidad resumida {id}')
    obj(i,template).getparent().append(s);text(i,id,value,size,color,bold);box(i,id,x,y,w,h)
    return s

# 33: Keep the explanatory purpose requested by the teacher, but move business
# credentials and legal/interchange detail to the speaker's reference notes.
text(33,1835,'Normas del\nplan de calidad',51)
text(33,1838,'REFERENCIA → APLICACIÓN EN EL PLAN',16)
for id in range(1857,1863):remove(33,id)
for row,(bg,label,desc) in enumerate([(1839,1840,1841),(1842,1843,1844),(1845,1846,1847),(1848,1849,1850),(1851,1852,1853),(1854,1855,1856)]):
    y=133+row*84;box(33,bg,y=y,h=64);box(33,label,y=y+18,h=32);box(33,desc,y=y+18,h=38)
text(33,1863,'EVIDENCIA PARA PUELCHE',16)
for id,value in {1864:'Producto y datos',1865:'Pruebas y conciliaciones',1866:'Seguridad y accesibilidad',1867:'Informes automáticos y revisión manual',1868:'Gestión de calidad',1869:'Registros y acciones correctivas'}.items():text(33,id,value)
for j,(a,b) in enumerate([(1864,1865),(1866,1867),(1868,1869)]):
    box(33,a,y=335+j*100,h=32);box(33,b,y=372+j*100,h=38)
box(33,1863,y=286,h=26)
for id in range(1870,1874):remove(33,id)

# 34: Keep the model of quality visible; explain only the critical criteria in notes.

# 35: Group G0–G6 into three plain-language moments, retaining full gates in notes.
for start in [1944,1948,1952,1960]:
    for id in range(start,start+4):remove(35,id)
groups=[(1940,1941,1942,1943,'A','Revisar el cambio','Pares · pruebas · seguridad del código'),
        (1956,1957,1958,1959,'B','Validar antes de Producción','Pruebas · certificación · reversión'),
        (1964,1965,1966,1967,'C','Supervisar en operación','Indicadores · reversión ante desvíos')]
for j,(bg,badge,title,desc,letter,heading,body) in enumerate(groups):
    y=150+j*155;box(35,bg,y=y,h=118)
    text(35,badge,letter,21);box(35,badge,y=y+28)
    text(35,title,heading,25);box(35,title,y=y+18,h=42)
    text(35,desc,body,19);box(35,desc,y=y+65,h=36)
extra(35,1927,35002,'CONTROLES DURANTE LA ENTREGA',759.6,98,600,30,17,'E8641B',True)
extra(35,1927,35003,'MEJORA CONTINUA',759.6,650,600,27,16,'E8641B',True)
extra(35,1943,35004,'Analizar causa → corregir → verificar → cerrar',759.6,688,600,32,18)

# 36: Reduce the test inventory to three groups, then show a concrete evidence
# chain instead of an additional standalone technical traceability slide.
text(36,1974,'Pruebas y evidencia')
for id in [1984,1985,1987,1988,1989,1994,1995,1996,2001,2002,2003,2004,2008]:remove(36,id)
columns=[(1981,[1982,1983,1986],'Código e integración',['Reglas y componentes','Contratos e integración','Regresión, seguridad y accesibilidad']),
         (1990,[1991,1992,1993],'Antes de Producción',['Aceptación de usuarios','Carga, fallas y recuperación','Migración, despliegue y reversión']),
         (1997,[1998,1999,2000],'Terreno y operación',['Trabajo sin señal y sincronización','Frío con guantes y uso real','Indicadores en marcha blanca'])]
for j,(header,ids,title,items) in enumerate(columns):
    x=72+j*444;box(36,header,x=x,w=408,h=48);text(36,header,title,24)
    for row,(id,value) in enumerate(zip(ids,items)):
        box(36,id,x=x,y=316+row*62,w=408,h=48);text(36,id,value,20)
extra(36,1982,36001,'EJEMPLO DE TRAZABILIDAD DEL REQUISITO A LA ACEPTACIÓN',72,510,1296,32,18,'E8641B',True)
sp=obj(36,36001);pr=sp.find('p:spPr',NS)
for f in pr.findall('a:solidFill',NS):pr.remove(f)
E.SubElement(pr,q('a:noFill'))
for j,(id,value) in enumerate([(2005,'Requisito\nIdentificar afectados por lote en < 2 h'),(2006,'Prueba\nSimulacro cronometrado'),(2007,'Aceptación\nEvidencia y acta de Puelche')]):
    box(36,id,x=72+j*444,y=555,w=408,h=90);text(36,id,value)
    for k,p in enumerate(obj(36,id).findall('p:txBody/a:p',NS)):
        for rp in p.findall('a:r/a:rPr',NS):rp.set('sz','2400' if k==0 else '1800')
extra(36,1982,36002,'Cada prueba deja evidencia; los datos reales de prueba requieren anonimización.',72,665,1296,28,18,'606060',False)
pr=obj(36,36002).find('p:spPr',NS)
for f in pr.findall('a:solidFill',NS):pr.remove(f)
E.SubElement(pr,q('a:noFill'))

def note_path(i):
    rel=root(f'ppt/slides/_rels/slide{i}.xml.rels')
    n=next(e for e in rel if e.get('Type','').endswith('/notesSlide'))
    return posixpath.normpath('ppt/slides/'+n.get('Target'))
def notes(i):
    r=root(note_path(i));b=r.xpath('//p:sp[p:nvSpPr/p:nvPr/p:ph[@type="body"]]/p:txBody',namespaces=NS)[0]
    return b,'\n'.join(''.join(p.xpath('.//a:t/text()',namespaces=NS)) for p in b.findall('a:p',NS))
archived=notes(37)[1]
scripts={
33:'El plan convierte las referencias en controles verificables. ISO 25010 organiza la calidad del producto; ISO 25012, la calidad de los datos; ISO 29119, las pruebas. PMBOK guía la gestión; WCAG y OWASP apoyan accesibilidad y seguridad. Para Puelche, el cumplimiento se demuestra con pruebas, conciliaciones, informes y registros.',
34:'La calidad se juzga con criterios de aceptación, no con resultados que demos por logrados. Destacamos que los requisitos funcionen, que el despacho mantenga continuidad y que no queden hallazgos graves abiertos. Las demás características siguen en el modelo. Los resultados de negocio se comprueban en operación y en el momento previsto.',
35:'Agrupamos los controles en revisión del cambio, validación antes de Producción y supervisión en operación. Si un criterio falla, se corrige y se verifica. La aceptación de Puelche exige conjuntamente todas las condiciones del protocolo; entrar a Producción no significa que la marcha blanca esté aceptada. Las desviaciones se tratan analizando la causa y cerrando con evidencia.',
36:'Las pruebas avanzan del código hacia condiciones de operación real. Comprobamos integración, carga, recuperación y trabajo sin señal. Cada resultado queda documentado. En el ejemplo, el requisito de identificar clientes afectados por un lote se comprueba mediante un simulacro cronometrado y se vincula con la aceptación de Puelche. El detalle técnico queda como respaldo.'}
for i,script in scripts.items():
    b,old=notes(i)
    backup=old.split('RESPALDO DE CONSULTA',1)[-1] if 'RESPALDO DE CONSULTA' in old else old
    if i==33:backup+='\nREFERENCIAS COMPLEMENTARIAS EN RESPALDO: ISO 9001 (gestión y auditoría), CMMI-DEV N3 (evaluación de madurez), sanidad alimentaria, documentación tributaria, jornada de conductores, protección de datos y GS1/EDI. No se eliminan de la oferta; no es necesario enumerarlas al exponer este bloque.'
    if i==35:backup+='\nMEJORA CONTINUA: analizar causa y responsable, corregir, verificar con el mismo criterio y cerrar o escalar con evidencia (SD9 §9.2.6). Las tres agrupaciones visibles no sustituyen las puertas G0–G6 del plan.'
    if i==36:backup+='\nRESPALDO DE TRAZABILIDAD Y MEJORA ANTES MOSTRADO EN UNA LÁMINA INDEPENDIENTE\n'+archived
    for p in b.findall('a:p',NS):b.remove(p)
    for line in ('GUION ORAL COMPACTO\n'+script+'\n\nRESPALDO DE CONSULTA'+backup).split('\n'):
        p=E.SubElement(b,q('a:p'));r=E.SubElement(p,q('a:r'));E.SubElement(r,q('a:rPr'),lang='es-CL',sz='1200');E.SubElement(r,q('a:t')).text=line

# Remove only the old standalone traceability slide. Do not rebuild/reorder the
# remaining slides, so the user's Gantt/EDT/RBS Morph sequences stay unchanged.
pres=root('ppt/presentation.xml');rels=root('ppt/_rels/presentation.xml.rels')
removed_rel=next(e for e in rels if e.get('Target')=='slides/slide37.xml');rid=removed_rel.get('Id')
sid=next(e for e in pres.find('p:sldIdLst',NS) if e.get(q('r:id'))==rid);numeric_id=sid.get('id');sid.getparent().remove(sid);rels.remove(removed_rel)
for e in pres.xpath('//*[local-name()="sldId" and @id="'+numeric_id+'"]'):e.getparent().remove(e)
for e in pres.xpath('//*[local-name()="sld" and @r:id="'+rid+'"]',namespaces=NS):e.getparent().remove(e)
removed={'ppt/slides/slide37.xml','ppt/slides/_rels/slide37.xml.rels',note_path(37),'ppt/notesSlides/_rels/'+Path(note_path(37)).name+'.rels'}
types=root('[Content_Types].xml')
for e in list(types):
    if (e.get('PartName') or '').lstrip('/') in removed:types.remove(e)
if 'docProps/app.xml' in data:
    a=root('docProps/app.xml')
    for e in a.xpath('//*[local-name()="Slides"]'):e.text='50'

# Keep visible folios consistent after removal; no other text changes outside
# the quality block, including innovations, Gantt, EDT and risks.
for old in range(38,52):
    r=slide(old)
    for c in r.findall('.//p:cNvPr',NS):
        if c.get('name')=='!!slidenum':
            for t in c.getparent().getparent().findall('.//a:t',NS):t.text=str(old-1)
    n=root(note_path(old))
    for s in n.xpath('//p:sp[p:nvSpPr/p:nvPr/p:ph[@type="sldNum"]]',namespaces=NS):
        for t in s.findall('.//a:t',NS):t.text=str(old-1)
for name,r in roots.items():
    if name not in removed:data[name]=E.tostring(r,xml_declaration=True,encoding='UTF-8',standalone=True)
for n in removed:data.pop(n,None)
# Native PowerPoint saves binary-float tails in this pre-existing chart cache.
# Refresh only equivalent values from the unchanged embedded worksheet; this
# does not alter the business data, workbook or visible chart.
chartname='ppt/charts/chart1.xml';cr=E.fromstring(data[chartname]);cn={'c':'http://schemas.openxmlformats.org/drawingml/2006/chart'}
xlsxname=next(n for n in data if n.startswith('ppt/embeddings/') and n.endswith('.xlsx'))
with zipfile.ZipFile(io.BytesIO(data[xlsxname])) as z:
    sx=E.fromstring(z.read('xl/worksheets/sheet1.xml'));sn={'s':'http://schemas.openxmlformats.org/spreadsheetml/2006/main'}
    cells={c.get('r'):c.findtext('s:v',namespaces=sn) for c in sx.findall('.//s:c',sn)}
cache_repairs=0
for ref in cr.findall('.//c:numRef',cn):
    m=re.fullmatch(r"'?([^']+)'?!\$([A-Z]+)\$(\d+):\$([A-Z]+)\$(\d+)",ref.findtext('c:f',namespaces=cn) or '')
    if not m:continue
    sheet,col,start,_,end=m.groups()
    for pt in ref.findall('c:numCache/c:pt',cn):
        v=pt.find('c:v',cn);cell=cells.get(f'{col}{int(start)+int(pt.get("idx"))}')
        if cell is not None and Decimal(v.text)!=Decimal(cell):
            assert abs(Decimal(v.text)-Decimal(cell))<Decimal('0.00000001')
            v.text=cell;cache_repairs+=1
if cache_repairs:data[chartname]=E.tostring(cr,xml_declaration=True,encoding='UTF-8',standalone=True)
assert len(pres.find('p:sldIdLst',NS))==50
# No transition element or animation tree in retained slides is rewritten.
for i in range(1,52):
    if i==37:continue
    a=E.fromstring(original[f'ppt/slides/slide{i}.xml']);b=E.fromstring(data[f'ppt/slides/slide{i}.xml'])
    for tag in ['transition','timing']:
        assert [E.tostring(t) for t in a.xpath(f'//*[local-name()="{tag}"]')]==[E.tostring(t) for t in b.xpath(f'//*[local-name()="{tag}"]')],(i,tag)
with zipfile.ZipFile(OUT,'w') as z:
    for info in infos:
        if info.filename in data:z.writestr(info,data[info.filename])
fonts=sorted({e.get('typeface') for n,v in original.items() if n.startswith('ppt/slides/slide') and n.endswith('.xml') for e in E.fromstring(v).xpath('//*[local-name()="latin" or local-name()="ea" or local-name()="cs" or local-name()="sym" or local-name()="buFont"]') if e.get('typeface') and not e.get('typeface').startswith('+')})
report={'source':str(SOURCE),'source_sha256':hashlib.sha256(SOURCE.read_bytes()).hexdigest(),'original_slide_count':51,'final_slide_count':50,'quality_positions':[33,34,35,36],'innovations_position':37,'removed_old_position':37,'fonts':fonts,'equivalent_chart_cache_repairs':cache_repairs,'changed_parts':[n for n in data if data[n]!=original.get(n)],'removed_parts':sorted(removed),'scripts':scripts}
(ROOT/'tmp/recorte_calidad/report.json').write_text(json.dumps(report,ensure_ascii=False,indent=2),encoding='utf8')
print(json.dumps({k:v for k,v in report.items() if k not in ['changed_parts','scripts']},ensure_ascii=False,indent=2))
