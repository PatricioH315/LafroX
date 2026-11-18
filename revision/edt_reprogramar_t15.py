# -*- coding: utf-8 -*-
"""Reprogramación del T-15 para la EDT por productos (17-11-2026), en códigos vigentes.

1. Olas de construcción de los módulos de la Etapa 1 (equipos de 3 a 6 personas).
2. Intercambio electrónico con las cadenas (3.6.5 desde el mes 9; 3.6.6 en los meses 16-18).
3. Predecesoras para los 77 paquetes con entregable que no tenían.
Modifica formulario-t15/tablas/tab_T15_2.tex y tab_T15_paquetes.tex. La traducción a
los códigos nuevos se hace después con edt_recodificar.py.
"""
import io, math, os, re, sys
from datetime import date, timedelta
from bisect import bisect_left
sys.stdout.reconfigure(encoding='utf-8')
RAIZ = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
T = os.path.join(RAIZ, 'formulario-t15', 'tablas')
BS2 = chr(92) * 2

# ---- calendario hábil (mismo criterio que cpm_acta_integrada_20261109.py) ----
def easter(y):
    a=y%19; b=y//100; c=y%100; d=b//4; e=b%4; f=(b+8)//25
    g=(b-f+1)//3; h=(19*a+b-d-g+15)%30; i=c//4; k=c%4
    l=(32+2*e+2*i-h-k)%7; m=(a+11*h+22*l)//451
    n=h+l-7*m+114
    return date(y,n//31,n%31+1)
def holidays(y):
    r={date(y,m,d) for m,d in [(1,1),(5,1),(5,21),(7,16),(8,15),(9,18),(9,19),(11,1),(12,8),(12,25)]}
    r |= {easter(y)-timedelta(days=2), easter(y)-timedelta(days=1)}
    for m,d in [(6,29),(10,12)]:
        x=date(y,m,d)
        if x.weekday() in (1,2,3): x-=timedelta(days=x.weekday())
        elif x.weekday()==4: x+=timedelta(days=3)
        r.add(x)
    x=date(y,10,31)
    if x.weekday()==1:x-=timedelta(days=4)
    elif x.weekday()==2:x+=timedelta(days=2)
    r.add(x)
    if date(y,9,18).weekday()==1:r.add(date(y,9,17))
    if date(y,9,18).weekday()==2:r.add(date(y,9,20))
    if date(y,9,18).weekday()==5:r.add(date(y,9,17))
    if date(y,1,1).weekday()==6:r.add(date(y,1,2))
    r.add(date(y,6,{2027:21,2028:20,2029:20,2030:21,2031:21,2032:20}[y]))
    return r
HOL=set().union(*(holidays(y) for y in range(2027,2033)))
CAL=[date(2027,1,1)+timedelta(days=n) for n in range(2200)]
CAL=[d for d in CAL if d.weekday()<5 and d not in HOL]
def ix(d): return bisect_left(CAL,d)
def mes(d): return (d.year-2027)*12+d.month-1   # mes contractual (febrero 2027 = 1)
def dmy(d): return d.strftime('%d-%m-%Y')
def coma(x): return ('%.1f' % x).replace('.', ',')

def filas(nombre):
    p=os.path.join(T,nombre); txt=io.open(p,encoding='utf8').read()
    return p, txt

# ---- 1. olas de módulos ----
_, t2 = filas('tab_T15_2.tex')
HH = {}
for l in t2.splitlines():
    m=re.match(r'\s*(\d+(?:\.\d+)+)\s*&',l)
    if m:
        c=[x.strip() for x in l.strip().replace(BS2,'').split('&')]
        HH[c[0]]=float(c[7])
def dur_modulo(hh,p):  # misma fórmula del CPM para módulos (puertas A01/A02 y A12)
    return 3*math.ceil(80/(6.4*p))+math.ceil((hh-240)/(6.4*p))
OLAS=[  # código, personas máx., inicio (fecha | (pred, 'A02'|'fin')), predecesoras agregadas
 ('3.4.1',4,date(2027,6,10),''),
 ('3.4.2',5,date(2027,6,10),''),
 ('3.4.6',6,date(2027,6,10),''),
 ('3.4.3',5,('3.4.2','A02'),'3.4.2 CC'),
 ('3.4.4',6,('3.4.2','A02'),'3.4.2 CC'),
 ('3.4.5',4,('3.4.2','A02'),'3.4.2 CC'),
 ('3.4.9',3,('3.4.2','fin'),'3.4.2'),
 ('3.4.7',5,('3.4.1','fin'),'3.4.1'),
 ('3.4.8',7,('3.4.6','fin'),'3.4.6'),
 ('3.4.10',6,('3.4.8','A02'),'3.4.8 CC'),
 ('3.4.11',6,('3.4.4','fin'),'3.4.4'),
]
PROG={}
for c,p,ini,extra in OLAS:
    if isinstance(ini,tuple):
        pc,tipo=ini; s0,f0=PROG[pc][0],PROG[pc][1]
        ini = CAL[ix(s0)+2*math.ceil(80/(6.4*PROG[pc][2]))] if tipo=='A02' else CAL[ix(f0)+1]
    i0=ix(ini); d=dur_modulo(HH[c],p); fin=CAL[i0+d-1]
    PROG[c]=(CAL[i0],fin,p,d,extra)
# ---- 2. intercambio con las cadenas ----
PROG['3.6.5']=(date(2027,10,1),date(2028,5,31),2,None,'3.1.2 CC, 3.5.1 (QA)')
PROG['3.6.6']=(date(2028,5,2),date(2028,7,14),2,None,'3.6.5 CC, 3.5.1 (QA)')
PROG['3.6.4']=(date(2027,7,20),date(2027,8,16),4,None,'')  # fechas niveladas por capacidad de DES
PROG['3.6.3']=(date(2027,8,16),date(2027,9,10),4,None,'')  # mapas en agosto-septiembre: baja el pico de DES de julio

# ---- 3. predecesoras de los 77 ----
NUEVAS={
 '1.1.1':'Inicio del contrato','1.1.2':'1.1.1 CC','1.1.3':'1.1.1 CC','1.2.1':'1.1.2 CC','1.2.3':'1.1.1 CC',
 '1.2.4':'1.2.1, 1.3.2 CC','1.2.5':'3.8.7','1.3.1':'1.1.1','1.3.2':'1.2.1','1.3.3':'1.3.2 CC',
 '1.3.4':'1.3.3 CC','1.4.1':'1.1.1 CC','1.4.2':'1.4.1 CC','1.5.1':'1.2.1','1.6.1':'1.3.1',
 '1.7.1':'2.1.2','1.7.2':'1.7.1','1.9.1':'1.1.1 CC','1.9.2':'1.1.1 CC','1.9.3':'1.9.2',
 '2.1.2':'1.2.1, 2.3.1 CC','2.1.3':'1.2.1','2.1.4':'1.2.5 CC','2.2.1':'1.9.1, 2.1.1 CC',
 '2.2.3':'2.2.1','2.2.4':'1.9.1','2.3.1':'Inicio del contrato','2.3.2':'2.3.1 CC','2.3.3':'2.3.1',
 '2.5.1':'2.1.2','2.5.2':'2.1.2, 2.5.1 CC','2.6.1':'1.4.1','2.6.2':'2.6.1','2.6.3':'2.6.2',
 '3.1.4':'3.2.1 CC, 2.4.1','3.1.5':'3.1.1 CC','3.3.3':'1.2.3, 2.4.1','3.3.4':'1.2.3, 3.2.3',
 '3.3.5':'2.1.3, 2.4.1','3.3.6':'2.4.1, 3.3.1 CC','3.10.1.1':'2.4.1','3.10.2.1':'1.2.1',
 '3.10.3.1':'1.2.1, 2.1.3 CC','3.10.4.1':'3.4.8, 1.2.5 CC','4.3.4':'3.9.6','5.1.1':'1.2.1',
 '5.1.3':'5.1.1, 5.1.2','5.2.1':'2.1.2 CC','5.2.2':'5.2.1','5.2.3':'2.4.1','5.3.1':'2.1.2',
 '5.3.2':'2.1.2','5.3.3':'2.3.3','5.4.1':'1.4.2, 7.2.3','5.4.2':'7.2.3','5.4.3':'3.5.4',
 '5.4.4':'3.1.4','6.2.1':'6.1.1, 2.3.2','6.2.2':'6.2.1','6.2.3':'6.2.2, 2.3.3','6.3.3':'2.3.3, 5.1.2',
 '6.3.4':'6.3.3','6.4.1':'6.1.5','6.4.2':'6.1.5','6.4.3':'6.4.1','6.5.2':'5.1.3, 3.6.2',
 '6.5.3':'5.1.3, 6.2.3','6.5.5':'5.1.3','6.5.6':'5.1.3, 6.2.3','7.1.1':'2.6.3, 4.1.1 CC',
 '7.1.6':'7.1.1 CC','7.2.2':'2.4.2, 3.6.5 CC','7.2.3':'1.4.1','7.3.1':'7.1.1, 4.2.1 CC',
 '7.3.2':'3.5.4, 3.9.2','9.1.1':'3.9.6','9.2.2':'9.2.1 CC',
}

# ---- aplicar a tab_T15_2 (ventanas en meses) ----
p2, t2 = filas('tab_T15_2.tex')
L=[]
for l in t2.splitlines():
    m=re.match(r'(\s*)(\d+(?:\.\d+)+)(\s*&\s*\w+\s*&\s*\w+\s*&\s*)(\d+–\d+)(.*)$',l)
    if m and m.group(2) in PROG:
        a,b=PROG[m.group(2)][0],PROG[m.group(2)][1]
        l=m.group(1)+m.group(2)+m.group(3)+'%d–%d' % (mes(a),mes(b))+m.group(5)
    L.append(l)
io.open(p2,'w',encoding='utf8',newline='\n').write('\n'.join(L)+'\n')

# ---- aplicar a tab_T15_paquetes ----
pp, tp = filas('tab_T15_paquetes.tex')
L=[]; cambios=0
for l in tp.splitlines():
    m=re.match(r'\s*(\d+(?:\.\d+)+)\s*&',l)
    if m:
        c=[x.strip() for x in l.strip()[:-2].split(' & ')] if l.strip().endswith(BS2) else None
        assert c and len(c)==7, l
        cod=c[0]
        if cod in PROG:
            a,b,p,d,extra=PROG[cod]
            dias=ix(b)-ix(a)+1
            prom=min(p, HH[cod]/(6.4*dias))
            c[2]='%s / %d' % (coma(max(prom, 0.1)), p)
            c[4],c[5]=dmy(a),dmy(b)
            if extra:
                c[6]=(c[6]+', '+extra) if c[6] not in ('—','') else extra
            cambios+=1
        if cod in NUEVAS:
            assert c[6] in ('—',''), (cod,c[6])
            c[6]=NUEVAS[cod]; cambios+=1
        l='  '+' & '.join(c)+' '+BS2
    L.append(l)
io.open(pp,'w',encoding='utf8',newline='\n').write('\n'.join(L)+'\n')
print('filas modificadas', cambios)
for c,(a,b,p,d,extra) in PROG.items():
    print(c, dmy(a), dmy(b), p, d, 'meses %d–%d' % (mes(a),mes(b)))
