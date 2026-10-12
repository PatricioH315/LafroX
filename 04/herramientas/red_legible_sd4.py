"""Draw three independent network views at print size; preserve original XML/PDF."""
from pathlib import Path
from reportlab.pdfgen import canvas
from reportlab.lib.colors import HexColor, white
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont

ROOT = Path(__file__).resolve().parents[2]
OUT = ROOT/'04/figuras/fisica'
FONT = Path('C:/Windows/Fonts/arial.ttf')
pdfmetrics.registerFont(TTFont('RedSans', str(FONT)))
pdfmetrics.registerFont(TTFont('RedBold', 'C:/Windows/Fonts/arialbd.ttf'))
W, H = 620, 360
INK = '#253449'; BLUE = '#1674AD'; PURPLE = '#8250B5'; GREEN = '#398359'

def page(name, title):
    c = canvas.Canvas(str(OUT/name), pagesize=(W,H))
    c.setTitle(title)
    c.setAuthor('LafroX')
    c.setFillColor(HexColor(INK)); c.setFont('RedBold', 14)
    c.drawString(12, H-22, title)
    c.setStrokeColor(HexColor('#EF7228')); c.setLineWidth(2)
    c.line(12,H-31,W-12,H-31)
    return c

def text(c, x, y, lines, size=11, bold=False, center=False, color=INK):
    c.setFillColor(HexColor(color)); c.setFont('RedBold' if bold else 'RedSans',size)
    for i,line in enumerate(lines.split('\n')):
        fn = c.drawCentredString if center else c.drawString
        fn(x,y-i*(size+3),line)

def box(c,x,y,w,h,title,lines='',color=BLUE):
    c.setFillColor(HexColor('#F4F7FA')); c.setStrokeColor(HexColor(color)); c.setLineWidth(1)
    c.roundRect(x,y,w,h,5,stroke=1,fill=1)
    text(c,x+8,y+h-17,title,11.5,True,color=color)
    if lines: text(c,x+8,y+h-34,lines,10.5)

def wire(c,x1,y1,x2,y2,color=BLUE,dash=False,arrow=False):
    c.setStrokeColor(HexColor(color)); c.setFillColor(HexColor(color)); c.setLineWidth(1.3)
    c.setDash(4,3) if dash else c.setDash()
    c.line(x1,y1,x2,y2);c.setDash()
    if arrow:
        import math
        a=math.atan2(y2-y1,x2-x1); r=6
        p=c.beginPath();p.moveTo(x2,y2)
        p.lineTo(x2-r*math.cos(a-.45),y2-r*math.sin(a-.45))
        p.lineTo(x2-r*math.cos(a+.45),y2-r*math.sin(a+.45));p.close()
        c.drawPath(p,fill=1,stroke=0)

c=page('Red_01_general_legible.pdf','Red de los cinco sitios y las dos regiones')
box(c,12,88,170,220,'AWS primaria · sa-east-1','São Paulo\n\nVPC Hub\n10.100.0.0/16\nVPN y Transit Gateway\n\nVPC Producción\n10.101.0.0/16\nServicios privados · 2 AZ')
box(c,438,88,170,220,'AWS secundaria · us-east-1','Virginia del Norte\n\nVPN y Transit Gateway\npreparados para DR\n\nVPC Recuperación\n10.201.0.0/16\nNúcleo reducido\nPromoción y restitución',PURPLE)
sites=['CD Talca','CD Concepción','Curicó · cross-docking','Chillán · cross-docking','Los Ángeles · cross-docking']
for i,name in enumerate(sites):
    y=267-i*42
    box(c,217,y,186,33,name,color=INK)
    wire(c,182,y+16.5,217,y+16.5)
    wire(c,403,y+16.5,438,y+16.5,PURPLE,True)
wire(c,182,70,438,70,GREEN,arrow=True)
text(c,310,54,'Aurora Global Database y réplica S3',10.5,center=True,color=GREEN)
text(c,12,34,'Azul: producción. Violeta: rutas preparadas para recuperación.',10.5)
text(c,12,19,'Cada trazo WAN representa dos túneles IPsec / BGP por sitio y región.',10.5)
c.save()

c=page('Red_02_sitios_legible.pdf','Detalle de red y continuidad en los sitios')
cols=[(12,'CD Talca','Proxmox / Ceph: 3 nodos\nVM-01 a VM-06'),(221,'CD Concepción','2 servidores independientes\nVM-C01 a VM-C04'),(430,'Cada cross-docking','2 mini-PC industriales\nContenedores del sitio')]
for x,name,local in cols:
    text(c,x+93,305,name,12,True,True)
    box(c,x,233,178,55,'Cómputo local',local,INK)
    wire(c,x+89,233,x+89,211,INK)
    box(c,x,172,178,39,'Dos switches','Red local de operación',INK)
    wire(c,x+89,172,x+89,152,INK)
    box(c,x,113,178,39,'Par de firewalls HA','Seguridad y terminación VPN',PURPLE)
    wire(c,x+89,113,x+89,93,BLUE)
    wan='Fibra > LTE > satélite' if x<430 else 'Satélite > LTE dual'
    box(c,x,49,178,44,'Caminos WAN',wan,BLUE)
text(c,12,30,'VPN por sitio: dos túneles IPsec / BGP a cada región; datos locales durables.',10.5)
text(c,12,15,'Talca: N+1. Concepción y cross-docking: activo / espera con exclusión del escritor.',10.5)
c.save()

c=page('Red_03_regiones_legible.pdf','Detalle de conectividad regional y replicación')
box(c,12,87,272,224,'sa-east-1 · región primaria','VPC Hub: 10.100.0.0/16\nSite-to-Site VPN > Transit Gateway\n\nProducción: 10.101.0.0/16\nSubredes privadas en dos AZ\nALB privado > ECS Fargate\nKeycloak y Aurora PostgreSQL\n\nServicios regionales fuera de VPC:\nS3 privado y SQS FIFO',BLUE)
box(c,336,87,272,224,'us-east-1 · recuperación','Site-to-Site VPN > Transit Gateway\nConexiones preparadas por sitio\n\nRecuperación: 10.201.0.0/16\nALB privado > ECS Fargate reducido\nAurora secundaria y Keycloak\nPromoción y restitución por servicio\n\nServicios regionales fuera de VPC:\nS3 réplica y AWS Backup',PURPLE)
wire(c,284,208,336,208,GREEN,arrow=True)
text(c,310,194,'Aurora',10.5,center=True,color=GREEN)
wire(c,284,118,336,118,GREEN,arrow=True)
text(c,310,104,'S3',10.5,center=True,color=GREEN)
text(c,12,64,'SQS / SNS en DR: recursos preparados; el outbox se republica tras conmutar.',10.5)
text(c,12,46,'Las rutas regionales no habilitan acceso de Desarrollo, QA o Preproducción a sitios.',10.5)
text(c,12,28,'La réplica de datos y la restitución de canales son pasos distintos del procedimiento.',10.5)
c.save()
print('Generadas tres vistas independientes; fuente mínima: 10,5 puntos.')
