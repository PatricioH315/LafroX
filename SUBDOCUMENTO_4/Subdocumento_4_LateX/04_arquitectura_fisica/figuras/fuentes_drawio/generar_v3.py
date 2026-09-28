"""Recompone las dos vistas v3 a partir de los iconos de la página NUBE del usuario."""
from __future__ import annotations

import heapq
import html
import math
import re
from pathlib import Path
from xml.etree import ElementTree as ET

HERE = Path(__file__).resolve().parent
ORIGINAL = ET.parse(HERE / "usuario_nube_original.drawio").getroot()
PAGE = next(d for d in ORIGINAL.findall("diagram") if d.get("name") == "NUBE")
ORIGINAL_CELLS = {c.get("id", "").split("-")[-1]: c for c in PAGE.findall("./mxGraphModel/root/mxCell")}
AWS = {
    "route": "7", "waf": "75", "cloudfront": "78", "api": "86", "ecr": "82",
    "cloudwatch": "106", "alb": "25", "fargate": "58", "aurora": "97",
    "redis": "69", "dynamodb": "91", "s3": "94", "iot": "31", "lambda": "63",
    "sqs": "51", "glue": "14", "redshift": "21", "quicksight": "28",
    "tgw": "42", "vpn": "45", "dms": "54",
}
IMAGES = {"pc": "4", "phone": "5", "tablet": "114", "keycloak": "117"}
AWS_EXTRA = {
    "sns": ("sns", "#E7157B"), "transfer": ("transfer_family", "#E7157B"),
    "kms": ("key_management_service", "#DD344C"),
    "secrets": ("secrets_manager", "#DD344C"),
    "guardduty": ("guardduty", "#DD344C"),
    "backup": ("backup", "#7AA116"),
    "shield": ("shield_advanced", "#DD344C"),
    "sensor": ("sensor", "#7AA116"),
    "greengrass": ("greengrass", "#7AA116"),
}
CLIP = {
    "fibra": "networking/Modem_128x128.png", "lte": "networking/Wireless_Router_N_128x128.png",
    "firewall": "networking/Firewall_02_128x128.png", "switch": "networking/Switch_128x128.png",
    "vm": "computers/Virtual_Machine_128x128.png", "db": "computers/Database_128x128.png",
    "rabbit": "computers/Virtual_Application_128x128.png", "wifi": "networking/Wireless_Router_128x128.png",
    "terminal": "computers/IBM_Tablet_128x128.png", "starlink": "telecommunication/Signal_tower_on_128x128.png",
}


def clean_style(raw: str) -> dict[str, str]:
    return dict(p.split("=", 1) for p in raw.split(";") if "=" in p)


def style_str(data: dict[str, str]) -> str:
    return ";".join(f"{k}={v}" for k, v in data.items()) + ";"


def text_lines(value: str) -> list[str]:
    return html.unescape(re.sub(r"<[^>]*>", "", value.replace("<br>", "\n"))).split("\n")


class Diagram:
    def __init__(self, name: str, w: int, h: int, font: int = 28):
        self.name, self.w, self.h, self.font = name, w, h, font
        self.root = ET.Element("mxfile", host="app.diagrams.net", agent="LafroX", version="v3")
        d = ET.SubElement(self.root, "diagram", id=name, name=name)
        m = ET.SubElement(d, "mxGraphModel", dx="1700", dy="1200", grid="1", gridSize="10", guides="1",
                          tooltips="1", connect="1", arrows="1", fold="1", page="1", pageScale="1",
                          pageWidth=str(w), pageHeight=str(h), math="0", shadow="0")
        self.base = ET.SubElement(m, "root")
        ET.SubElement(self.base, "mxCell", id="0")
        ET.SubElement(self.base, "mxCell", id="1", parent="0")
        self.nodes: dict[str, tuple[int, int, int, int]] = {}
        self.groups: dict[str, tuple[int, int, int, int]] = {}
        self.labels: dict[str, tuple[float, float, float, float]] = {}
        self.parents: dict[str, str] = {}
        self.routed: list[list[tuple[int, int]]] = []
        self.edges: list[tuple[str, str, str, bool, str]] = []
        self.annotations: dict[str, tuple[float,float,float,float]] = {}

    def group(self, key: str, title: str, x: int, y: int, w: int, h: int, parent="1", color="#94a3b8", dashed=False):
        px, py = self.groups[parent][:2] if parent in self.groups else (0, 0)
        style = dict(shape="rectangle", whiteSpace="wrap", html="1", container="1", collapsible="0",
                     fillColor="none", strokeColor=color, strokeWidth="2", fontColor="#334155",
                     fontSize=str(self.font), fontStyle="1", align="left", verticalAlign="top",
                     spacingLeft="12", spacingTop="9", rounded="0")
        if dashed: style["dashed"] = "1"
        c = ET.SubElement(self.base, "mxCell", id=key, value=title, style=style_str(style), vertex="1", parent=parent)
        ET.SubElement(c, "mxGeometry", x=str(x-px), y=str(y-py), width=str(w), height=str(h), **{"as": "geometry"})
        self.groups[key] = (x, y, x+w, y+h)
        self.parents[key] = parent
        tw = len(title) * self.font * .68 + 8
        self.labels[key] = (x+12, y+9, x+12+tw, y+9+self.font*1.2+8)

    def icon(self, key: str, kind: str, title: str, x: int, y: int, parent="1", size=60, label_width=140):
        px, py = self.groups[parent][:2] if parent in self.groups else (0, 0)
        if kind in IMAGES:
            s = clean_style(ORIGINAL_CELLS[IMAGES[kind]].get("style", ""))
            s.pop("rotation", None)
        elif kind in AWS:
            s = clean_style(ORIGINAL_CELLS[AWS[kind]].get("style", ""))
        elif kind in AWS_EXTRA:
            resource, color = AWS_EXTRA[kind]
            s = clean_style(ORIGINAL_CELLS["7"].get("style", ""))
            s["resIcon"] = "mxgraph.aws4." + resource
            s["fillColor"] = color
        elif kind in CLIP:
            s = {"shape": "image", "image": "img/lib/clip_art/" + CLIP[kind], "imageAspect": "1", "aspect": "fixed"}
        else:
            raise ValueError(kind)
        s.update({"verticalLabelPosition": "bottom", "verticalAlign": "top", "align": "center",
                  "whiteSpace": "wrap", "html": "1", "fontSize": str(self.font), "fontStyle": "1",
                  "fontColor": "#172334", "spacing": "0", "strokeWidth": "2"})
        c = ET.SubElement(self.base, "mxCell", id=key, value="",
                          style=style_str(s), vertex="1", parent=parent, **{"data-label":key+"_label"})
        ET.SubElement(c, "mxGeometry", x=str(x-px), y=str(y-py), width=str(size), height=str(size), **{"as": "geometry"})
        self.nodes[key] = (x, y, x+size, y+size)
        self.parents[key] = parent
        lines = title.split("\n")
        tw = max(len(t)*self.font*.70 for t in lines)+20
        th = len(lines)*self.font*1.18+12
        lx,ly = x+size/2-tw/2, y+size+5
        self.labels[key] = (lx,ly,lx+tw,ly+th)
        label_style={"shape":"text","whiteSpace":"wrap","html":"1","fillColor":"none",
                     "strokeColor":"none","align":"center","verticalAlign":"top",
                     "fontSize":str(self.font),"fontStyle":"1","fontColor":"#172334",
                     "spacing":"0","overflow":"hidden"}
        label=ET.SubElement(self.base,"mxCell",id=key+"_label",value=title.replace("\n","<br>"),
                            style=style_str(label_style),vertex="1",parent=parent,**{"data-icon":key})
        ET.SubElement(label,"mxGeometry",x=str(lx-px),y=str(ly-py),width=str(tw),height=str(th),**{"as":"geometry"})

    def connect(self, source: str, target: str, title="", dashed=False, color="#475569"):
        self.edges.append((source, target, title, dashed, color))

    def annotation(self,key:str,title:str,x:int,y:int,w:int,h:int,parent="1"):
        px,py=self.groups[parent][:2] if parent in self.groups else (0,0)
        style={"shape":"text","whiteSpace":"wrap","html":"1","fillColor":"#ffffff",
               "strokeColor":"none","align":"center","verticalAlign":"middle","fontSize":str(self.font),
               "fontStyle":"1","fontColor":"#334155","spacing":"0"}
        c=ET.SubElement(self.base,"mxCell",id=key,value=title,style=style_str(style),vertex="1",parent=parent,
                        **{"data-annotation":"1"})
        ET.SubElement(c,"mxGeometry",x=str(x-px),y=str(y-py),width=str(w),height=str(h),**{"as":"geometry"})
        self.annotations[key]=(x,y,x+w,y+h)

    def _ancestors(self, key: str) -> set[str]:
        result = set()
        while key in self.parents:
            key = self.parents[key]
            result.add(key)
        return result

    def _route(self, source: str, target: str, include_endpoint_labels: bool = True) -> list[tuple[int, int]]:
        a, b = self.nodes[source], self.nodes[target]
        ac = ((a[0]+a[2])/2, (a[1]+a[3])/2)
        bc = ((b[0]+b[2])/2, (b[1]+b[3])/2)
        options = [("right", (a[2], ac[1]), (b[0], bc[1])),
                   ("left", (a[0], ac[1]), (b[2], bc[1])),
                   ("down", (ac[0], a[3]), (bc[0], b[1])),
                   ("up", (ac[0], a[1]), (bc[0], b[3]))]
        sources = {"right":(a[2],ac[1]),"left":(a[0],ac[1]),"down":(ac[0],a[3]),"up":(ac[0],a[1])}
        entries = {"left":(b[0],bc[1]),"right":(b[2],bc[1]),"up":(bc[0],b[1]),"down":(bc[0],b[3])}
        paired = {("right","left"),("left","right"),("down","up"),("up","down")}
        options += [(side,anchor,entry) for side,anchor in sources.items()
                    for entry_side,entry in entries.items() if (side,entry_side) not in paired]
        allowed = self._ancestors(source) | self._ancestors(target)
        blocked = []
        for k, r in self.nodes.items():
            if k not in (source, target):
                blocked.append((r[0]-8, r[1]-8, r[2]+8, r[3]+8))
            if include_endpoint_labels or k not in (source,target):
                l = self.labels[k]
                blocked.append((l[0]-5, l[1]-5, l[2]+5, l[3]+5))
        for k, r in self.groups.items():
            if k not in allowed:
                blocked.append((r[0]-8, r[1]-8, r[2]+8, r[3]+8))
            else:
                l = self.labels[k]
                blocked.append((l[0]-8, l[1]-8, l[2]+8, l[3]+8))
        blocked.extend((r[0]-5,r[1]-5,r[2]+5,r[3]+5) for r in self.annotations.values())
        best = None
        for option_index,(side, startf, endf) in enumerate(options):
            if option_index >= 4 and best is not None:
                break
            sx, sy, tx, ty = (int(round(v/10))*10 for v in (*startf, *endf))
            # This grid is aligned with all icon vertices; a 10-px outward lead keeps bends outside icons.
            step = {"right": (10,0), "left": (-10,0), "down": (0,10), "up": (0,-10)}[side]
            start = (sx+step[0], sy+step[1])
            end = (tx, ty)
            lowx, highx = max(0, min(sx,tx)-420), min(self.w, max(sx,tx)+420)
            lowy, highy = max(0, min(sy,ty)-420), min(self.h, max(sy,ty)+420)
            def legal(p):
                x,y=p
                if not (lowx <= x <= highx and lowy <= y <= highy): return False
                return all(not (r[0] < x < r[2] and r[1] < y < r[3]) for r in blocked)
            if not legal(start): continue
            heap=[(abs(start[0]-tx)+abs(start[1]-ty),0,start,None)]
            seen={(start,None):0}; prev={}
            found=None
            while heap:
                _,cost,p,direction=heapq.heappop(heap)
                state=(p,direction)
                if cost>seen.get(state,1e9):continue
                if p==end:
                    found=state;break
                for dx,dy in ((10,0),(-10,0),(0,10),(0,-10)):
                    q=(p[0]+dx,p[1]+dy)
                    if not legal(q) and q!=end:continue
                    turn=0 if direction is None or direction==(dx,dy) else 8
                    proximity=0
                    for old in self.routed:
                        for u,v in zip(old,old[1:]):
                            if u[0]==v[0] and dx==0 and min(u[1],v[1])<q[1]<max(u[1],v[1]) and abs(q[0]-u[0])<20: proximity+=120
                            if u[1]==v[1] and dy==0 and min(u[0],v[0])<q[0]<max(u[0],v[0]) and abs(q[1]-u[1])<20: proximity+=120
                    for g in self.groups.values():
                        if dx==0 and g[1]<q[1]<g[3] and (abs(q[0]-g[0])<18 or abs(q[0]-g[2])<18):proximity+=90
                        if dy==0 and g[0]<q[0]<g[2] and (abs(q[1]-g[1])<18 or abs(q[1]-g[3])<18):proximity+=90
                    nc=cost+10+turn+proximity
                    ns=(q,(dx,dy))
                    if nc<seen.get(ns,1e9):
                        seen[ns]=nc;prev[ns]=state
                        heapq.heappush(heap,(nc+abs(q[0]-tx)+abs(q[1]-ty),nc,q,(dx,dy)))
            if found:
                pts=[]
                while found in prev:
                    pts.append(found[0]);found=prev[found]
                pts.append(start);pts.reverse()
                pts=[(sx,sy)]+pts+[(tx,ty)]
                compressed=[pts[0]]
                for p,q,r in zip(pts,pts[1:],pts[2:]):
                    if (q[0]-p[0],q[1]-p[1]) != (r[0]-q[0],r[1]-q[1]):compressed.append(q)
                compressed.append(pts[-1])
                score=seen[(end,prev.get((end,(0,0)),(None,None))[1])] if False else len(compressed)*5 + sum(abs(q[0]-p[0])+abs(q[1]-p[1]) for p,q in zip(compressed,compressed[1:]))
                if best is None or score<best[0]:best=(score,compressed)
        if best is None:
            if include_endpoint_labels:
                return self._route(source,target,False)
            raise RuntimeError(f"No route {source}->{target}")
        return best[1]

    def write(self):
        for i,(src,dst,title,dashed,color) in enumerate(self.edges):
            pts=self._route(src,dst)
            self.routed.append(pts)
            a,b=self.nodes[src],self.nodes[dst]
            def rel(point,box):
                return ((point[0]-box[0])/(box[2]-box[0]),(point[1]-box[1])/(box[3]-box[1]))
            ex,ey=rel(pts[0],a);ix,iy=rel(pts[-1],b)
            s={"edgeStyle":"none","rounded":"0","html":"1","strokeColor":color,"strokeWidth":"2",
               "endArrow":"block","endFill":"1","fontSize":str(self.font),"fontStyle":"1",
               "fontColor":"#334155","labelBackgroundColor":"#ffffff",
               "exitX":str(ex),"exitY":str(ey),"exitDx":"0","exitDy":"0",
               "entryX":str(ix),"entryY":str(iy),"entryDx":"0","entryDy":"0"}
            if dashed:s["dashed"]="1"
            c=ET.SubElement(self.base,"mxCell",id=f"edge_{i}",value=title,style=style_str(s),edge="1",parent="1",source=src,target=dst)
            g=ET.SubElement(c,"mxGeometry",relative="1",x="0",y="-18",**{"as":"geometry"})
            arr=ET.SubElement(g,"Array",**{"as":"points"})
            for x,y in pts[1:-1]:ET.SubElement(arr,"mxPoint",x=str(x),y=str(y))
        ET.indent(self.root,space="  ")
        (HERE/f"{self.name}.drawio").write_bytes(ET.tostring(self.root,encoding="utf-8",xml_declaration=True))


def cloud():
    d=Diagram("Arquitectura_Fisica_Nube_v3",2025,1410,35)
    d.icon("pc","pc","PC/Laptop",600,-35)
    d.icon("phone","phone","Smartphones",900,-35)
    d.icon("tablet","tablet","Tablets",1200,-35)
    d.group("aws","AWS Cloud",10,90,2000,1300,color="#475569")
    d.group("monitor","Monitoreo y seguridad",40,145,560,335,"aws",dashed=True)
    for k,t,x,y in [("cloudwatch","CloudWatch",110,205),("kms","KMS",340,205),
                    ("secrets","Secrets\nManager",110,325),("guardduty","GuardDuty",340,325)]:
        d.icon(k,k,t,x,y,"monitor",size=56,label_width=165)
    d.group("shield_group","AWS Shield Advanced",630,145,520,335,"aws",color="#DD344C",dashed=True)
    for k,t,x,y in [("route","Route 53",700,205),("cloudfront","CloudFront",940,205),("waf","WAF",820,325)]:
        d.icon(k,k,t,x,y,"shield_group",size=60)
    d.icon("api","api","API Gateway",1280,220,"aws")
    d.icon("ecr","ecr","ECR",1530,220,"aws")
    d.icon("alb","alb","ALB",1330,400,"aws",size=56)
    d.group("sa","sa-east-1",40,500,1510,890,"aws",color="#00A6B2")
    d.group("prod","VPC Prod",60,550,1465,500,"sa",color="#8C4FFF")
    d.group("az1","AZ 1 · sa-east-1a",80,620,700,420,"prod",color="#147EBA")
    d.group("az2","AZ 2 · sa-east-1b",805,620,700,420,"prod",color="#147EBA")
    for k,kind,t,x,y in [("f1","fargate","ECS\nFargate",145,680),("k1","keycloak","Keycloak\n(Fargate)",360,680),
                          ("a1","aurora","Aurora\nPostgreSQL",615,680),("r1","redis","ElastiCache\nprimario",350,850),
                          ("dms","dms","DMS",130,850)]:d.icon(k,kind,t,x,y,"az1",size=56,label_width=170)
    for k,kind,t,x,y in [("f2","fargate","ECS\nFargate",870,680),("k2","keycloak","Keycloak\n(Fargate)",1085,680),
                          ("a2","aurora","Aurora\nPostgreSQL",1340,680),("r2","redis","ElastiCache\nréplica",1020,850)]:
        d.icon(k,kind,t,x,y,"az2",size=56,label_width=170)
    services=[("iot","iot","IoT Core",105,1060),("lambda","lambda","Lambda",355,1060),
              ("ddb","dynamodb","DynamoDB",605,1060),("sqs","sqs","SQS FIFO",855,1060),
              ("sns","sns","SNS",1105,1060),("transfer","transfer","Transfer\nFamily (AS2)",1355,1060),
              ("glue","glue","Glue",650,1235),("s3","s3","S3",875,1235),
              ("redshift","redshift","Redshift",1100,1235),("quicksight","quicksight","QuickSight",1325,1235)]
    for k,kind,t,x,y in services:d.icon(k,kind,t,x,y,"sa",size=56,label_width=170)
    d.group("hub","VPC Hub",80,1170,430,210,"sa",color="#8C4FFF")
    d.icon("tgw","tgw","Transit\nGateway",150,1225,"hub",size=56)
    d.icon("vpn","vpn","Site-to-Site\nVPN",350,1225,"hub",size=56)
    d.group("dr","us-east-1",1580,500,410,760,"aws",color="#00A6B2")
    for k,kind,t,x,y in [("dr_f","fargate","Fargate\nreducido",1658,610),("dr_a","aurora","Aurora\nréplica",1860,610),
                          ("dr_d","dynamodb","DynamoDB\nréplica",1658,800),("dr_s","s3","S3\nréplica",1860,800),
                          ("backup","backup","AWS Backup",1755,1030)]:
        d.icon(k,kind,t,x,y,"dr",size=56,label_width=145)
    d.annotation("lbl_global_db","Global Database",1200,500,320,45,"sa")
    d.annotation("lbl_global_tables","Global Tables",1640,955,300,45,"dr")
    d.annotation("lbl_s3","réplica S3",1680,1160,220,45,"dr")
    for s,t in [("pc","route"),("phone","route"),("tablet","route"),("route","cloudfront"),
                ("cloudfront","waf"),("waf","cloudfront"),("cloudfront","api"),("api","alb"),
                ("alb","f1"),("alb","f2"),("ecr","f1"),("ecr","f2"),
                ("f1","k1"),("f2","k2"),("f1","a1"),("f2","a2"),("f1","r1"),("f2","r2"),
                ("dms","a1"),("f1","sqs"),("f2","sqs"),("f1","ddb"),("f2","ddb"),
                ("iot","lambda"),("lambda","ddb"),("sqs","f1"),("ddb","glue"),
                ("glue","s3"),("s3","redshift"),("redshift","quicksight"),
                ("tgw","vpn"),("tgw","prod"),("tgw","sqs"),("tgw","dms")]:
        if t in d.nodes:d.connect(s,t)
    for s,t in [("a1","a2"),("r1","r2"),("a1","dr_a"),("ddb","dr_d"),("s3","dr_s")]:
        d.connect(s,t,dashed=True)
    d.connect("dr_a","backup")
    d.connect("sqs","sns")
    d.connect("f1","transfer")
    d.write()


def general():
    d=Diagram("Arquitectura_Fisica_General_v3",2400,1800,43)
    for k,kind,t,x in [("pc","pc","PC/Laptop",850),("phone","phone","Smartphones",1200),
                        ("tablet","tablet","Tablets",1550)]:d.icon(k,kind,t,x,-10,size=60)
    d.group("aws","AWS Cloud",20,130,2360,890,color="#475569")
    for k,kind,t,x in [("route","route","Route 53",780),("cf","cloudfront","CloudFront",1030),
                        ("waf","waf","WAF",1280),("api","api","API\nGateway",1530)]:
        d.icon(k,kind,t,x,205,"aws",size=60)
    d.group("sa","sa-east-1",40,400,1820,590,"aws",color="#00A6B2")
    d.group("prod","VPC Prod · dos AZ",60,470,1780,280,"sa",color="#8C4FFF")
    for k,kind,t,x in [("alb","alb","ALB",100),("f","fargate","ECS\nFargate",350),
                        ("key","keycloak","Keycloak",600),("aur","aurora","Aurora\nPostgreSQL",850),
                        ("cache","redis","ElastiCache",1100),("ddb","dynamodb","DynamoDB",1350),
                        ("sqs","sqs","SQS FIFO",1600)]:
        d.icon(k,kind,t,x,550,"prod",size=60,label_width=215)
    for k,kind,t,x in [("iot","iot","IoT Core",100),("s3","s3","S3",380),
                        ("rs","redshift","Redshift",660)]:d.icon(k,kind,t,x,805,"sa",size=60)
    d.group("hub","VPC Hub",1010,765,810,205,"sa",color="#8C4FFF")
    d.icon("tgw","tgw","Transit\nGateway",1300,790,"hub",size=60)
    d.icon("vpn","vpn","Site-to-Site\nVPN",1600,790,"hub",size=60)
    d.group("dr","us-east-1",1890,400,470,590,"aws",color="#00A6B2")
    for k,kind,t,x,y in [("dra","aurora","Aurora\nréplica",1950,550),
                          ("drd","dynamodb","DynamoDB\nréplica",2180,550),
                          ("drs","s3","S3 réplica",2065,805)]:
        d.icon(k,kind,t,x,y,"dr",size=60,label_width=210)
    d.group("talca","CD Talca · sala técnica",20,1050,770,720,color="#475569")
    d.group("conce","CD Concepción · borde",815,1050,770,720,color="#475569")
    d.group("cross","Cross-docking × 3",1610,1050,770,720,color="#475569")
    d.group("talca_fwgroup","Par HA",250,1125,350,195,"talca",dashed=True)
    d.icon("talca_fib","fibra","Fibra",75,1160,"talca",size=58)
    d.icon("talca_lte","lte","LTE",185,1160,"talca",size=58)
    d.icon("talca_fw","firewall","Activo",315,1195,"talca_fwgroup",size=58)
    d.icon("talca_fw2","firewall","Pasivo",475,1195,"talca_fwgroup",size=58)
    d.icon("talca_sw","switch","Switch",660,1180,"talca",size=58)
    d.group("talca_vm","Proxmox · 3 nodos",70,1335,710,195,"talca",dashed=True)
    for k,kind,t,x in [("twms","vm","WMS",150),("tdb","db","PostgreSQL",375),
                        ("tmq","rabbit","RabbitMQ",625)]:d.icon(k,kind,t,x,1410,"talca_vm",size=58)
    d.group("talca_bodega","Bodega",40,1535,250,215,"talca",dashed=True)
    d.group("talca_frio","Cadena de frío",310,1535,470,215,"talca",dashed=True)
    d.icon("talca_term","terminal","Terminal",145,1610,"talca_bodega",size=58)
    d.icon("talca_sens","sensor","Sensores",415,1610,"talca_frio",size=58)
    d.icon("talca_gw","greengrass","GW IoT",650,1610,"talca_frio",size=58)
    d.icon("conce_fib","fibra","Fibra",850,1160,"conce",size=58)
    d.icon("conce_lte","lte","LTE",1000,1160,"conce",size=58)
    d.icon("conce_fw","firewall","Firewall",1170,1160,"conce",size=58)
    d.icon("conce_sw","switch","Switch",1390,1160,"conce",size=58)
    d.group("conce_vm","Proxmox · C01/C02",860,1310,680,220,"conce",dashed=True)
    d.icon("cwms","vm","WMS",980,1390,"conce_vm",size=58)
    d.icon("cdb","db","PostgreSQL",1280,1390,"conce_vm",size=58)
    d.group("conce_bodega","Bodega",835,1535,250,215,"conce",dashed=True)
    d.group("conce_frio","Cadena de frío",1105,1535,470,215,"conce",dashed=True)
    d.icon("conce_term","terminal","Terminal",940,1610,"conce_bodega",size=58)
    d.icon("conce_sens","sensor","Sensores",1210,1610,"conce_frio",size=58)
    d.icon("conce_gw","greengrass","GW IoT",1445,1610,"conce_frio",size=58)
    d.icon("star","starlink","Starlink",1685,1160,"cross",size=58)
    d.icon("clte","lte","LTE\n2 SIM",1850,1130,"cross",size=58)
    d.icon("cfw","firewall","Firewall",2020,1160,"cross",size=58)
    d.icon("csw","switch","Switch",2200,1160,"cross",size=58)
    d.group("mini_group","Mini-PC · Docker",1780,1310,570,310,"cross",dashed=True)
    d.icon("mini","vm","WMS · PostgreSQL\nRabbitMQ · caché\nADOT",2035,1380,"mini_group",size=58,label_width=540)
    d.icon("scanner","terminal","Escáneres\nGS1",1720,1580,"cross",size=58)
    d.annotation("lbl_replica","replicación",1940,335,270,48,"aws")
    # La nube resume un subconjunto; los flujos entre sitios mantienen sus conexiones clave.
    for s,t in [("pc","route"),("phone","route"),("tablet","route"),("route","cf"),("cf","waf"),
                ("waf","api"),("api","alb"),("alb","f"),("f","key"),("f","aur"),("f","cache"),
                ("f","sqs"),("iot","ddb"),("ddb","drd"),("aur","dra"),("s3","drs"),
                ("tgw","vpn"),("talca_fib","talca_fw"),("talca_lte","talca_fw"),
                ("talca_fw2","talca_sw"),("talca_fw","talca_fw2"),("talca_sw","twms"),
                ("twms","tdb"),("twms","tmq"),("talca_term","talca_sw"),
                ("talca_sens","talca_gw"),("talca_gw","talca_sw"),
                ("conce_fib","conce_fw"),("conce_lte","conce_fw"),("conce_fw","conce_sw"),
                ("conce_sw","cwms"),("cwms","cdb"),("conce_term","conce_sw"),
                ("conce_sens","conce_gw"),("conce_gw","conce_sw"),
                ("star","cfw"),("clte","cfw"),("cfw","csw"),("csw","mini"),
                ("scanner","mini"),("talca_fw","tgw"),("conce_fw","tgw"),("cfw","tgw")]:
        d.connect(s,t,"",
                  dashed=(s,t) in [("ddb","drd"),("aur","dra"),("s3","drs"),("talca_lte","talca_fw"),("conce_lte","conce_fw"),("clte","cfw")])
    d.write()


if __name__=="__main__":
    cloud()
    general()
