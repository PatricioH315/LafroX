# Genera los 5 diagramas de ambientes del 4.2.4 centrados en el despliegue:
# cadena del equipo de desarrollo -> ECR -> donde vive el codigo (Fargate / VM / E-01).
# Nombres y codigos tomados del informe (02_a, 02_b, 11_j, 06_e, 15_anexo_t11).
import os
from xml.sax.saxutils import escape
OUT = r'C:\Users\Guillermo Castillo M\LafroX-g4\SUBDOCUMENTO_4\Diagramas\Ambientes'

# Colores oficiales por categoria de AWS Architecture Icons
CAT = {'compute': '#ED7100', 'container': '#ED7100', 'devtools': '#C925D1', 'db': '#C925D1',
       'storage': '#7AA116', 'net': '#8C4FFF', 'sec': '#DD344C', 'mgmt': '#E7157B'}

class D:
    def __init__(s, name):
        s.name, s.cells, s.n = name, [], 0
    def id(s):
        s.n += 1; return 'n%d' % s.n
    def add(s, style, x, y, w, h, value='', vertex=True):
        i = s.id()
        s.cells.append('<mxCell id="%s" value="%s" style="%s" vertex="1" parent="1"><mxGeometry x="%d" y="%d" width="%d" height="%d" as="geometry"/></mxCell>'
                       % (i, escape(value, {'"': '&quot;'}), style, x, y, w, h))
        return i
    def icon(s, label, res, cat, x, y, size=56, lw=200, right=False):
        pos = ('labelPosition=right;verticalLabelPosition=middle;verticalAlign=middle;align=left;spacingLeft=6;' if right
               else 'verticalLabelPosition=bottom;verticalAlign=top;align=center;')
        st = ('sketch=0;outlineConnect=0;fontColor=#232F3E;fillColor=%s;strokeColor=#ffffff;dashed=0;'
              + pos + 'html=1;fontSize=15;aspect=fixed;'
              'shape=mxgraph.aws4.resourceIcon;resIcon=mxgraph.aws4.%s;whiteSpace=wrap;labelWidth=%d;') % (CAT[cat], res, lw)
        return s.add(st, x, y, size, size, label)
    def group(s, label, gr, color, x, y, w, h, dashed=0, fc='none'):
        st = ('points=[];outlineConnect=0;gradientColor=none;html=1;whiteSpace=wrap;fontSize=17;fontStyle=1;'
              'container=0;pointerEvents=0;collapsible=0;recursiveResize=0;shape=mxgraph.aws4.group;grIcon=mxgraph.aws4.%s;'
              'strokeColor=%s;fillColor=%s;verticalAlign=top;align=left;spacingLeft=30;fontColor=%s;dashed=%d;') % (gr, color, fc, color, dashed)
        return s.add(st, x, y, w, h, label)
    def box(s, html, x, y, w, h, fill='#FFFFFF', stroke='#545B64', size=14, dashed=0):
        st = ('rounded=1;arcSize=6;whiteSpace=wrap;html=1;fillColor=%s;strokeColor=%s;fontSize=%d;fontColor=#232F3E;dashed=%d;'
              'align=center;verticalAlign=middle;spacing=6;') % (fill, stroke, size, dashed)
        return s.add(st, x, y, w, h, html)
    def zone(s, label, x, y, w, h):
        st = ('rounded=0;whiteSpace=wrap;html=1;fillColor=none;strokeColor=#147EBA;dashed=1;fontColor=#147EBA;'
              'fontSize=15;fontStyle=1;verticalAlign=top;align=center;')
        return s.add(st, x, y, w, h, label)
    def badge(s, text, color, x, y, w=700):
        return s.add('rounded=1;arcSize=12;whiteSpace=wrap;html=1;fillColor=%s;strokeColor=%s;fontSize=18;fontColor=#FFFFFF;' % (color, color),
                     x, y, w, 40, text)
    def edge(s, a, b, label='', dashed=0, ports='', pos=0, pts=()):
        i = s.id()
        s.cells.append('<mxCell id="%s" value="%s" style="edgeStyle=orthogonalEdgeStyle;rounded=0;html=1;endArrow=block;endFill=1;'
                       'strokeColor=#545B64;strokeWidth=1.5;fontSize=13;fontColor=#232F3E;labelBackgroundColor=#FFFFFF;dashed=%d;%s" '
                       'edge="1" parent="1" source="%s" target="%s"><mxGeometry x="%s" relative="1" as="geometry">%s</mxGeometry></mxCell>'
                       % (i, escape(label), dashed, ports, a, b, pos,
                          ('<Array as="points">%s</Array>' % ''.join('<mxPoint x="%d" y="%d"/>' % q for q in pts)) if pts else ''))
    def save(s, fname):
        xml = ('<mxfile host="app.diagrams.net"><diagram name="%s" id="%s"><mxGraphModel dx="1600" dy="1000" grid="1" gridSize="10" '
               'guides="1" tooltips="1" connect="1" arrows="1" fold="1" page="0" pageScale="1" math="0" shadow="0"><root>'
               '<mxCell id="0"/><mxCell id="1" parent="0"/>%s</root></mxGraphModel></diagram></mxfile>') % (s.name, fname[:2], ''.join(s.cells))
        open(os.path.join(OUT, fname), 'w', encoding='utf-8').write(xml)

B = lambda t: '<b>%s</b>' % t
NUBE, MIX = '#1A73E8', '#7B3FA0'

def cadena(d, y0=90):
    """Cadena de entrega del equipo de desarrollo (N-04, sa-east-1). Devuelve el id de ECR."""
    d.add('rounded=1;arcSize=6;whiteSpace=wrap;html=1;fillColor=#232F3E;strokeColor=#232F3E;fontSize=15;fontColor=#FFFFFF;', 20, y0, 230, 56, B('Cadena de entrega') + '<br>N-04 · sa-east-1')
    dev = d.add('sketch=0;outlineConnect=0;fontColor=#232F3E;fillColor=#232F3E;strokeColor=none;dashed=0;verticalLabelPosition=bottom;'
                'labelPosition=right;verticalLabelPosition=middle;verticalAlign=middle;align=left;html=1;fontSize=15;aspect=fixed;shape=mxgraph.aws4.users;', 40, y0 + 80, 50, 50,
                'Equipo de desarrollo')
    git = d.box(B('GitLab CI') + '<br>por suscripción', 20, y0 + 175, 170, 56, fill='#FFF2E8', stroke='#E67E22')
    cb = d.icon('AWS CodeBuild<br>(SLSA nivel 3)', 'codebuild', 'devtools', 40, y0 + 270, right=True)
    ecr = d.icon('Amazon ECR<br>(imagen firmada)', 'ecr', 'container', 40, y0 + 390, right=True)
    d.edge(dev, git); d.edge(git, cb); d.edge(cb, ecr)
    return ecr

def cuenta(d, nombre, region, vpc, x, y, w, h):
    d.group('AWS Cloud · organización AWS Control Tower', 'group_aws_cloud_alt', '#232F3E', x, y, w, h)
    d.group('Cuenta AWS · %s' % nombre, 'group_account', '#CD2264', x + 20, y + 40, w - 40, h - 60)
    d.group(region, 'group_region', '#00A4A6', x + 40, y + 85, w - 80, h - 125, dashed=1)
    return d.group(vpc, 'group_vpc2', '#8C4FFF', x + 60, y + 130, w - 120, h - 190)

# ---------------------------------------------------------------- A1 Desarrollo
d = D('Desarrollo')
d.badge(B('Tipo de ambiente:') + ' solo nube (AWS)', NUBE, 20, 20)
ecr = cadena(d)
cuenta(d, 'Desarrollo', 'sa-east-1 (São Paulo)', 'VPC Desarrollo · 10.104.0.0/16', 300, 80, 1000, 560)
far = d.icon('ECS Fargate (N-04)<br>imagen Laravel 13 · PHP 8.5', 'fargate', 'compute', 420, 270, lw=240)
d.box(B('Pruebas unitarias'), 620, 250, 260, 50)
d.box('Datos sintéticos o anonimizados', 620, 320, 260, 50, fill='#F5E6FA', stroke='#C925D1')
d.box('Aislado y reconstruible desde código<br>Se reduce o apaga fuera del horario de uso', 620, 390, 260, 80, fill='#F4F6F6')
d.icon('AWS Secrets Manager', 'secrets_manager', 'sec', 960, 250)
d.icon('Amazon S3 privado<br>(portales N-01 a N-03)', 's3', 'storage', 960, 380)
d.icon('Amazon CloudFront', 'cloudfront', 'net', 1120, 380)
d.edge(ecr, far, 'despliega la misma imagen', ports='exitX=1;exitY=0.5;entryX=0;entryY=0.5;', pos=0.6)
d.save('A1_Ambiente_Desarrollo.drawio')

# ---------------------------------------------------------------- A2 QA
d = D('QA')
d.badge(B('Tipo de ambiente:') + ' solo nube (AWS)', NUBE, 20, 20)
ecr = cadena(d)
cuenta(d, 'QA', 'sa-east-1 (São Paulo)', 'VPC QA · 10.103.0.0/16', 300, 80, 1000, 620)
far = d.icon('ECS Fargate (N-04)<br>misma imagen; perfil wms_only', 'fargate', 'compute', 420, 270, lw=240)
d.box(B('Pruebas funcionales, de integración y de regresión automatizadas') + '<br>Análisis dinámico', 620, 240, 290, 80)
d.box('Verificador local de identidad y puerta de API local del WMS', 620, 335, 290, 60, fill='#FCE4EC', stroke='#DD344C')
d.box('Adaptadores simulados del ERP', 620, 410, 290, 45, fill='#FCE4EC', stroke='#DD344C')
d.box('Ensayo de corte de enlace y relevo de turno', 620, 470, 290, 45)
d.box('Datos de prueba versionados<br>Aislado y reconstruible desde código · se reduce o apaga fuera de horario', 380, 550, 530, 60, fill='#F5E6FA', stroke='#C925D1')
d.icon('AWS Secrets Manager', 'secrets_manager', 'sec', 990, 250)
d.icon('Amazon S3 privado<br>(portales N-01 a N-03)', 's3', 'storage', 990, 390)
d.icon('Amazon CloudFront', 'cloudfront', 'net', 1150, 390)
d.edge(ecr, far, 'despliega la misma imagen', ports='exitX=1;exitY=0.5;entryX=0;entryY=0.5;', pos=0.6)
d.save('A2_Ambiente_QA.drawio')

# ---------------------------------------------------------------- A3 Preproduccion
d = D('Preproducción')
d.badge(B('Tipo de ambiente:') + ' solo nube (AWS) · el sitio on-premise se emula en una VPC', NUBE, 20, 20, 900)
ecr = cadena(d)
cuenta(d, 'Preproducción', 'sa-east-1 (São Paulo)', 'VPC Preproducción · 10.102.0.0/16 · misma topología de nube que Producción', 300, 80, 1500, 700)
alb = d.icon('Application Load Balancer privado', 'elastic_load_balancing', 'net', 400, 245, right=True, lw=260)
d.zone('Zona sa-east-1a', 390, 340, 330, 250); d.zone('Zona sa-east-1b', 750, 340, 330, 250)
f1 = d.icon('ECS Fargate (N-04)<br>perfil API', 'fargate', 'compute', 520, 380)
d.icon('ECS Fargate (N-04)<br>perfil API', 'fargate', 'compute', 880, 380)
d.icon('Aurora PostgreSQL (N-05)<br>escritor', 'aurora', 'db', 520, 490)
d.icon('Aurora PostgreSQL (N-05)<br>lector', 'aurora', 'db', 880, 490)
d.box('ECS Fargate (N-04): consumidor de reconciliación · trabajos · planificador · motor de rutas M4 · AS2 M11', 390, 620, 690, 50, fill='#FFF2E8', stroke='#ED7100')
d.icon('AWS Secrets Manager', 'secrets_manager', 'sec', 1140, 250)
d.icon('Amazon S3 privado<br>(portales N-01 a N-03)', 's3', 'storage', 1140, 370)
d.icon('Amazon CloudFront', 'cloudfront', 'net', 1140, 490)
d.icon('Amazon Macie<br>(verifica datos sintéticos)', 'macie', 'sec', 1140, 610)
d.group('Sitio on-premise emulado · VPC propia', 'group_vpc2', '#8C4FFF', 1330, 230, 390, 250)
d.box('Misma imagen: ' + B('wms_only') + ' · broker · verificador local', 1350, 290, 350, 50)
d.box(B('Sin túnel hacia las bodegas'), 1350, 360, 350, 50, fill='#FCE4EC', stroke='#DD344C')
d.box(B('Aceptación, carga, resiliencia y ensayo del paso a producción') +
      '<br>Se reduce o apaga fuera de horario; dimensionamiento completo en las pruebas de carga', 1330, 510, 390, 110, fill='#F4F6F6')
fb = [c for c in d.cells if 'ECS Fargate (N-04): consumidor' in c][0].split('"')[1]
d.edge(ecr, f1, 'despliega la misma imagen', ports='exitX=1;exitY=0.5;entryX=0;entryY=0.5;', pos=0.3)
d.save('A3_Ambiente_Preproduccion.drawio')

# ---------------------------------------------------------------- A4 Produccion
d = D('Producción')
d.badge(B('Tipo de ambiente:') + ' mixto (nube + on-premise)', MIX, 20, 20)
ecr = cadena(d)
d.box(B('Paso a Producción automático') + '<br>sin intervención manual (RT-04.06)', 20, 650, 230, 70, fill='#F4F6F6')
cuenta(d, 'Producción', 'sa-east-1 (São Paulo) · región primaria', 'VPC Producción · 10.101.0.0/16', 300, 80, 1150, 720)
alb = d.icon('Application Load Balancer privado', 'elastic_load_balancing', 'net', 400, 245, right=True, lw=260)
d.zone('Zona sa-east-1a', 390, 340, 330, 250); d.zone('Zona sa-east-1b', 750, 340, 330, 250)
f1 = d.icon('ECS Fargate (N-04)<br>perfil API', 'fargate', 'compute', 520, 380)
d.icon('ECS Fargate (N-04)<br>perfil API', 'fargate', 'compute', 880, 380)
d.icon('Aurora PostgreSQL (N-05)<br>escritor · migraciones', 'aurora', 'db', 520, 490)
d.icon('Aurora PostgreSQL (N-05)<br>lector promovible', 'aurora', 'db', 880, 490)
d.box('ECS Fargate (N-04): consumidor de reconciliación · trabajos · planificador · motor de rutas M4 · AS2 M11', 390, 620, 690, 50, fill='#FFF2E8', stroke='#ED7100')
d.icon('AWS Secrets Manager', 'secrets_manager', 'sec', 1140, 250)
d.icon('Amazon S3 privado<br>(portales N-01 a N-03)', 's3', 'storage', 1140, 370)
d.icon('Amazon CloudFront', 'cloudfront', 'net', 1140, 490)
d.icon('AWS Systems Manager<br>Session Manager (acceso excepcional)', 'systems_manager', 'mgmt', 1140, 610, lw=230)
op = d.group('On-premise · parte de Producción', 'group_corporate_data_center', '#7D8998', 1500, 80, 470, 720)
d.box(B('CD Talca · Proxmox VE, 3 nodos') + '<br>VM-01: A-01 Motor WMS (wms_only)<br>VM-03: A-03 Broker y shipper', 1520, 140, 430, 100, fill='#F4F6F6')
d.box(B('CD Concepción · Proxmox VE') + '<br>VM-C01: A-01 Motor WMS (wms_only)<br>VM-C04: A-03 Broker y shipper', 1520, 270, 430, 100, fill='#F4F6F6')
d.box(B('Cross-docking (3) · E-01 WMS de cross-docking') + '<br>Docker Compose: wms_only, shipper, PostgreSQL, RabbitMQ y caché de identidad', 1520, 400, 430, 100, fill='#F4F6F6')
sit = d.box('Primera instalación de cada versión: sitio por sitio', 1520, 540, 430, 50)
d.box('Contenedores de la misma imagen; infraestructura de cada sitio declarada como código versionado', 1520, 610, 430, 70, fill='#F4F6F6')
fb = [c for c in d.cells if 'ECS Fargate (N-04): consumidor' in c][0].split('"')[1]
d.edge(ecr, f1, 'despliega la misma imagen', ports='exitX=1;exitY=0.5;entryX=0;entryY=0.5;', pos=0.3)
d.edge(ecr, sit, 'misma imagen a los sitios (wms_only y shipper), sitio por sitio', dashed=1, ports='exitX=0.5;exitY=1;entryX=0;entryY=0.5;', pos=0.5, pts=((68, 610), (275, 610), (275, 830), (1480, 830), (1480, 565)))
d.save('A4_Ambiente_Produccion.drawio')

# ---------------------------------------------------------------- A5 Recuperacion
d = D('Recuperación ante Desastres')
d.badge(B('Tipo de ambiente:') + ' mixto (nube + on-premise)', MIX, 20, 20)
cuenta(d, 'Recuperación ante Desastres', 'us-east-1 · ≈ 7.700 km de la primaria', 'VPC Recuperación · 10.201.0.0/16', 20, 80, 900, 520)
d.icon('ECS Fargate (N-04)<br>réplica reducida<br>carga completa en &lt; 30 min', 'fargate', 'compute', 170, 260, lw=220)
d.icon('Aurora Global Database (N-05)<br>réplica promovible', 'aurora', 'db', 460, 260, lw=240)
d.icon('AWS Backup (N-11)<br>copias entre regiones', 'backup', 'storage', 720, 260)
d.box('Keycloak (A-05), API pública y privada y Verified Access: se restituyen en la conmutación (paso 6, Tabla 4.3-6)', 110, 420, 740, 60, fill='#F4F6F6')
d.group('On-premise · recuperación del dominio on-premise', 'group_corporate_data_center', '#7D8998', 960, 80, 470, 520)
t = d.box(B('CD Talca') + '<br>VM-01: A-01 Motor WMS · VM-02: A-02 Base transaccional', 990, 150, 410, 80, fill='#F4F6F6')
c = d.box(B('CD Concepción') + '<br>VM-C01 promueve su A-01 Motor WMS<br>RTO adicional de 1 a 2 h', 990, 320, 410, 90, fill='#F4F6F6')
d.edge(t, c, 'DRP local · ≈ 200 km', dashed=1)
d.save('A5_Ambiente_Recuperacion_Desastres.drawio')
print('ok')
