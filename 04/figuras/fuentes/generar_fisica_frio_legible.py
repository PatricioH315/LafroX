"""Vista física propia y legible. Conserva sin cambios el diagrama original."""
from pathlib import Path
import xml.etree.ElementTree as ET

root = ET.Element('mxfile', host='app.diagrams.net')
diagram = ET.SubElement(root, 'diagram', id='fisica-frio', name='Física vigente')
model = ET.SubElement(diagram,'mxGraphModel',page='0')
cells = ET.SubElement(model,'root')
ET.SubElement(cells,'mxCell',id='0')
ET.SubElement(cells,'mxCell',id='1',parent='0')

def box(id_,text,x,y,w,h,fill='#FFFFFF'):
    c=ET.SubElement(cells,'mxCell',id=id_,parent='1',vertex='1',value=text,
        style=f'rounded=1;whiteSpace=wrap;html=1;fontSize=20;fontFamily=Helvetica;'
              f'fillColor={fill};strokeColor=#555555;fontColor=#111111;spacing=6;')
    ET.SubElement(c,'mxGeometry',x=str(x),y=str(y),width=str(w),height=str(h),**{'as':'geometry'})

def edge(a,b,ex='.5',ey='1',ix='.5',iy='0'):
    c=ET.SubElement(cells,'mxCell',id=a+'-'+b,parent='1',edge='1',source=a,target=b,
        style=f'edgeStyle=orthogonalEdgeStyle;endArrow=block;strokeColor=#555555;'
              f'exitX={ex};exitY={ey};entryX={ix};entryY={iy};')
    ET.SubElement(c,'mxGeometry',relative='1',**{'as':'geometry'})

box('truck','28 camiones de frío; reserva por familia<br>B-04 Greengrass + B-05/B-06: tres PT100<br>B-03/B-08 y C-02: contraste independiente<br>B-09 Iridium; B-10 a B-15: soporte<br>Alarma local; móvil y SBD en paralelo',0,0,440,150,'#FDE8DA')
box('users','Accesos de personas y empresas<br>C-01 Preventa · C-02 Reparto · C-03 Bodega<br>Portales/apps → CloudFront, WAF y Shield<br>Consolas → Verified Access<br>Cadenas → borde AS2 → ALB/OpenAS2',470,0,440,150)
box('primary','AWS sa-east-1 · Producción multi-AZ<br>N-03 API → N-04 ECS Fargate / Keycloak<br>N-05 Aurora; N-07 ElastiCache<br>N-08 IoT Core + CloudConnect/SQS<br>N-06 DynamoDB/S3; N-10 Glue/Redshift<br>N-09 mensajería; N-11 respaldo; N-12/N-13 gestión',0,190,580,190,'#EDF6FA')
box('dr','AWS us-east-1 · DR<br>Aurora, temperatura y S3<br>Aplicación reducida<br>Copias protegidas<br>RTO ≤4 h; RPO ≤15 min<br>GPS no se replica',620,190,290,190,'#EDF6FA')
box('talca','CD Talca<br>3 nodos Proxmox/Ceph<br>VM-01 a VM-06; ERP 2017<br>NAS WORM; firewall HA<br>B-01/B-02; UPS y generador<br>Fibra + LTE + Starlink',0,430,285,180)
box('conce','CD Concepción<br>2 servidores activo/en espera<br>VM-C01 a VM-C04 y copias<br>WMS propio; firewall HA<br>B-01/B-02; UPS<br>Fibra + LTE + Starlink',312,430,285,180)
box('cross','Cross-docking ×3<br>Curicó, Chillán, Los Ángeles<br>2 mini-PC E-01 por sitio<br>WMS propio; firewall HA; UPS<br>Starlink + LTE Entel/Claro<br>WMS autónomo',625,430,285,180)
box('rule','Cada sitio conserva su autoridad sobre el stock y opera sin WAN.<br>El kit no necesita Internet para proteger el frío. M9 persiste antes de A2 y concilia móvil/SBD.',0,638,910,64,'#F4F4F4')
edge('truck','primary',ix='.25')
edge('users','primary',ix='.75')
edge('primary','dr',ex='1',ey='.5',ix='0',iy='.5')
for site,port in [('talca','.15'),('conce','.5'),('cross','.85')]:edge(site,'primary',ex='.5',ey='0',ix=port,iy='1')
target=Path(__file__).with_name('Arquitectura_Fisica_General_frio_legible.drawio')
ET.ElementTree(root).write(target,encoding='utf-8',xml_declaration=True)
print(target)
