# Genera los 5 diagramas de ambientes del apartado de despliegue (11_j_despliegue.tex).
#
# Criterio: cada diagrama muestra solo lo que interviene en la secuencia de despliegue de su
# ambiente, con los nombres y codigos del informe. El unico texto explicativo es la leyenda
# "Secuencia de despliegue"; los circulos numerados ubican cada paso en el dibujo.
#
# Todo elemento dibujado participa en un paso numerado. No se dibujan servicios que solo se usan en
# tiempo de ejecucion (Secrets Manager, Parameter Store) ni componentes que la imagen no toca
# (broker, verificador local, segunda zona).
#
# Ubicacion AWS coherente: dentro de la VPC solo lo que vive en ella (ALB, ECS Fargate, Aurora);
# S3 en la region, fuera de la VPC; CloudFront, que es global, en la cuenta y fuera de la region.
import os
import re
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

    def group(s, label, gr, color, x, y, w, h, dashed=0, valign='top'):
        st = ('points=[];outlineConnect=0;gradientColor=none;html=1;whiteSpace=wrap;fontSize=16;fontStyle=1;'
              'container=0;pointerEvents=0;collapsible=0;recursiveResize=0;shape=mxgraph.aws4.group;'
              'grIcon=mxgraph.aws4.%s;strokeColor=%s;fillColor=none;verticalAlign=%s;align=left;spacingLeft=30;spacingBottom=6;'
              'fontColor=%s;dashed=%d;') % (gr, color, valign, color, dashed)
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
                     'fontColor=#232F3E;align=left;verticalAlign=top;spacing=10;', 20, y, w,
                     40 + sum(21 * (1 + len(re.sub('<[^>]+>', '', t)) // int((w - 60) / 6.6)) + 5 for t in pasos), html)

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
COMUNES = ['GitLab CI orquesta el pipeline; cada cambio instala sus dependencias según composer.lock y pasa por los controles (RT-04.05)',
           'AWS CodeBuild construye cada imagen de forma hermética, con procedencia SLSA nivel 3; el pipeline bloquea ante un hallazgo crítico o alto, un contrato público roto sin versión nueva o una cobertura inferior al 70 % (RT-04.11)',
           'La imagen aprobada se firma, se publica en Elastic Container Registry y se promueve por su digest, de modo que ningún ambiente recompila']


def cadena(d):
    """Pasos 1 a 3, comunes a los cinco ambientes. Devuelve (GitLab CI, ECR)."""
    d.add('rounded=1;arcSize=6;whiteSpace=wrap;html=1;fillColor=#232F3E;strokeColor=#232F3E;fontSize=15;'
          'fontColor=#FFFFFF;', 20, 80, 240, 50, B('Cadena de entrega'))
    dev = d.add('sketch=0;outlineConnect=0;fontColor=#232F3E;fillColor=#232F3E;strokeColor=none;dashed=0;'
                'labelPosition=right;verticalLabelPosition=middle;verticalAlign=middle;align=left;spacingLeft=4;'
                'html=1;fontSize=15;aspect=fixed;shape=mxgraph.aws4.users;', 40, 160, 50, 50, 'Equipo de desarrollo')
    # GitLab CI es un servicio contratado por suscripcion, fuera de AWS
    git = d.box(B('GitLab CI') + '<br>(suscripción)', 20, 250, 170, 50, fill='#FFF2E8', stroke='#E67E22')
    # CodeBuild y ECR son servicios de AWS (N-04, sa-east-1); el informe no fija la cuenta
    d.group('AWS Cloud · sa-east-1 · N-04', 'group_aws_cloud_alt', '#232F3E', 20, 325, 270, 290, valign='bottom')
    cb = d.icon('AWS CodeBuild', 'codebuild', 'devtools', 72, 375, right=True)
    ecr = d.icon('Amazon ECR', 'ecr', 'container', 72, 480)
    d.edge(dev, git, 'exitX=0.5;exitY=1;entryX=0.3;entryY=0;')
    d.edge(git, cb, 'exitX=0.3;exitY=1;entryX=0.5;entryY=0;')
    d.edge(cb, ecr, 'exitX=0.5;exitY=1;entryX=0.5;entryY=0;')
    d.paso(1, 6, 238); d.paso(2, 36, 367); d.paso(3, 36, 472)
    return git, ecr


def nube(d, cuenta, region, x, y, w, h, rw):
    """Nube, cuenta y region. La region deja a su derecha, dentro de la cuenta, el espacio para CloudFront."""
    d.group('AWS Cloud · organización AWS Control Tower', 'group_aws_cloud_alt', '#232F3E', x, y, w, h)
    d.group('Cuenta AWS · ' + cuenta, 'group_account', '#CD2264', x + 20, y + 40, w - 40, h - 60)
    d.group(region, 'group_region', '#00A4A6', x + 40, y + 85, rw, h - 125, dashed=1)


def portales(d, git, n, xcf):
    """Paso de los portales: GitLab CI publica en S3 (fila superior de la region) y CloudFront los sirve."""
    s3 = d.icon('Amazon S3<br>portales N-01 a N-03', 's3', 'storage', 420, 247, lw=170)
    d.paso(n, 386, 237)
    cf = d.icon('Amazon CloudFront', 'cloudfront', 'net', xcf, 247, lw=150)
    d.edge(git, s3, R(0.5))
    d.edge(s3, cf, R(0.5))


PASO_DESPLIEGUE = 'El ambiente despliega la imagen en ECS Fargate, en su propia cuenta y desde el mismo ECR de sa-east-1, con la configuración externalizada por ambiente (RT-04.08)'
PASO_DESPLIEGUE_QA = 'QA despliega en ECS Fargate, en su propia cuenta, la misma imagen que recorrió Desarrollo, con la configuración externalizada por ambiente (RT-04.08)'
PASO_PORTALES = 'Los portales siguen el mismo ciclo: su aplicación Angular se publica por ambiente en S3 privado y CloudFront'
PASO_MIGRACIONES = 'Las migraciones Laravel, aditivas y reversibles, se ejecutan en Aurora como un paso único del despliegue, antes de cambiar el tráfico (RT-04.10)'


# ------------------------------------------------------------------ Desarrollo y QA
# 1-3 cadena, 4 despliegue en Fargate, 5 portales
def ambiente_simple(nombre, vpc, fname, paso4):
    d = D(nombre)
    d.badge(B('Tipo de ambiente:') + ' solo nube (AWS)', NUBE, 460)
    git, ecr = cadena(d)
    nube(d, nombre, 'sa-east-1 (São Paulo)', 320, 80, 780, 560, 540)
    portales(d, git, 5, 950)
    d.group(vpc, 'group_vpc2', '#8C4FFF', 380, 370, 320, 190)
    far = d.icon('ECS Fargate (N-04)', 'fargate', 'compute', 510, 450)
    d.paso(4, 476, 440)
    d.edge(ecr, far, R(0.5))
    d.leyenda(COMUNES + [paso4, PASO_PORTALES], 680, 1000)
    d.save(fname)


ambiente_simple('Desarrollo', 'VPC Desarrollo · 10.104.0.0/16', 'A1_Ambiente_Desarrollo.drawio', PASO_DESPLIEGUE)
ambiente_simple('QA', 'VPC QA · 10.103.0.0/16', 'A2_Ambiente_QA.drawio', PASO_DESPLIEGUE_QA)


# ------------------------------------------------------------------ Preproduccion y Produccion
def vpc_productiva(d, titulo, ecr):
    """VPC con la topologia de Produccion (RT-04.02): Aurora (paso 4), ECS Fargate en 2 zonas y el ALB privado
    que desplaza el trafico en el azul-verde con canario (paso 5)."""
    d.group(titulo, 'group_vpc2', '#8C4FFF', 380, 370, 580, 350)
    f1 = d.icon('ECS Fargate (N-04)<br>en 2 zonas', 'fargate', 'compute', 640, 440, lw=180)
    au = d.icon('Aurora PostgreSQL (N-05)<br>escritor', 'aurora', 'db', 640, 600, lw=220)
    alb = d.icon('Application Load Balancer<br>privado', 'elastic_load_balancing', 'net', 840, 440, lw=200)
    d.paso(5, 606, 430); d.paso(4, 606, 590)
    d.edge(ecr, f1, R(0.25), pts=((330, 494), (330, 468)))
    d.edge(ecr, au, R(0.75), pts=((310, 522), (310, 628)))
    d.edge(alb, f1, 'exitX=0;exitY=0.5;entryX=1;entryY=0.5;')
    return f1, au


# Preproduccion: 1-3 cadena, 4 migraciones, 5 azul-verde en Fargate y en el sitio emulado, 6 portales
d = D('Preproducción')
d.badge(B('Tipo de ambiente:') + ' solo nube (AWS) · el sitio on-premise se emula en una VPC', NUBE, 800)
git, ecr = cadena(d)
nube(d, 'Preproducción', 'sa-east-1 (São Paulo)', 320, 80, 1220, 700, 940)
portales(d, git, 6, 1350)
vpc_productiva(d, 'VPC Preproducción · 10.102.0.0/16 · topología de Producción', ecr)
d.group('Sitio emulado · VPC propia', 'group_vpc2', '#8C4FFF', 1000, 370, 285, 180)
emu = d.icon('ECS Fargate (N-04)<br>wms_only', 'fargate', 'compute', 1110, 420, lw=180)
d.paso(5, 1076, 410)
d.edge(ecr, emu, 'exitX=0;exitY=0.5;entryX=0;entryY=0.5;', pts=((14, 508), (14, 810), (980, 810), (980, 448)))
d.leyenda(COMUNES + [PASO_MIGRACIONES,
                     'Azul-verde con canario: la versión nueva se despliega junto a la vigente y recibe tráfico de forma gradual, y se demuestra aquí antes de cada paso a producción (RT-04.07); el balanceador drena la versión que se retira. En el sitio emulado se ensaya la promoción de la versión nueva con el sitio desconectado y su reconexión',
                     PASO_PORTALES], 850, 1180)
d.save('A3_Ambiente_Preproduccion.drawio')

# Produccion: 1-3 cadena, 4 migraciones, 5 azul-verde automatico, 6 portales, 7 sitios on-premise
d = D('Producción')
d.badge(B('Tipo de ambiente:') + ' mixto (nube + on-premise)', MIX, 520)
git, ecr = cadena(d)
nube(d, 'Producción', 'sa-east-1 (São Paulo) · región primaria', 320, 80, 1220, 700, 940)
portales(d, git, 6, 1350)
vpc_productiva(d, 'VPC Producción · 10.101.0.0/16', ecr)
# 11_j: los sitios descargan la imagen desde ECR por la VPN, a traves de la VPC Hub, y los endpoints de interfaz
# de la VPC de Produccion (ECR y S3); Ansible (F-02, CD Talca) actualiza los contenedores de los sitios.
epi = d.icon('VPC endpoints de interfaz<br>(ECR y S3)', 'endpoints', 'net', 840, 620, lw=200)
d.cells[-1] = d.cells[-1].replace('verticalLabelPosition=bottom;verticalAlign=top;', 'verticalLabelPosition=top;verticalAlign=bottom;')
d.paso(7, 804, 633)
d.group('VPC Hub', 'group_vpc2', '#8C4FFF', 1000, 370, 290, 170)
tgw = d.icon('AWS Transit Gateway', 'transit_gateway', 'net', 1040, 420, lw=120)
vpn = d.icon('AWS Site-to-Site VPN', 'site_to_site_vpn', 'net', 1190, 420, lw=120)
d.edge(tgw, vpn, R(0.5), dashed=1)
d.group('On-premise · parte de Producción', 'group_corporate_data_center', '#7D8998', 1590, 80, 420, 700)
ans = d.box(B('F-02 Ansible') + ' · CD Talca<br>actualiza los contenedores por la red de gestión', 1650, 170, 340, 70)
d.paso(7, 1616, 160)
sitios = [d.box(B('CD Talca') + '<br>VM-01: wms_only · VM-03: shipper', 1610, 413, 380, 70),
          d.box(B('CD Concepción') + '<br>VM-C01: wms_only · VM-C04: shipper', 1610, 543, 380, 70),
          d.box(B('Cross-docking (3)') + '<br>E-01: wms_only y shipper (Docker Compose)', 1610, 673, 380, 70)]
d.edge(ecr, epi, 'exitX=0;exitY=0.5;entryX=0.5;entryY=1;', dashed=1, pts=((14, 508), (14, 810), (868, 810)))
d.edge(epi, tgw, 'exitX=1;exitY=0.5;entryX=0;entryY=0.5;', dashed=1, pts=((980, 648), (980, 448)))
for sid, yc in zip(sitios, (448, 578, 708)):
    d.edge(vpn, sid, R(0.5), dashed=1)
    d.edge(ans, sid, 'exitX=1;exitY=0.5;entryX=1;entryY=0.5;', dashed=1, pts=((2000, 205), (2000, yc)))
d.leyenda(COMUNES + [PASO_MIGRACIONES,
                     'Azul-verde con canario: la versión nueva se despliega junto a la vigente y recibe tráfico de forma gradual; el paso a Producción es automático, sin intervención manual, dentro de las ventanas de despliegue (RT-04.06, RT-04.07); el balanceador drena la versión que se retira',
                     PASO_PORTALES,
                     'Los sitios descargan la imagen desde ECR por la VPN, a través de la VPC Hub, y los endpoints de interfaz de la VPC de Producción; Ansible (F-02) actualiza sus contenedores sitio por sitio'],
          850, 1300)
d.save('A4_Ambiente_Produccion.drawio')

# ------------------------------------------------------------------ Recuperacion ante Desastres
# 1-3 cadena, 4 la replica reducida recibe cada version, 5 Concepcion promueve VM-C01 si se pierde Talca
d = D('Recuperación ante Desastres')
d.badge(B('Tipo de ambiente:') + ' mixto (nube + on-premise) · un sitio de recuperación por dominio', MIX, 760)
git, ecr = cadena(d)
d.group('AWS Cloud · organización AWS Control Tower', 'group_aws_cloud_alt', '#232F3E', 320, 80, 560, 460)
d.group('Cuenta AWS · Recuperación ante Desastres', 'group_account', '#CD2264', 340, 120, 520, 400)
d.group('us-east-1 · ≈ 7.700 km de la primaria', 'group_region', '#00A4A6', 360, 165, 480, 335, dashed=1)
d.group('VPC Recuperación · 10.201.0.0/16', 'group_vpc2', '#8C4FFF', 380, 230, 440, 230)
far = d.icon('ECS Fargate (N-04)<br>réplica reducida', 'fargate', 'compute', 580, 320, lw=200)
d.paso(4, 546, 310)
d.edge(ecr, far, R(0.5))
d.group('On-premise · sitio de recuperación', 'group_corporate_data_center', '#7D8998', 930, 80, 440, 460)
t = d.box(B('CD Talca') + '<br>VM-01: wms_only', 950, 170, 400, 70)
c = d.box(B('CD Concepción') + '<br>VM-C01: wms_only', 950, 420, 400, 70)
d.paso(5, 916, 410)
d.edge(t, c, 'exitX=0.5;exitY=1;entryX=0.5;entryY=0;', dashed=1, label='DRP local')
d.leyenda(COMUNES + ['La réplica reducida de us-east-1 recibe cada versión liberada en Producción desde el mismo ECR de sa-east-1, de modo que la plataforma que se promueve en una conmutación corre la misma versión',
                     'Si la contingencia afecta solo a la bodega de Talca, el WMS de Concepción (VM-C01), que ya corre la misma imagen, asume su carga con un RTO adicional de 1 a 2 horas'],
          650, 1040)
d.save('A5_Ambiente_Recuperacion_Desastres.drawio')
print('ok')
