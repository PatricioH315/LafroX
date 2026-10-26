"""Vista general legible: mismas ocho capas y doce módulos, sin recortar el original.

La vista detallada anterior se conserva en ARQL-01_General_definitivo.pdf.
Las interfaces por actor se desarrollan en las vistas de capa y en el Anexo 4-N.
"""
from pathlib import Path
import xml.etree.ElementTree as ET

OUT = Path(__file__).with_name('ARQL-01_General_frio_vigente.drawio')
mx = ET.Element('mxfile', host='app.diagrams.net')
dg = ET.SubElement(mx, 'diagram', name='General vigente', id='general-frio')
model = ET.SubElement(dg, 'mxGraphModel', grid='1', page='0')
root = ET.SubElement(model, 'root')
ET.SubElement(root, 'mxCell', id='0')
ET.SubElement(root, 'mxCell', id='1', parent='0')

def box(id_, text, x, y, w, h, fill='#FFFFFF'):
    c = ET.SubElement(root, 'mxCell', id=id_, value=text, parent='1', vertex='1',
        style=f'rounded=1;whiteSpace=wrap;html=1;fontFamily=Helvetica;fontSize=20;'
              f'fillColor={fill};strokeColor=#555555;fontColor=#111111;spacing=6;')
    ET.SubElement(c, 'mxGeometry', x=str(x), y=str(y), width=str(w), height=str(h), **{'as':'geometry'})

def edge(a,b):
    c=ET.SubElement(root,'mxCell',id=f'e-{a}-{b}',source=a,target=b,parent='1',edge='1',
        style='edgeStyle=orthogonalEdgeStyle;rounded=0;endArrow=block;strokeColor=#555555;exitX=0.5;exitY=1;entryX=0.5;entryY=0;')
    ET.SubElement(c,'mxGeometry',relative='1',**{'as':'geometry'})

box('ui','1 · Presentación<br>C-01 Preventa · C-02 Reparto · C-03 Bodega/Calidad · Portales Angular y consolas',0,0,900,60,'#FDE8DA')
box('edge-public','2 · Borde público<br>CloudFront · WAF · Shield',0,76,280,60)
box('edge-private','2 · Acceso privado<br>Verified Access · red del sitio',310,76,280,60)
box('edge-truck','2 · Frío local<br>B-02/B-04 · C-02/B-08<br>Móvil + Iridium SBD',620,76,280,84,'#FDE8DA')
box('api','3 · Servicios: API Gateway → ALB privado · Keycloak<br>WMS: puerta local y verificador de turno sin WAN',0,172,900,58)
names=['M1 Recepción','M2 Inventario','M3 Preventa','M4 Rutas','M5 Preparación','M6 Reparto',
       'M7 Cobranza<br>y rendición','M8 Devoluciones<br>y envases','M9 Calidad<br>y trazabilidad','M10 Analítica','M11 Canal<br>moderno','M12 Telemetría<br>de flota']
box('business','4 · Negocio: Laravel/PHP; perfiles de ejecución y reversión independientes',0,254,900,36,'#EEF2F4')
for i,name in enumerate(names):box(f'm{i+1}',name,(i%6)*151,292+(i//6)*64,145,(74 if i>=6 else 58),'#F4F4F4')
box('integration','5 · Integración: RabbitMQ · SQS FIFO · ACL ERP/DTE · OpenAS2<br>INT-05: IoT Core + CloudConnect/SQS → M9<br>Persistencia antes de A2; deduplicación móvil/SBD',0,432,900,84)
box('data','6 · Datos: PostgreSQL/Room locales; Aurora, S3, DynamoDB y N-10 en nube<br>INT-05: 30.548 mensajes / 127.848 lecturas por día<br>SBD: 8.120 mensajes de transporte paralelo, sin duplicar eventos',0,532,900,84)
box('security','7 · Seguridad transversal<br>OIDC · KMS · MDM · mTLS · auditoría',0,632,435,72)
box('obs','8 · Observabilidad transversal<br>ADOT y CloudWatch; nube y borde',465,632,435,72)
box('scope','Actores, permisos, contratos y emplazamientos: vistas de capa y Anexo 4-N.<br>El frío se protege localmente; M12/GPS no se mezcla con INT-05.',0,728,900,60,'#F4F4F4')
for i in range(1,13):
    cell=next(c for c in root.findall('mxCell') if c.get('id')==f'm{i}')
    cell.set('style',cell.get('style').replace('fontSize=20','fontSize=19').replace('spacing=6;','spacing=2;'))
for target in ['edge-public','edge-private','edge-truck']:edge('ui',target)
for target in ['edge-public','edge-private']:edge(target,'api')
edge('edge-truck','integration')
truck_edge=next(c for c in root.findall('mxCell') if c.get('id')=='e-edge-truck-integration')
truck_edge.set('style','edgeStyle=orthogonalEdgeStyle;rounded=0;endArrow=block;strokeColor=#555555;exitX=1;exitY=0.5;entryX=1;entryY=0.5;')
pts=ET.SubElement(truck_edge.find('mxGeometry'),'Array',{'as':'points'})
ET.SubElement(pts,'mxPoint',x='925',y='112')
ET.SubElement(pts,'mxPoint',x='925',y='474')
edge('api','business')
for a,b in [('m7','integration'),('m9','integration'),('m11','integration'),('integration','data')]:edge(a,b)
ET.ElementTree(mx).write(OUT,encoding='utf-8',xml_declaration=True)
print(OUT)
