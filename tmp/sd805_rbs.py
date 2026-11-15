"""Render the editable RBS geometry as a vector PDF; keep the existing layout."""
from pathlib import Path
import xml.etree.ElementTree as ET
import re
from reportlab.pdfgen.canvas import Canvas
from reportlab.lib.styles import ParagraphStyle
from reportlab.platypus import Paragraph
from reportlab.lib.colors import HexColor

root=Path(__file__).resolve().parents[1]
source=root/'08_plan_riesgos/figuras/LafroX_RBS_36_riesgos_S8_v4.drawio'
target=source.with_suffix('.pdf')
cells={c.get('id'): c for c in ET.parse(source).iter('mxCell')}
def geo(c):
    g=c.find('mxGeometry')
    return [float(g.get(k,'0')) for k in ['x','y','width','height']]
c=Canvas(str(target), pagesize=(594.96,841.92))
c.setTitle('RBS LafroX: 36 riesgos por fuente predominante')
c.setAuthor('LafroX')
scale=594.96/3820
c.scale(scale,scale)
height=841.92/scale
c.setStrokeColor(HexColor('#666666')); c.setLineWidth(3)
# Root and branch bus.
rx,ry,rw,rh=geo(cells['root'])
bus=275
c.line(rx+rw/2,height-(ry+rh),rx+rw/2,height-bus)
branches=[cells[f'b{i}'] for i in range(1,7)]
centers=[geo(b)[0]+geo(b)[2]/2 for b in branches]
c.line(min(centers),height-bus,max(centers),height-bus)
for b in branches:
    x,y,w,h=geo(b); c.line(x+w/2,height-bus,x+w/2,height-y)
# Route risk edges down each existing subcolumn, outside the text boxes.
for edge in cells.values():
    if edge.get('edge')!='1' or not edge.get('target','').startswith('n'): continue
    child=cells[edge.get('target')]; parent=cells[edge.get('source')]
    x,y,w,h=geo(child); px,py,pw,ph=geo(parent)
    spine=x-28
    c.line(spine,height-(py+ph),spine,height-(y+h/2))
    c.line(spine,height-(y+h/2),x,height-(y+h/2))
for cell in cells.values():
    if cell.get('vertex')!='1': continue
    x,y,w,h=geo(cell)
    c.setFillColor(HexColor('#f5f5f5')); c.setStrokeColor(HexColor('#666666'))
    c.roundRect(x,height-y-h,w,h,16,stroke=1,fill=1)
    size=58 if cell.get('id')=='root' else 50 if cell.get('id','').startswith('b') else 45
    value=re.sub(r'<font style="font-size:(\d+)px">',r'<font size="\1">',cell.get('value','')).replace('<br>','<br/>')
    style=ParagraphStyle('rbs',fontName='Helvetica',fontSize=size,leading=size*1.20,
                         textColor=HexColor('#000000'),alignment=1 if cell.get('id')=='root' else 0)
    p=Paragraph(value,style)
    aw,ah=p.wrap(w-50,h-20)
    assert ah<=h-10,(cell.get('id'),ah,h)
    p.drawOn(c,x+25,height-y-(h-ah)/2-ah)
c.showPage();c.save()
print(target)
