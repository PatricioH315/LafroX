# Genera los 5 diagramas de ambientes del apartado de despliegue (11_j_despliegue.tex).
# Regla: cada elemento y cada paso dibujado debe estar dicho en el apartado de despliegue;
# nombres y codigos como en el informe (02_a, 02_b, 06_e, 15_anexo_t11).
# Los pasos numerados siguen el orden que declara el texto:
#   1 GitLab CI orquesta y ejecuta los controles (RT-04.05)
#   2 AWS CodeBuild construye la imagen (SLSA nivel 3)
#   3 Amazon ECR guarda la imagen firmada, que se promueve por su digest
#   4 migraciones de esquema, antes de cambiar el trafico (solo donde hay Aurora dibujada)
#   n despliegue de la misma imagen en ECS Fargate (azul-verde con canario en Preproduccion y Produccion)
#   n+1 portales Angular en S3 privado + CloudFront (mismo ciclo)
#   n+2 sitios on-premise: descarga desde ECR y Ansible (F-02), sitio por sitio (solo Produccion)
import os
from xml.sax.saxutils import escape
OUT = os.path.dirname(os.path.abspath(__file__))

# Colores oficiales por categoria de AWS Architecture Icons
CAT = {'compute': '#ED7100', 'container': '#ED7100', 'devtools': '#C925D1', 'db': '#C925D1',
       'storage': '#7AA116', 'net': '#8C4FFF', 'sec': '#DD344C', 'mgmt': '#E7157B'}
PASO = '#D6246E'   # color de los circulos de paso


class D:
    def __init__(s, name):
        s.name, s.cells, s.n = name, [], 0

    def id(s):
        s.n += 1
        return 'n%d' % s.n

    def add(s, style, x, y, w, h, value=''):
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

    def group(s, label, gr, color, x, y, w, h, dashed=0):
        st = ('points=[];outlineConnect=0;gradientColor=none;html=1;whiteSpace=wrap;fontSize=17;fontStyle=1;'
              'container=0;pointerEvents=0;collapsible=0;recursiveResize=0;shape=mxgraph.aws4.group;grIcon=mxgraph.aws4.%s;'
              'strokeColor=%s;fillColor=none;verticalAlign=top;align=left;spacingLeft=30;fontColor=%s;dashed=%d;') % (gr, color, color, dashed)
        return s.add(st, x, y, w, h, label)

    def box(s, html, x, y, w, h, fill='#FFFFFF', stroke='#545B64', size=14, align='center'):
        st = ('rounded=1;arcSize=6;whiteSpace=wrap;html=1;fillColor=%s;strokeColor=%s;fontSize=%d;fontColor=#232F3E;'
              'align=%s;verticalAlign=middle;spacing=8;') % (fill, stroke, size, align)
        return s.add(st, x, y, w, h, html)

    def zone(s, label, x, y, w, h):
        st = ('rounded=0;whiteSpace=wrap;html=1;fillColor=none;strokeColor=#147EBA;dashed=1;fontColor=#147EBA;'
              'fontSize=15;fontStyle=1;verticalAlign=top;align=center;')
        return s.add(st, x, y, w, h, label)

    def badge(s, text, color, x, y, w=700):
        return s.add('rounded=1;arcSize=12;whiteSpace=wrap;html=1;fillColor=%s;strokeColor=%s;fontSize=18;fontColor=#FFFFFF;' % (color, color),
                     x, y, w, 40, text)

    def paso(s, n, x, y):
        """Circulo numerado del paso n, con su esquina superior izquierda en (x, y)."""
        return s.add('ellipse;whiteSpace=wrap;html=1;aspect=fixed;fillColor=%s;strokeColor=#FFFFFF;strokeWidth=2;'
                     'fontColor=#FFFFFF;fontStyle=1;fontSize=16;align=center;verticalAlign=middle;' % PASO, x, y, 30, 30, str(n))

    def leyenda(s, pasos, x, y, w=250):
        filas = ''.join('<tr><td style="vertical-align:top;padding:2px 6px 2px 0"><b style="color:%s">%d</b></td>'
                        '<td style="padding:2px 0">%s</td></tr>' % (PASO, i + 1, t) for i, t in enumerate(pasos))
        html = '<b>Secuencia de despliegue</b><table style="font-size:13px;margin-top:4px">%s</table>' % filas
        return s.add('rounded=1;arcSize=4;whiteSpace=wrap;html=1;fillColor=#F4F6F6;strokeColor=#545B64;fontSize=14;'
                     'fontColor=#232F3E;align=left;verticalAlign=top;spacing=10;', x, y, w, 44 + 30 * len(pasos), html)

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
R = 'exitX=1;exitY=%s;entryX=0;entryY=0.5;'
COMUNES = ['GitLab CI orquesta el cambio y ejecuta los controles; bloquea ante hallazgos críticos o altos (RT-04.05)',
           'AWS CodeBuild construye la imagen de forma hermética (SLSA nivel 3)',
           'Amazon ECR guarda la imagen firmada; se promueve por su digest, sin recompilar']


def cadena(d, y0=90):
    """Cadena de entrega del equipo de desarrollo (N-04, sa-east-1). Devuelve (codebuild, ecr)."""
    d.add('rounded=1;arcSize=6;whiteSpace=wrap;html=1;fillColor=#232F3E;strokeColor=#232F3E;fontSize=15;fontColor=#FFFFFF;',
          20, y0, 250, 56, B('Cadena de entrega') + '<br>N-04 · sa-east-1')
    dev = d.add('sketch=0;outlineConnect=0;fontColor=#232F3E;fillColor=#232F3E;strokeColor=none;dashed=0;'
                'labelPosition=right;verticalLabelPosition=middle;verticalAlign=middle;align=left;html=1;fontSize=15;aspect=fixed;'
                'shape=mxgraph.aws4.users;', 40, y0 + 80, 50, 50, 'Equipo de desarrollo')
    git = d.box(B('GitLab CI') + '<br>por suscripción', 20, y0 + 175, 170, 56, fill='#FFF2E8', stroke='#E67E22')
    cb = d.icon('AWS CodeBuild<br>(SLSA nivel 3)', 'codebuild', 'devtools', 40, y0 + 270, right=True)
    ecr = d.icon('Amazon ECR<br>(imagen firmada)', 'ecr', 'container', 40, y0 + 390, lw=180)
    d.edge(dev, git); d.edge(git, cb); d.edge(cb, ecr)
    d.paso(1, 175, y0 + 160); d.paso(2, 8, y0 + 262); d.paso(3, 8, y0 + 382)
    return cb, ecr


def cuenta(d, nombre, region, vpc, x, y, w, h):
    d.group('AWS Cloud · organización AWS Control Tower', 'group_aws_cloud_alt', '#232F3E', x, y, w, h)
    d.group('Cuenta AWS · %s' % nombre, 'group_account', '#CD2264', x + 20, y + 40, w - 40, h - 60)
    d.group(region, 'group_region', '#00A4A6', x + 40, y + 85, w - 80, h - 125, dashed=1)
    return d.group(vpc, 'group_vpc2', '#8C4FFF', x + 60, y + 130, w - 120, h - 190)


def portales(d, cb, x, y, n):
    s3 = d.icon('Amazon S3 privado<br>(portales N-01 a N-03)', 's3', 'storage', x, y)
    d.icon('Amazon CloudFront', 'cloudfront', 'net', x + 170, y)
    d.paso(n, x - 34, y - 10)
    return s3


# ---------------------------------------------------------------- A1 Desarrollo
d = D('Desarrollo')
d.badge(B('Tipo de ambiente:') + ' solo nube (AWS)', NUBE, 20, 20)
cb, ecr = cadena(d)
cuenta(d, 'Desarrollo', 'sa-east-1 (São Paulo)', 'VPC Desarrollo · 10.104.0.0/16', 340, 80, 1000, 560)
far = d.icon('ECS Fargate (N-04)<br>imagen Laravel 13 · PHP 8.5', 'fargate', 'compute', 460, 300, lw=240)
d.paso(4, 426, 290)
d.box(B('Pruebas unitarias'), 660, 280, 260, 50)
d.box('Datos sintéticos o anonimizados', 660, 350, 260, 50, fill='#F5E6FA', stroke='#C925D1')
d.box('Aislado y reconstruible desde código<br>Se reduce o apaga fuera del horario de uso', 660, 420, 260, 80, fill='#F4F6F6')
d.icon('AWS Secrets Manager<br>(secretos del ambiente)', 'secrets_manager', 'sec', 1000, 280, lw=150)
d.icon('SSM Parameter Store<br>(configuración del ambiente)', 'systems_manager', 'mgmt', 1170, 280, lw=150)
portales(d, cb, 1000, 420, 5)
d.edge(ecr, far, 'despliega la misma imagen', ports=R % 0.5, pos=0.6)
d.leyenda(COMUNES + ['Despliegue de la imagen en ECS Fargate, con la configuración (Parameter Store) y los secretos (Secrets Manager) del ambiente',
                     'Publicación de los portales Angular en S3 privado y CloudFront'], 20, 660, 520)
d.save('A1_Ambiente_Desarrollo.drawio')

# ---------------------------------------------------------------- A2 QA
d = D('QA')
d.badge(B('Tipo de ambiente:') + ' solo nube (AWS)', NUBE, 20, 20)
cb, ecr = cadena(d)
cuenta(d, 'QA', 'sa-east-1 (São Paulo)', 'VPC QA · 10.103.0.0/16', 340, 80, 1000, 620)
far = d.icon('ECS Fargate (N-04)<br>misma imagen; ensayo del perfil wms_only', 'fargate', 'compute', 460, 300, lw=260)
d.paso(4, 426, 290)
d.box(B('Pruebas funcionales, de integración y de regresión automatizadas') + '<br>Análisis dinámico', 680, 270, 290, 80)
d.box('Verificador local de identidad y puerta de API local del WMS', 680, 365, 290, 60, fill='#FCE4EC', stroke='#DD344C')
d.box('Adaptadores simulados del ERP', 680, 440, 290, 45, fill='#FCE4EC', stroke='#DD344C')
d.box('Ensayo de corte de enlace y relevo de turno', 680, 500, 290, 45)
d.box('Datos de prueba versionados<br>Aislado y reconstruible desde código · se reduce o apaga fuera de horario', 420, 565, 550, 55, fill='#F5E6FA', stroke='#C925D1')
d.icon('AWS Secrets Manager<br>(secretos del ambiente)', 'secrets_manager', 'sec', 1030, 280, lw=150)
d.icon('SSM Parameter Store<br>(configuración del ambiente)', 'systems_manager', 'mgmt', 1200, 280, lw=150)
portales(d, cb, 1030, 440, 5)
d.edge(ecr, far, 'despliega la misma imagen', ports=R % 0.5, pos=0.6)
d.leyenda(COMUNES + ['Despliegue de la imagen en ECS Fargate, con la configuración (Parameter Store) y los secretos (Secrets Manager) del ambiente',
                     'Publicación de los portales Angular en S3 privado y CloudFront'], 20, 720, 520)
d.save('A2_Ambiente_QA.drawio')


def nube_productiva(d, x0, lector, extra_aurora):
    """Topologia de nube comun a Preproduccion y Produccion (Preproduccion replica la de Produccion, RT-04.02)."""
    alb = d.icon('Application Load Balancer privado', 'elastic_load_balancing', 'net', x0 + 60, 245, right=True, lw=260)
    d.zone('Zona sa-east-1a', x0 + 50, 340, 330, 250); d.zone('Zona sa-east-1b', x0 + 410, 340, 330, 250)
    f1 = d.icon('ECS Fargate (N-04)<br>perfil API', 'fargate', 'compute', x0 + 180, 380)
    d.icon('ECS Fargate (N-04)<br>perfil API', 'fargate', 'compute', x0 + 540, 380)
    au = d.icon('Aurora PostgreSQL (N-05)<br>escritor' + extra_aurora, 'aurora', 'db', x0 + 180, 490)
    d.icon('Aurora PostgreSQL (N-05)<br>' + lector, 'aurora', 'db', x0 + 540, 490)
    fb = d.box('ECS Fargate (N-04): consolas Angular · consumidor de reconciliación · trabajos · planificador · motor de rutas M4 · AS2 M11',
               x0 + 50, 620, 690, 56, fill='#FFF2E8', stroke='#ED7100')
    return alb, f1, au, fb


# ---------------------------------------------------------------- A3 Preproduccion
d = D('Preproducción')
d.badge(B('Tipo de ambiente:') + ' solo nube (AWS) · el sitio on-premise se emula en una VPC', NUBE, 20, 20, 900)
cb, ecr = cadena(d)
cuenta(d, 'Preproducción', 'sa-east-1 (São Paulo)', 'VPC Preproducción · 10.102.0.0/16 · misma topología de nube que Producción', 340, 80, 1500, 720)
alb, f1, au, fb = nube_productiva(d, 380, 'lector', '')
d.paso(4, 520, 480); d.paso(5, 520, 370)
d.icon('AWS Secrets Manager<br>(secretos del ambiente)', 'secrets_manager', 'sec', 1180, 250, lw=150)
d.icon('SSM Parameter Store<br>(configuración del ambiente)', 'systems_manager', 'mgmt', 1350, 250, lw=150)
portales(d, cb, 1180, 380, 6)
d.icon('Amazon Macie<br>(verifica datos sintéticos)', 'macie', 'sec', 1180, 620)
d.group('Sitio on-premise emulado · VPC propia', 'group_vpc2', '#8C4FFF', 1450, 230, 320, 250)
emu = d.box('Misma imagen: ' + B('wms_only') + ' · broker · verificador local', 1465, 290, 290, 60)
d.paso(5, 1432, 282)
d.box(B('Sin túnel hacia las bodegas'), 1465, 370, 290, 50, fill='#FCE4EC', stroke='#DD344C')
d.box(B('Aceptación, carga, resiliencia y ensayo del paso a producción') +
      '<br>Se reduce o apaga fuera de horario; dimensionamiento completo en las pruebas de carga', 1450, 510, 320, 130, fill='#F4F6F6')
d.edge(ecr, au, 'migraciones de esquema', ports=R % 0.75, pos=0.25)
d.edge(ecr, f1, 'azul-verde con canario', ports=R % 0.25, pos=0.25)
d.leyenda(COMUNES + ['Migraciones Laravel aditivas y reversibles, antes de cambiar el tráfico (RT-04.10)',
                     'Despliegue azul-verde con canario en ECS Fargate y en el sitio emulado (RT-04.07)',
                     'Publicación de los portales Angular en S3 privado y CloudFront'], 20, 840, 620)
d.save('A3_Ambiente_Preproduccion.drawio')

# ---------------------------------------------------------------- A4 Produccion
d = D('Producción')
d.badge(B('Tipo de ambiente:') + ' mixto (nube + on-premise)', MIX, 20, 20)
cb, ecr = cadena(d)
cuenta(d, 'Producción', 'sa-east-1 (São Paulo) · región primaria', 'VPC Producción · 10.101.0.0/16', 340, 80, 1150, 720)
alb, f1, au, fb = nube_productiva(d, 380, 'lector promovible', '')
d.paso(4, 520, 480); d.paso(5, 520, 370)
d.icon('AWS Secrets Manager<br>(secretos del ambiente)', 'secrets_manager', 'sec', 1180, 250, lw=150)
d.icon('SSM Parameter Store<br>(configuración del ambiente)', 'systems_manager', 'mgmt', 1350, 250, lw=150)
portales(d, cb, 1180, 380, 6)
d.icon('AWS Systems Manager<br>Session Manager (acceso excepcional)', 'systems_manager', 'mgmt', 1180, 620, lw=230)
d.group('On-premise · parte de Producción', 'group_corporate_data_center', '#7D8998', 1540, 80, 470, 720)
d.box(B('CD Talca · Proxmox VE, 3 nodos') + '<br>VM-01: A-01 Motor WMS (wms_only)<br>VM-03: A-03 Broker (RabbitMQ) y shipper', 1560, 140, 430, 100, fill='#F4F6F6')
d.box(B('CD Concepción · Proxmox VE') + '<br>VM-C01: A-01 Motor WMS (wms_only)<br>VM-C04: A-03 Broker (RabbitMQ) y shipper', 1560, 270, 430, 100, fill='#F4F6F6')
d.box(B('Cross-docking (3) · E-01 WMS de cross-docking') + '<br>Docker Compose: wms_only, shipper, PostgreSQL, RabbitMQ y caché de identidad', 1560, 400, 430, 100, fill='#F4F6F6')
sit = d.box('Primera instalación de cada versión: sitio por sitio', 1560, 540, 430, 50)
d.paso(7, 1526, 530)
d.box('Contenedores de la misma imagen; infraestructura de cada sitio declarada como código versionado', 1560, 610, 430, 70, fill='#F4F6F6')
d.edge(ecr, au, 'migraciones de esquema', ports=R % 0.75, pos=0.25)
d.edge(ecr, f1, 'azul-verde con canario', ports=R % 0.25, pos=0.25)
d.edge(ecr, sit, 'misma imagen desde ECR por la VPN (VPC Hub) y los endpoints de interfaz de la VPC de Producción; Ansible (F-02) actualiza los contenedores',
       dashed=1, ports='exitX=0;exitY=0.5;entryX=0;entryY=0.5;', pos=0.3, pts=((14, 508), (14, 830), (1520, 830), (1520, 565)))
d.leyenda(COMUNES + ['Migraciones Laravel aditivas y reversibles, antes de cambiar el tráfico (RT-04.10)',
                     'Despliegue azul-verde con canario en ECS Fargate; paso automático sin intervención manual (RT-04.06, RT-04.07)',
                     'Publicación de los portales Angular en S3 privado y CloudFront',
                     'Sitios on-premise: descarga desde ECR por la VPN (VPC Hub) y los endpoints de interfaz; Ansible (F-02) actualiza los contenedores, sitio por sitio'],
          20, 860, 720)
d.save('A4_Ambiente_Produccion.drawio')

# ---------------------------------------------------------------- A5 Recuperacion
d = D('Recuperación ante Desastres')
d.badge(B('Tipo de ambiente:') + ' mixto (nube + on-premise) · un sitio de recuperación por dominio', MIX, 20, 20, 820)
cb, ecr = cadena(d)
cuenta(d, 'Recuperación ante Desastres', 'us-east-1 · ≈ 7.700 km de la primaria', 'VPC Recuperación · 10.201.0.0/16', 340, 80, 1000, 560)
rfar = d.icon('ECS Fargate (N-04)<br>réplica reducida<br>carga completa en &lt; 30 min', 'fargate', 'compute', 460, 300, lw=220, right=True)
d.paso(4, 426, 290)
d.icon('Aurora Global Database (N-05)<br>réplica promovible', 'aurora', 'db', 800, 260, lw=240)
d.icon('AWS Backup (N-11)<br>copias entre regiones', 'backup', 'storage', 1100, 260)
d.box('Keycloak (A-05), API pública y privada y Verified Access: se restituyen en la conmutación (paso 6, Tabla 4.3-6)', 460, 460, 780, 60, fill='#F4F6F6')
d.edge(ecr, rfar, 'cada versión liberada en Producción', ports=R % 0.5, pos=0.6)
d.group('On-premise · sitio de recuperación del dominio on-premise', 'group_corporate_data_center', '#7D8998', 1380, 80, 470, 560)
t = d.box(B('CD Talca') + '<br>VM-01: A-01 Motor WMS · VM-02: A-02 Base transaccional', 1410, 150, 410, 80, fill='#F4F6F6')
c = d.box(B('CD Concepción') + ' (opera a diario en Producción)<br>VM-C01 promueve su A-01 Motor WMS<br>RTO adicional de 1 a 2 h', 1410, 320, 410, 90, fill='#F4F6F6')
d.edge(t, c, 'DRP local · ≈ 200 km', dashed=1)
d.leyenda(COMUNES + ['La réplica reducida de ECS Fargate recibe cada versión liberada en Producción, desde el mismo ECR de sa-east-1'],
          20, 660, 620)
d.save('A5_Ambiente_Recuperacion_Desastres.drawio')
print('ok')
