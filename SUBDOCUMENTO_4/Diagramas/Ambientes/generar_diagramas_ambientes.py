# Genera los 5 diagramas de ambientes del apartado de despliegue (11_j_despliegue.tex).
#
# Criterio: cada diagrama muestra solo lo que interviene en la secuencia de despliegue de su
# ambiente, con los nombres y codigos del informe. El unico texto explicativo es la leyenda
# "Secuencia de despliegue"; los circulos numerados ubican cada paso en el dibujo.
#
# Ubicacion AWS coherente: dentro de la VPC solo lo que vive en ella (ALB, ECS Fargate, Aurora);
# los servicios regionales (S3, Secrets Manager, Parameter Store) en la region, fuera de la VPC;
# CloudFront, que es global, en la cuenta y fuera de la region.
import os
from xml.sax.saxutils import escape

OUT = os.path.dirname(os.path.abspath(__file__))
CAT = {'compute': '#ED7100', 'container': '#ED7100', 'devtools': '#C925D1', 'db': '#C925D1',
       'storage': '#7AA116', 'net': '#8C4FFF', 'sec': '#DD344C', 'mgmt': '#E7157B'}
PASO = '#D6246E'
NUBE, MIX = '#1A73E8', '#7B3FA0'
B = lambda t: '<b>%s</b>' % t


class D:
    def __init__(s, name):
        s.name, s.cells, s.n = name, [], 0

    def _id(s):
        s.n += 1
        return 'n%d' % s.n

    def add(s, style, x, y, w, h, value=''):
        i = s._id()
        s.cells.append('<mxCell id="%s" value="%s" style="%s" vertex="1" parent="1">'
                       '<mxGeometry x="%d" y="%d" width="%d" height="%d" as="geometry"/></mxCell>'
                       % (i, escape(value, {'"': '&quot;'}), style, x, y, w, h))
        return i

    def icon(s, label, res, cat, x, y, lw=170, right=False):
        pos = ('labelPosition=right;verticalLabelPosition=middle;verticalAlign=middle;align=left;spacingLeft=6;' if right
               else 'verticalLabelPosition=bottom;verticalAlign=top;align=center;')
        st = ('sketch=0;outlineConnect=0;fontColor=#232F3E;fillColor=%s;strokeColor=#ffffff;dashed=0;%s'
              'html=1;fontSize=15;aspect=fixed;shape=mxgraph.aws4.resourceIcon;resIcon=mxgraph.aws4.%s;'
              'whiteSpace=wrap;labelWidth=%d;') % (CAT[cat], pos, res, lw)
        return s.add(st, x, y, 56, 56, label)

    def group(s, label, gr, color, x, y, w, h, dashed=0):
        st = ('points=[];outlineConnect=0;gradientColor=none;html=1;whiteSpace=wrap;fontSize=16;fontStyle=1;'
              'container=0;pointerEvents=0;collapsible=0;recursiveResize=0;shape=mxgraph.aws4.group;'
              'grIcon=mxgraph.aws4.%s;strokeColor=%s;fillColor=none;verticalAlign=top;align=left;spacingLeft=30;'
              'fontColor=%s;dashed=%d;') % (gr, color, color, dashed)
        return s.add(st, x, y, w, h, label)

    def zone(s, label, x, y, w, h):
        return s.add('rounded=0;whiteSpace=wrap;html=1;fillColor=none;strokeColor=#147EBA;dashed=1;'
                     'fontColor=#147EBA;fontSize=14;fontStyle=1;verticalAlign=top;align=center;', x, y, w, h, label)

    def box(s, html, x, y, w, h, fill='#F4F6F6', stroke='#545B64'):
        return s.add('rounded=1;arcSize=6;whiteSpace=wrap;html=1;fillColor=%s;strokeColor=%s;fontSize=14;'
                     'fontColor=#232F3E;align=center;verticalAlign=middle;spacing=6;' % (fill, stroke), x, y, w, h, html)

    def badge(s, text, color, w):
        return s.add('rounded=1;arcSize=12;whiteSpace=wrap;html=1;fillColor=%s;strokeColor=%s;fontSize=17;'
                     'fontColor=#FFFFFF;' % (color, color), 20, 20, w, 38, text)

    def paso(s, n, x, y):
        return s.add('ellipse;whiteSpace=wrap;html=1;aspect=fixed;fillColor=%s;strokeColor=#FFFFFF;strokeWidth=2;'
                     'fontColor=#FFFFFF;fontStyle=1;fontSize=16;align=center;verticalAlign=middle;' % PASO,
                     x, y, 30, 30, str(n))

    def leyenda(s, pasos, y, w):
        filas = ''.join('<tr><td style="vertical-align:top;padding:2px 8px 2px 0"><b style="color:%s">%d</b></td>'
                        '<td style="padding:2px 0">%s</td></tr>' % (PASO, i + 1, t) for i, t in enumerate(pasos))
        html = '<b>Secuencia de despliegue</b><table style="font-size:14px;margin-top:4px">%s</table>' % filas
        return s.add('rounded=1;arcSize=4;whiteSpace=wrap;html=1;fillColor=#F4F6F6;strokeColor=#545B64;fontSize=15;'
                     'fontColor=#232F3E;align=left;verticalAlign=top;spacing=10;', 20, y, w, 46 + 26 * len(pasos), html)

    def edge(s, a, b, ports='', dashed=0, pts=(), label=''):
        i = s._id()
        arr = ('<Array as="points">%s</Array>' % ''.join('<mxPoint x="%d" y="%d"/>' % q for q in pts)) if pts else ''
        s.cells.append('<mxCell id="%s" value="%s" style="edgeStyle=orthogonalEdgeStyle;rounded=0;html=1;endArrow=block;'
                       'endFill=1;strokeColor=#545B64;strokeWidth=1.5;fontSize=13;fontColor=#232F3E;'
                       'labelBackgroundColor=#FFFFFF;dashed=%d;%s" edge="1" parent="1" source="%s" target="%s">'
                       '<mxGeometry relative="1" as="geometry">%s</mxGeometry></mxCell>'
                       % (i, escape(label), dashed, ports, a, b, arr))

    def save(s, fname):
        xml = ('<mxfile host="app.diagrams.net"><diagram name="%s" id="%s"><mxGraphModel dx="1600" dy="1000" grid="1" '
               'gridSize="10" guides="1" tooltips="1" connect="1" arrows="1" fold="1" page="0" pageScale="1" math="0" '
               'shadow="0"><root><mxCell id="0"/><mxCell id="1" parent="0"/>%s</root></mxGraphModel></diagram></mxfile>'
               % (s.name, fname[:2], ''.join(s.cells)))
        open(os.path.join(OUT, fname), 'w', encoding='utf-8').write(xml)


R = lambda y: 'exitX=1;exitY=%s;entryX=0;entryY=0.5;' % y
COMUNES = ['GitLab CI orquesta el cambio y ejecuta los controles; bloquea ante hallazgos críticos o altos (RT-04.05)',
           'AWS CodeBuild construye la imagen de forma hermética (SLSA nivel 3)',
           'Amazon ECR guarda la imagen firmada, que se promueve por su digest sin recompilar']


def cadena(d):
    """Pasos 1 a 3, comunes a los cinco ambientes. Devuelve el id de ECR."""
    d.add('rounded=1;arcSize=6;whiteSpace=wrap;html=1;fillColor=#232F3E;strokeColor=#232F3E;fontSize=15;'
          'fontColor=#FFFFFF;', 20, 80, 240, 50, B('Cadena de entrega') + '<br>N-04 · sa-east-1')
    dev = d.add('sketch=0;outlineConnect=0;fontColor=#232F3E;fillColor=#232F3E;strokeColor=none;dashed=0;'
                'labelPosition=right;verticalLabelPosition=middle;verticalAlign=middle;align=left;spacingLeft=4;'
                'html=1;fontSize=15;aspect=fixed;shape=mxgraph.aws4.users;', 40, 160, 50, 50, 'Equipo de desarrollo')
    git = d.box(B('GitLab CI'), 20, 250, 170, 50, fill='#FFF2E8', stroke='#E67E22')
    cb = d.icon('AWS CodeBuild', 'codebuild', 'devtools', 40, 350, right=True)
    ecr = d.icon('Amazon ECR', 'ecr', 'container', 40, 470)
    d.edge(dev, git); d.edge(git, cb); d.edge(cb, ecr)
    d.paso(1, 176, 238); d.paso(2, 6, 342); d.paso(3, 6, 462)
    return ecr


def nube(d, cuenta, region, x, y, w, h, rw):
    """Nube, cuenta y region. La region deja a su derecha, dentro de la cuenta, el espacio para CloudFront."""
    d.group('AWS Cloud · organización AWS Control Tower', 'group_aws_cloud_alt', '#232F3E', x, y, w, h)
    d.group('Cuenta AWS · ' + cuenta, 'group_account', '#CD2264', x + 20, y + 40, w - 40, h - 60)
    d.group(region, 'group_region', '#00A4A6', x + 40, y + 85, rw, h - 125, dashed=1)


def servicios_regionales(d, x, y, paso_portales):
    """Secrets Manager y Parameter Store (configuracion del paso de despliegue) y S3 de los portales."""
    d.icon('AWS Secrets Manager', 'secrets_manager', 'sec', x, y, lw=150)
    d.icon('SSM Parameter Store', 'systems_manager', 'mgmt', x + 160, y, lw=150)
    s3 = d.icon('Amazon S3<br>portales N-01 a N-03', 's3', 'storage', x, y + 150, lw=170)
    d.paso(paso_portales, x - 34, y + 140)
    return s3


def cloudfront(d, s3, x, y):
    cf = d.icon('Amazon CloudFront', 'cloudfront', 'net', x, y, lw=150)
    d.edge(s3, cf, R(0.5))


# ------------------------------------------------------------------ Desarrollo y QA
def ambiente_simple(nombre, vpc, fname):
    d = D(nombre)
    d.badge(B('Tipo de ambiente:') + ' solo nube (AWS)', NUBE, 460)
    ecr = cadena(d)
    nube(d, nombre, 'sa-east-1 (São Paulo)', 320, 80, 880, 520, 620)
    d.group(vpc, 'group_vpc2', '#8C4FFF', 380, 210, 280, 200)
    far = d.icon('ECS Fargate (N-04)', 'fargate', 'compute', 490, 290)
    d.paso(4, 456, 280)
    s3 = servicios_regionales(d, 720, 230, 5)
    cloudfront(d, s3, 1060, 380)
    d.edge(ecr, far, R(0.5))
    d.leyenda(COMUNES + ['Despliegue de la imagen en ECS Fargate, con su configuración (Parameter Store) y sus secretos (Secrets Manager)',
                         'Publicación de los portales Angular en S3 privado, servidos por CloudFront'], 640, 900)
    d.save(fname)


ambiente_simple('Desarrollo', 'VPC Desarrollo · 10.104.0.0/16', 'A1_Ambiente_Desarrollo.drawio')
ambiente_simple('QA', 'VPC QA · 10.103.0.0/16', 'A2_Ambiente_QA.drawio')


# ------------------------------------------------------------------ Preproduccion y Produccion
def vpc_productiva(d, titulo):
    """VPC con la topologia de Produccion (RT-04.02): ALB privado, Fargate en dos zonas y Aurora escritor."""
    d.group(titulo, 'group_vpc2', '#8C4FFF', 380, 210, 680, 440)
    d.icon('Application Load Balancer privado', 'elastic_load_balancing', 'net', 410, 250, lw=280, right=True)
    d.zone('Zona sa-east-1a', 400, 330, 310, 290)
    d.zone('Zona sa-east-1b', 730, 330, 310, 290)
    f1 = d.icon('ECS Fargate (N-04)', 'fargate', 'compute', 527, 380)
    d.icon('ECS Fargate (N-04)', 'fargate', 'compute', 857, 380)
    au = d.icon('Aurora PostgreSQL (N-05)<br>escritor', 'aurora', 'db', 527, 510, lw=220)
    d.paso(4, 493, 500); d.paso(5, 493, 370)
    return f1, au


PASO4 = 'Migraciones Laravel aditivas y reversibles en Aurora, antes de cambiar el tráfico (RT-04.10)'
PASO_PORTALES = 'Publicación de los portales Angular en S3 privado, servidos por CloudFront'

# Preproduccion
d = D('Preproducción')
d.badge(B('Tipo de ambiente:') + ' solo nube (AWS) · el sitio on-premise se emula en una VPC', NUBE, 800)
ecr = cadena(d)
nube(d, 'Preproducción', 'sa-east-1 (São Paulo)', 320, 80, 1440, 700, 1160)
f1, au = vpc_productiva(d, 'VPC Preproducción · 10.102.0.0/16')
d.group('Sitio on-premise emulado · VPC propia', 'group_vpc2', '#8C4FFF', 1100, 210, 390, 150)
d.box(B('wms_only') + ' · broker · verificador local', 1125, 270, 345, 56, fill='#FFFFFF')
d.paso(5, 1091, 258)
s3 = servicios_regionales(d, 1120, 420, 6)
cloudfront(d, s3, 1600, 570)
d.edge(ecr, au, R(0.75)); d.edge(ecr, f1, R(0.25))
d.leyenda(COMUNES + [PASO4,
                     'Despliegue azul-verde con canario en ECS Fargate y en el sitio emulado, con su configuración y sus secretos (RT-04.07)',
                     PASO_PORTALES], 820, 960)
d.save('A3_Ambiente_Preproduccion.drawio')

# Produccion
d = D('Producción')
d.badge(B('Tipo de ambiente:') + ' mixto (nube + on-premise)', MIX, 520)
ecr = cadena(d)
nube(d, 'Producción', 'sa-east-1 (São Paulo) · región primaria', 320, 80, 1440, 700, 1160)
f1, au = vpc_productiva(d, 'VPC Producción · 10.101.0.0/16')
d.group('VPC Hub', 'group_vpc2', '#8C4FFF', 1100, 210, 390, 150)
tgw = d.icon('AWS Transit Gateway', 'transit_gateway', 'net', 1380, 250, lw=160)
d.paso(7, 1346, 240)
s3 = servicios_regionales(d, 1170, 420, 6)
cloudfront(d, s3, 1600, 570)
d.group('On-premise · parte de Producción', 'group_corporate_data_center', '#7D8998', 1800, 80, 440, 700)
sitios = [d.box(B('CD Talca · Proxmox VE') + '<br>VM-01: A-01 (wms_only) · VM-03: A-03 y shipper', 1820, 150, 400, 70),
          d.box(B('CD Concepción · Proxmox VE') + '<br>VM-C01: A-01 (wms_only) · VM-C04: A-03 y shipper', 1820, 290, 400, 70),
          d.box(B('Cross-docking (3) · E-01') + '<br>Docker Compose: wms_only y shipper', 1820, 430, 400, 70)]
d.edge(ecr, au, R(0.75)); d.edge(ecr, f1, R(0.25))
d.edge(ecr, tgw, 'exitX=0;exitY=0.5;entryX=0;entryY=0.5;', dashed=1, pts=((14, 498), (14, 820), (1080, 820), (1080, 278)))
for i, sid in enumerate(sitios):
    d.edge(tgw, sid, R(0.5), dashed=1, label='VPN' if i == 0 else '')
d.leyenda(COMUNES + [PASO4,
                     'Despliegue azul-verde con canario en ECS Fargate, con su configuración y sus secretos; paso automático, sin intervención manual (RT-04.06, RT-04.07)',
                     PASO_PORTALES,
                     'Sitios on-premise: descarga de la misma imagen desde ECR por la VPN (VPC Hub) y los endpoints de interfaz; Ansible (F-02) actualiza los contenedores, sitio por sitio'],
          860, 1100)
d.save('A4_Ambiente_Produccion.drawio')

# ------------------------------------------------------------------ Recuperacion ante Desastres
d = D('Recuperación ante Desastres')
d.badge(B('Tipo de ambiente:') + ' mixto (nube + on-premise) · un sitio de recuperación por dominio', MIX, 760)
ecr = cadena(d)
d.group('AWS Cloud · organización AWS Control Tower', 'group_aws_cloud_alt', '#232F3E', 320, 80, 620, 460)
d.group('Cuenta AWS · Recuperación ante Desastres', 'group_account', '#CD2264', 340, 120, 580, 400)
d.group('us-east-1 · ≈ 7.700 km de la primaria', 'group_region', '#00A4A6', 360, 165, 540, 335, dashed=1)
d.group('VPC Recuperación · 10.201.0.0/16', 'group_vpc2', '#8C4FFF', 380, 210, 380, 250)
far = d.icon('ECS Fargate (N-04)<br>réplica reducida', 'fargate', 'compute', 540, 300)
d.paso(4, 506, 290)
d.edge(ecr, far, R(0.5))
d.group('On-premise · sitio de recuperación', 'group_corporate_data_center', '#7D8998', 990, 80, 440, 460)
t = d.box(B('CD Talca') + '<br>VM-01: A-01 Motor WMS', 1010, 150, 400, 70)
c = d.box(B('CD Concepción') + '<br>VM-C01: A-01 Motor WMS', 1010, 340, 400, 70)
d.paso(5, 976, 330)
d.edge(t, c, 'exitX=0.5;exitY=1;entryX=0.5;entryY=0;', dashed=1, label='DRP local')
d.leyenda(COMUNES + ['La réplica reducida de ECS Fargate en us-east-1 recibe cada versión liberada en Producción, desde el ECR de sa-east-1',
                     'Si se pierde Talca, el CD Concepción promueve VM-C01 con la misma imagen que recibió en Producción (RTO adicional de 1 a 2 h)'],
          580, 900)
d.save('A5_Ambiente_Recuperacion_Desastres.drawio')
print('ok')
