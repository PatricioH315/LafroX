"""Topología legible; conserva íntegra la lámina original de nube."""
from pathlib import Path
import xml.etree.ElementTree as ET

root = ET.Element('mxfile', host='app.diagrams.net')
diagram = ET.SubElement(root, 'diagram', id='nube-as2', name='Nube y borde AS2')
model = ET.SubElement(diagram, 'mxGraphModel', page='0')
cells = ET.SubElement(model, 'root')
ET.SubElement(cells, 'mxCell', id='0')
ET.SubElement(cells, 'mxCell', id='1', parent='0')


def box(id_, value, x, y, w, h, fill='#FFFFFF', group=False):
    style = ('rounded=1;whiteSpace=wrap;html=1;fontSize=20;fontFamily=Helvetica;'
             f'fillColor={fill};strokeColor=#555555;fontColor=#111111;spacing=6;')
    if group:
        style += 'verticalAlign=top;align=left;fontStyle=1;dashed=1;'
    cell = ET.SubElement(cells, 'mxCell', id=id_, parent='1', vertex='1', value=value, style=style)
    ET.SubElement(cell, 'mxGeometry', x=str(x), y=str(y), width=str(w), height=str(h), **{'as': 'geometry'})


def edge(a, b, side=False):
    ports = 'exitX=1;exitY=.5;entryX=0;entryY=.5;' if side else 'exitX=.5;exitY=1;entryX=.5;entryY=0;'
    c = ET.SubElement(cells, 'mxCell', id=a+'-'+b, parent='1', edge='1', source=a, target=b,
                      style='edgeStyle=orthogonalEdgeStyle;endArrow=block;strokeColor=#555555;'+ports)
    ET.SubElement(c, 'mxGeometry', relative='1', **{'as': 'geometry'})


box('region', 'AWS sa-east-1 · VPC Producción · dos zonas: sa-east-1a / sa-east-1b', 0, 270, 800, 420, '#EDF6FA', True)
box('apps', 'Personas externas<br>EC55 / TC58e y portales', 0, 0, 250, 75)
box('chains', 'Cadenas de supermercados<br>Mensajes AS2 y MDN', 275, 0, 250, 75)
box('office', 'Oficinas y teletrabajo<br>Consolas y administración', 550, 0, 250, 75)
box('web', 'Borde web global<br>Route 53 · CloudFront<br>WAF · Shield Advanced<br>S3 portales privado', 0, 105, 250, 125)
box('as2edge', 'Borde AS2 global<br>CloudFront / WAF / Shield<br>Sin caché ni CAPTCHA<br>MIME y firma intactos', 275, 105, 250, 125, '#FDE8DA')
box('va', 'Acceso de personal<br>Verified Access<br>Identidad, MFA y postura<br>Sin consola pública', 550, 105, 250, 125)
box('app', 'API REST + autorizador<br>ALB privado → Fargate<br>Perfiles en dos zonas<br>OIDC público → Keycloak', 10, 320, 250, 150)
box('as2', 'ALB de origen AS2<br>Solo CloudFront + secreto<br>TLS 1.3 en cada tramo<br>OpenAS2: 2 tareas / 2 AZ<br>Firma, cifrado y MDN', 275, 320, 250, 150, '#FDE8DA')
box('console', 'Consolas en ALB privado<br>Angular: 2 tareas / 2 AZ<br>API privada / execute-api<br>Keycloak privado (admin)<br>OIDC público solo usuario', 540, 320, 250, 150)
box('data', 'Aurora escritor/lector · ElastiCache primario/réplica · DMS desde VM-02<br>Frío: IoT Core + CloudConnect/SQS → M9, no por portales<br>DynamoDB · S3 datos · SQS FIFO · SNS · ECR<br>Analítica: S3 → Glue → Redshift Serverless → QuickSight', 10, 510, 780, 140)
box('dr', 'AWS us-east-1 · Recuperación<br><br>Aurora secundaria · DynamoDB · S3<br>Datos replicados; GPS no se replica<br><br>API, Lambda, ALB, Fargate,<br>Keycloak, AS2 y Verified Access<br>se restituyen y validan antes<br>de redirigir el borde global<br><br>Transit Gateway · VPN · Backup<br>SQS · SNS · ECR<br>RTO ≤4 h · RPO ≤15 min', 840, 270, 350, 420, '#EDF6FA')
box('network', 'Conectividad regional y cinco sitios<br>VPC Hub: Transit Gateway y Site-to-Site VPN<br>Endpoints privados de servicios AWS<br>ALB web/consolas privados; AS2 de origen restringido<br>Operación local sin WAN; ERP único emisor en Talca', 0, 730, 590, 150)
box('ops', 'Operación, seguridad y claves<br>CloudWatch · CloudTrail · Config · GuardDuty<br>Security Hub · Inspector · KMS · Secrets Manager<br>Systems Manager · IAM Identity Center<br>Backup y custodia segregada de registros', 610, 730, 580, 150)
for a, b in [('apps', 'web'), ('chains', 'as2edge'), ('office', 'va'),
             ('web', 'app'), ('as2edge', 'as2'), ('va', 'console'),
             ('app', 'data'), ('as2', 'data'), ('console', 'data')]:
    edge(a, b)
edge('data', 'dr', side=True)

target = Path(__file__).with_name('Arquitectura_Fisica_Nube_AS2_vigente.drawio')
ET.ElementTree(root).write(target, encoding='utf-8', xml_declaration=True)
print(target)
