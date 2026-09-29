// Generación reproducible de las dos vistas mxGraphModel, sin compresión.
// Las coordenadas se expresan en el lienzo; parent conserva la jerarquía draw.io.
const fs = require('fs');
const path = require('path');
const out = __dirname;
const esc = s => String(s).replace(/&/g, '&amp;').replace(/</g, '&lt;').replace(/>/g, '&gt;').replace(/"/g, '&quot;');

function diagram(name) {
  const cells = [];
  const nodes = new Map([['1', {x:0,y:0,w:0,h:0}]]);
  let count = 0;
  function vertex(key, value, x,y,w,h, style, parent='1') {
    if (nodes.has(key)) throw Error('ID repetido: '+key);
    const p = nodes.get(parent);
    if (!p) throw Error('Padre desconocido: '+parent);
    nodes.set(key,{x,y,w,h,parent,ax:p.ax===undefined?x:p.ax+x,ay:p.ay===undefined?y:p.ay+y});
    cells.push(`<mxCell id="${key}" value="${esc(value)}" style="${esc(style)}" vertex="1" parent="${parent}"><mxGeometry x="${x}" y="${y}" width="${w}" height="${h}" as="geometry"/></mxCell>`);
    return key;
  }
  const group = (key,title,x,y,w,h,kind='plain',parent='1') => {
    const color = kind==='cloud'?'#232F3E':kind==='region'?'#1B7F98':kind==='vpc'?'#7B5AA6':'#8295A8';
    const fill = kind==='cloud'?'#F6FAFD':kind==='region'?'#F8FCFC':kind==='vpc'?'#FBF9FE':'#FFFFFF';
    const aws = kind==='cloud'?'grIcon=mxgraph.aws4.group_aws_cloud_alt;':kind==='region'?'grIcon=mxgraph.aws4.group_region;':kind==='vpc'?'grIcon=mxgraph.aws4.group_vpc2;':'';
    const shape = kind==='plain'?'rounded=1;arcSize=10;':'shape=mxgraph.aws4.group;'+aws;
    return vertex(key,title,x,y,w,h,`html=1;${shape}whiteSpace=wrap;container=1;collapsible=0;align=left;verticalAlign=top;spacingLeft=42;spacingTop=10;fontSize=28;fontStyle=1;fontColor=${color};strokeColor=${color};strokeWidth=2;fillColor=${fill};`,parent);
  };
  const box = (key,label,x,y,w,h,parent='1',fill='#FFFFFF',font=24,spacing=8) => vertex(key,label,x,y,w,h,`rounded=1;arcSize=12;whiteSpace=wrap;html=1;align=center;verticalAlign=middle;spacing=${spacing};fontSize=${font};fontStyle=1;fontColor=#243746;strokeColor=#496779;strokeWidth=2;fillColor=${fill};`,parent);
  const zone = (key,label,x,y,w,h,parent) => vertex(key,label,x,y,w,h,'rounded=0;whiteSpace=wrap;html=1;align=center;verticalAlign=middle;spacing=0;fontSize=24;fontStyle=1;fontColor=#243746;strokeColor=#147EBA;strokeWidth=2;dashed=1;fillColor=#F3F8FC;',parent);
  const icon = (key,label,res,x,y,parent='1') => {
    const color = res==='waf'?'#C7131F':res==='ecr'?'#D05C17':'#5A30B5';
    return vertex(key,label,x,y,56,56,`shape=mxgraph.aws4.resourceIcon;resIcon=mxgraph.aws4.${res};html=1;whiteSpace=wrap;aspect=fixed;verticalLabelPosition=bottom;verticalAlign=top;align=center;fontSize=24;fontStyle=1;fontColor=#243746;strokeColor=#FFFFFF;strokeWidth=2;fillColor=${color};`,parent);
  };
  function edge(key,source,target,exit,entry,points=[],label='',extra='',labelOptions={}) {
    const route = points.length?`<Array as="points">${points.map(p=>`<mxPoint x="${p[0]}" y="${p[1]}"/>`).join('')}</Array>`:'';
    const style=`edgeStyle=none;rounded=0;html=1;orthogonal=0;endArrow=block;endFill=1;strokeWidth=2;strokeColor=#526B7A;fontSize=24;fontStyle=1;fontColor=#233746;labelBackgroundColor=#FFFFFF;exitX=${exit[0]};exitY=${exit[1]};exitDx=0;exitDy=0;entryX=${entry[0]};entryY=${entry[1]};entryDx=0;entryDy=0;${extra}`;
    const geometryAttrs=`relative="1" x="${labelOptions.x||0}" y="${labelOptions.y||0}" as="geometry"`;
    const offset=labelOptions.offset?`<mxPoint x="${labelOptions.offset[0]}" y="${labelOptions.offset[1]}" as="offset"/>`:'';
    cells.push(`<mxCell id="${key}" value="${esc(label)}" style="${esc(style)}" edge="1" parent="1" source="${source}" target="${target}"><mxGeometry ${geometryAttrs}>${route}${offset}</mxGeometry></mxCell>`);
  }
  function write() {
    const xml=`<?xml version="1.0" encoding="UTF-8"?>\n<mxfile host="app.diagrams.net" modified="2026-09-26T00:00:00.000Z" agent="LafroX" version="24.7.17" type="device"><diagram id="${name}" name="Página 1"><mxGraphModel dx="1600" dy="1000" grid="1" gridSize="10" guides="1" tooltips="1" connect="1" arrows="1" fold="1" page="1" pageScale="1" pageWidth="1700" pageHeight="1100" math="0" shadow="0"><root><mxCell id="0"/><mxCell id="1" parent="0"/>${cells.join('')}</root></mxGraphModel></diagram></mxfile>\n`;
    fs.writeFileSync(path.join(out,name+'.drawio'),xml,'utf8');
  }
  return {group,box,zone,icon,edge,write,nodes};
}

if (!process.argv.includes('--nube')) {
 const d=diagram('Arquitectura_Fisica_General_v2');
 d.box('users','Portales: clientes, transportistas, proveedores<br>Preventa y reparto en terreno',385,0,830,85);
 d.group('cloud','AWS Cloud',20,115,1560,710,'cloud');
 d.box('border','Borde y protección<br>Route 53 · CloudFront · AWS WAF<br>Shield Advanced · API Gateway',430,65,700,110,'cloud','#EEF4FA',24,4);
 d.group('sa','sa-east-1 · región primaria',30,205,1030,480,'region','cloud');
 d.group('dr','us-east-1 · DR',1090,205,440,480,'region','cloud');
 d.box('app','Aplicación · ECS Fargate<br>Laravel · Keycloak<br>motor de rutas',25,65,450,135,'sa','#EFF7FD');
 d.box('data','Datos operacionales<br>Aurora PostgreSQL · ElastiCache<br>DynamoDB',525,65,450,135,'sa','#F3F0FB',24,4);
 d.box('integration','Integración · SQS FIFO · SNS<br>IoT Core · Lambda · DMS<br>Transfer Family (AS2)',25,215,450,130,'sa','#FDF4F8',24,0);
 d.box('analytics','Analítica<br>S3 · Glue · Redshift Serverless<br>QuickSight',525,215,450,130,'sa','#F5F6FC',24,0);
 d.box('security','Seguridad / observabilidad<br>KMS · Secrets Manager<br>GuardDuty · CloudWatch',25,360,485,100,'sa','#F8F8F8',24,0);
 d.box('hub','VPC Hub · VPN IPsec<br>Transit Gateway<br>Site-to-Site VPN',540,360,415,100,'sa','#F8F5FC',24,0);
 d.box('drdata','Aurora Global Database<br>DynamoDB Global Tables<br>S3 · AWS Backup<br>ECS Fargate reducido',30,70,380,250,'dr','#F2F7FA');
 d.box('talca','CD Talca · sala técnica<br>Proxmox VE · VM-01 a VM-06<br>Firewall HA · NAS WORM<br>ERP 2017 · fibra + LTE',20,850,495,145,'1','#F3F8FB');
 d.box('conce','CD Concepción · gabinete de borde<br>Proxmox VE: VM-C01 a VM-C04<br>Fibra + LTE',552,850,495,145,'1','#F3F8FB');
 d.box('cross','Cross-docking × 3<br>Mini-PC industrial · Docker Compose<br>Starlink + LTE doble SIM',1084,850,495,145,'1','#F3F8FB');
 d.edge('e1','users','border',[0.5,1],[0.5,0]);
 d.edge('e2','border','app',[0.5,1],[0,0.481481481],[[800,300],[70,300],[70,450]]);
 d.edge('e3','app','data',[1,0.5],[0,0.5]);
 d.edge('e4','app','integration',[0.5,1],[0.5,0]);
 d.edge('e5','data','analytics',[0.5,1],[0.5,0]);
 d.edge('e6','data','drdata',[1,0.5],[0.552631579,1],[[1060,452.5],[1060,700],[1350,700]],'replicación','dashed=1;',{x:0.8});
 d.edge('e7','hub','talca',[0.144578313,1],[0.5,0],[[650,845],[267.5,845]]);
 d.edge('e8','hub','conce',[0.504819277,1],[0.5,0]);
 d.edge('e9','hub','cross',[0.867469880,1],[0.5,0],[[950,845],[1331.5,845]]);
 d.write();
}

{
 const d=diagram('Arquitectura_Fisica_Nube');
 d.box('users','Usuarios · portales y terreno',500,0,600,70);
 d.group('cloud','AWS Cloud',15,95,1635,845,'cloud');
 d.group('shield','AWS Shield Advanced',350,75,480,210,'plain','cloud');
 d.icon('route','Route 53','route_53',35,75,'shield');
 d.icon('cf','CloudFront','cloudfront',175,75,'shield');
 d.icon('waf','AWS WAF','waf',315,75,'shield');
 d.icon('api','API Gateway','api_gateway',850,240,'cloud');
 d.icon('ecr','ECR','ecr',1085,55,'cloud');
 d.box('transversal','Transversales · sa-east-1<br>CloudWatch · Systems Manager · KMS<br>Secrets Manager · GuardDuty<br>Security Hub · Security Lake<br>CloudTrail · AWS Backup<br>S3 Object Lock',1010,165,540,200,'cloud','#F8F8F8',24,4);
 d.group('sa','sa-east-1 · región primaria',25,380,1200,465,'region','cloud');
 d.group('dr','us-east-1 · DR',1275,380,350,465,'region','cloud');
 d.group('prod','VPC Prod',30,55,1080,270,'vpc','sa');
 d.box('dms','AWS DMS',230,35,170,45,'prod','#F4F0FB',24,0);
 d.box('alb','Application Load Balancer',430,35,400,45,'prod','#EFF7FD',24,0);
 d.box('motor','M4 · rutas',850,30,200,40,'prod','#EFF7FD',24,0);
 d.zone('az1','AZ 1: sa-east-1a<br>ECS Fargate: API, trabajos<br>reconciliación, planificador<br>Keycloak (contenedor)<br>Aurora PostgreSQL escritor<br>ElastiCache primario',20,85,430,181,'prod');
 d.zone('az2','AZ 2: sa-east-1b<br>ECS Fargate: API, trabajos<br>reconciliación, planificador<br>Keycloak (contenedor)<br>Aurora lector promovible<br>ElastiCache réplica',630,85,430,181,'prod');
 d.box('regional','SQS FIFO · SQS · SNS · Transfer Family (AS2)<br>IoT Core → Lambda → DynamoDB · MQTTS<br>DynamoDB/S3 → Glue → S3<br>Redshift Serverless → QuickSight',30,330,720,125,'sa','#F5F5FC',24,0);
 d.group('hub','VPC Hub',780,330,340,125,'vpc','sa');
 d.box('hubservices','Transit Gateway<br>Site-to-Site VPN',20,55,300,68,'hub','#F8F5FC',24,0);
 d.box('drdata','Aurora réplica<br>Global Database<br>DynamoDB réplica<br>Global Tables<br>S3 réplica<br>ECS Fargate<br>capacidad reducida<br>AWS Backup',25,85,300,300,'dr','#F2F7FA',24,0);
 d.box('sites','Sitios on-premise · VPN IPsec · gateways MQTTS',400,950,800,45,'1','#F3F8FB',24,0);
 d.edge('n1','users','route',[0,1],[0,0.5],[[390,70],[390,273]]);
 d.edge('n2','route','cf',[1,0.5],[0,0.5]);
 d.edge('n3','cf','waf',[1,0.5],[0,0.5]);
 d.edge('n4','waf','api',[1,0.5],[0,0.5],[[780,273],[780,363]]);
 d.edge('n5','api','alb',[0.5,0],[0.8,0],[[893,315],[980,315],[980,495],[820,495]]);
 d.edge('n6','alb','az1',[0,0.5],[0.918604651,0],[[485,587.5],[485,615]]);
 d.edge('n7','alb','az2',[1,0.5],[0.488372093,0],[[910,587.5],[910,615]]);
 d.edge('n8','dms','az1',[0.5,1],[0.686046512,0]);
 d.edge('n9','az1','az2',[1,0.419889503],[0,0.419889503],[],'Aurora','dashed=1;');
 d.edge('n10','az1','az2',[1,0.751381215],[0,0.751381215],[],'ElastiCache','dashed=1;');
 d.edge('n11','sa','drdata',[1,0.591397849],[0.45,1],[[1265,750],[1265,900],[1450,900]],'replicación','dashed=1;',{x:0.8});
 d.edge('n12','hub','prod',[0.382352941,0],[0.814814815,1]);
 d.edge('n13','hub','sites',[0.529411765,1],[0.75,0]);
 d.edge('n14','hub','regional',[0,0.5],[1,0.5]);
 d.edge('n15','ecr','az2',[0,0.5],[1,0.469613260],[[1000,178],[1000,510],[1175,510],[1175,700]]);
 d.edge('n16','hub','dms',[1,0.16],[0.5,0],[[1210,825],[1210,545],[385,545]]);
 d.edge('n17','motor','az2',[0.5,1],[0.744186047,0]);
 d.write();
}
