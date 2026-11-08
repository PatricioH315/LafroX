from pathlib import Path
from decimal import Decimal as D, ROUND_HALF_UP
from collections import Counter,defaultdict
import re,json,hashlib,ast
r=Path(__file__).resolve().parents[1]
files=['08_plan_riesgos/contenido.tex','08_plan_riesgos/figuras/rbs.tex','LAFROX-Subdocumento8-Anexos.tex','LAFROX-Formulario-T-16.tex']
base={p:(r/p).read_text(encoding='utf-8') for p in files}
if (r/'tmp/cierre-s8-base.json').exists():
 assert json.loads((r/'tmp/cierre-s8-base.json').read_text(encoding='utf-8'))['original']==base,'Aplicación única'
hashes={str(p.relative_to(r.parent)):hashlib.sha256(p.read_bytes()).hexdigest() for p in (r.parent/'Informe propuesta tecnica/Informe_2_LafroX').glob('Subdocumento_*/*.pdf')}
(r/'tmp/cierre-s8-base.json').write_text(json.dumps({'original':base,'sources':hashes},ensure_ascii=False,indent=2),encoding='utf-8')
b,rb,a,f=[base[p] for p in files]
def sec(s,needle):
 i=s.index(needle);return s[i:s.index('\\end{tablalafrox}',i)]
def rows(s):return {l.split(' & ')[0]:l.split(' & ') for l in s.splitlines() if re.match(r'R-\d{3} &',l)}
reg=rows(f);q=rows(sec(a,'\\begin{tablalafrox}{Estimación acumulada'));imp=rows(sec(a,'\\begin{tablalafrox}{Fundamento del impacto'));resp=rows(sec(a,'\\begin{tablalafrox}{Matriz de respuestas'))
assert len(reg)==len(q)==len(imp)==len(resp)==35
mapping={k:f'R-{i:03}' for i,k in enumerate(reg,1)}
ciids=set(f'R-{i:03}' for i in range(1,52))-set(reg)
def rename(s):
 # Expand historical ranges before substituting IDs; never reinterpret the new IDs.
 s=re.sub(r'R-(\d{3})--R-(\d{3})',lambda m:', '.join(f'R-{i:03}' for i in range(int(m[1]),int(m[2])+1)),s)
 return re.sub(r'(?<![\w-])R-\d{3}',lambda m:mapping.get(m[0],m[0].replace('R-','CI-')),s)
num=lambda x:D(x.replace(',','.'))
rn=lambda x:x.quantize(D('.01'),rounding=ROUND_HALF_UP)
fmt=lambda x:f'{rn(D(x)):.2f}'.replace('.',',')
pretty=lambda x:format(rn(D(x)),',.2f').replace(',','X').replace('.',',').replace('X','.')
pl=lambda p:1 if p<=10 else 2 if p<=30 else 3 if p<=50 else 4 if p<=70 else 5
weights=list(map(D,['.1','.3','.5','.7','.9']))
zone=lambda e:'Baja' if e<D('.08') else 'Media' if e<D('.20') else 'Alta' if e<D('.40') else 'Crítica'
role={'Jefe de Proyecto':'JP','Arquitecto de Solución':'ARQ','Líder de Datos':'DAT','Líder de Calidad':'CAL','Líder de Operación / SRE':'SRE','Líder de Implantación y Gestión del Cambio':'IMP','Encargado de Seguridad de la Información':'SEG'}
# Hipótesis nuevas de planificación: p posterior (%), A preventiva extra (HH), C contenida en H0 (HH), ventana, evidencia de la acción y límite de contingencia.
# Las consecuencias se conservan; no se atribuye a los controles una eficacia observada.
spec={
1:(25,8,16,13,20,'Agenda EDI y certificación de cada cadena, con pruebas de intercambio y registro de pendientes.','Al D-5 sin certificación, JP escala en un día hábil y conserva pendiente la cadena; sólo ampliar tras su certificación.'),
2:(60,12,24,1,20,'Inventario de vínculos sanitarios por lote, evidencia de origen y resolución firmada de Calidad sobre cada excepción.','Plan adicional: DAT aísla el conjunto el mismo día; Calidad decide antes del corte. No cargar ni despachar lotes sin trazabilidad exigida; si no es reconstruible, elevar decisión de alcance contractual, sin inventar historia.'),
3:(30,6,16,1,18,'Extracto de tres años perfilado y reconciliado con Abastecimiento/TI; acta V-09.','A D-5 sin extracto válido, separar períodos y pedir extracción complementaria; revalidar antes de cargar.'),
4:(30,8,20,1,20,'Acta de conteo, causas de diferencias y ajustes autorizados por Bodega/Finanzas.','Bloquear corte con diferencia no explicada; DAT presenta conciliación y nueva prueba antes de la ventana autorizada.'),
5:(30,6,16,1,20,'Saldos de envases aceptados por cliente y transportista, política V-08 y evidencia de M8.','Mantener saldos afectados pendientes; Finanzas resuelve antes de su carga, sin asumir saldo cero.'),
6:(35,8,16,1,20,'Fuentes históricas de horas y montos verificadas con Comercial, Operaciones y Finanzas, V-10.','Plan adicional: JP reúne áreas dentro de dos días hábiles desde bloqueo; en cinco días hábiles exige evidencia o eleva al Comité Ejecutivo la condición contractual. No sustituir historia por mediciones futuras ni aceptar resultado sin referencia.'),
7:(25,6,16,1,18,'Universo de deuda vigente conciliado con Finanzas/TI y extracción complementaria comprobada.','No dar por migrada cartera incompleta; escalar a D-5 de cada carga y repetir conciliación.'),
8:(10,0,8,13,56,'Cola tributaria con correlación, consulta y reintento idempotente; confirmación externa conservada.','SRE registra pendiente al detectar demora, consulta dentro de 15 min y revisa cada 30 min; si afecta salida, avisa de inmediato a Finanzas/CT. No interpretar silencio como aprobación.'),
11:(20,6,12,1,20,'Matriz térmica V-11 versionada y firmada por Calidad por familia antes de certificación.','Sin parámetros aprobados, bloquear certificación del alcance afectado y escalar a D-5; no relajar bloqueo térmico.'),
12:(20,4,12,1,20,'Recepción técnica por equipo y sitio, con conformidad de TI/Operaciones antes de la ola.','A D-5 sin equipos, JP decide reprogramación de trabajo independiente en un día hábil; no certificar con sustitutos no validados.'),
13:(25,4,8,2,20,'Acuerdo operativo firmado y nómina de cada transportista antes de incorporar la ola.','A D-5 sin firma, escalar por CT el mismo día; no habilitar empresa pendiente ni reducir cobertura obligatoria.'),
14:(15,4,12,1,20,'Autorización escrita por vehículo y visita; propietario y Operaciones confirman disponibilidad.','A D-5 sin permiso, suspender visita y acordar alternativa autorizada antes de instalar.'),
15:(30,8,20,13,56,'Transacciones de muestra registradas en el flujo nuevo y cobertura certificada por turno/ola.','Si persiste flujo paralelo, IMP abre refuerzo en el siguiente turno y mide diariamente; sin evidencia de adopción no cerrar ola.'),
16:(20,6,16,1,15,'V-14, reglas y excepciones transferidas al ayudante y prueba en 13--15 sin planificador.','Retiro confirmado no cambia p0 del fallo de transferencia. Si faltan reglas, IMP inicia reconstrucción en dos días hábiles y valida antes de cerrar el piloto.'),
17:(20,4,12,1,56,'Lista de convocados, asistencia, evaluación y suplentes certificados por sesión.','Ausencia: avisar a jefatura el mismo día y fijar recuperación dentro de cinco días hábiles, antes de trabajo autónomo.'),
18:(25,4,12,1,56,'Matriz de decisión con titular y suplente; recepción de insumos y resolución trazables.','D-5 sin decisión: escalar un día hábil después; promoción regional: suplente a 15 min y decisión dentro de 30 min, sin actuar por silencio.'),
19:(20,4,12,1,56,'Recepción de respaldos por sitio y ensayo de pérdida del último camino, incluida Concepción y Los Ángeles.','SRE activa continuidad al corte y avisa a TI/CT en 15 min; comprobar conmutación menor a 30 s, ventana local y restitución antes de normalizar.'),
20:(5,0,8,13,56,'Autonomía y transferencia verificadas por componente; coordinación de energía con TI/Operaciones.','Al corte, SRE mide autonomía restante y alerta en 15 min; activar recuperación antes de agotarla y bloquear operación insegura.'),
21:(20,4,12,1,2,'Aprobación escrita de residencia/transferencia para regiones propuestas antes de habilitar datos.','Sin aprobación al mes 2, JP escala en un día hábil y ARQ presenta alternativa en cinco días hábiles; no transferir datos sin autorización.'),
22:(10,4,12,1,56,'Flujo de cambios urgentes y suplentes aprobados; autorización escrita por intervención.','Durante incidente escalar en una hora o antes si exige el servicio; contener sin intervención prohibida y conservar congelamientos.'),
28:(15,0,8,1,20,'Ventana y recorrido de prueba confirmados por Operaciones/transportista antes de salir.','Al aviso de falla, suspender prueba, notificar el mismo día y acordar recorrido dentro de dos días hábiles; repetir sólo con vehículo seguro.'),
29:(10,0,8,1,20,'Autorización de recorrido y protocolo de seguridad del CLIENTE/transportista.','Suspender de inmediato ante siniestro; coordinar el mismo día y fijar nueva ventana dentro de dos días hábiles, condicionada a autorización segura.'),
30:(10,0,8,1,20,'Custodia y seguridad del transporte corresponden al CLIENTE/transportista; evidencia de prueba preservada.','Interrumpir ante asalto, avisar el mismo día y acordar reejecución dentro de dos días hábiles; no reanudar sin habilitación segura.'),
31:(30,4,12,2,56,'Identidad, autorización, capacitación y vínculo persona--vehículo--viaje verificados en andén.','Sustituto no certificado: bloquear acceso al detectar y solicitar otro conductor ese mismo turno; verificar antes de salida.'),
32:(30,4,12,1,56,'Solicitud y análisis de impacto aprobados antes de iniciar trabajo fuera de alcance.','Registrar solicitud el mismo día; JP responde o escala en dos días hábiles y mantiene línea base hasta decisión formal.'),
33:(20,0,16,1,56,'Seguimiento de cambios aplicables con asesoría competente; decisión contractual documentada.','ARQ registra aviso el mismo día hábil, solicita interpretación dentro de dos y presenta impacto dentro de cinco tras recibirla; no inventar multas o reformas.'),
39:(25,6,12,20,56,'Reglas de costo de servir aprobadas al mes 20 y tres liquidaciones en sombra reproducidas en 21--23.','Antes del mes 24 sin acuerdo, no activar tramo variable; Finanzas/CT reciben disputa en un día hábil y mantienen servicio mientras resuelven.'),
41:(25,6,12,1,20,'Acuerdo 5.4.2 con finalidades, accesos y controles comprendidos por Operaciones/TI/sindicato.','D-5 sin acuerdo: JP escala el mismo día y conserva sólo uso operacional autorizado; no cámaras en cabina ni GPS de jornada no acordado.'),
42:(35,12,32,13,56,'Altas por turno, tutor, evaluación antes de autonomía y aprendizaje dentro de dos horas según 7.1.2.','Plan adicional: Bodega asigna cobertura certificada antes del turno; IMP/SRE revisa cada alta diariamente. Si supera tutoría, no asignar trabajo autónomo; presentar refuerzo en dos días hábiles y revalidar antes de habilitar.'),
43:(35,12,24,1,18,'Contrato de extracción e intercambio confirmado con TI; ensayo temprano sin modificar ERP y sustitución progresiva de WMS.','Plan adicional: ARQ eleva brecha al finalizar semana 2 del mes 1; TI entrega acceso o alternativa verificable antes de integración. Ensayar archivo controlado si satisface requisitos; bloquear certificación si persiste interfaz no verificable.'),
44:(35,8,16,19,20,'Disponibilidad y continuidad acordadas antes de septiembre; seguimiento diario de las seis condiciones de cierre.','Plan adicional: cerrar habilitaciones en mes 19 antes del congelamiento; JP revisa incidentes diariamente en 19--20. Escalar el mismo día una condición incumplida y acordar recuperación en dos días hábiles, sin intervención prohibida ni aceptación ficticia.'),
45:(25,6,20,1,56,'Inventario de versiones y soporte, revisión trimestral y compatibilidad probada antes del límite verificado.','Cambio excepcional: ARQ registra aviso en un día hábil y presenta transición en cinco; programar antes de fin de soporte, conservando ventanas y pruebas.'),
46:(20,4,24,1,56,'Cuentas, claves, exportación y restauración utilizable verificadas en recepción y revisión anual de salida.','Restricción efectiva: ARQ escala en un día hábil y presenta alternativas en cinco; no sustituir proveedor sin prueba/aprobación ni declarar reversibilidad por una descarga.'),
49:(25,6,20,13,56,'Procedimiento ERP con TI/Finanzas probado en AL-DTE-01/AL-DR-01 antes de H5/H10.','Al fallo ERP avisar de inmediato a TI/Finanzas, mantener sólo guías preemitidas válidas y bloquear nuevas salidas sin guía. Activar restitución con RTO 4 h/RPO 15 min exigidos; escalar a los 30 min sin recuperación encaminada.'),
51:(25,6,16,2,56,'Demostración práctica en andén e incorporación acordada con transportista y conductor habilitado.','Ante rechazo actuar antes de salida: IMP solicita conductor certificado/dispuesto ese turno y registra cobertura pendiente; refuerzo antes de siguiente asignación.')}
assert {f'R-{i:03}' for i in spec}==set(reg)
data={}; monthly=defaultdict(lambda:defaultdict(D)); cbtotal=D(0); ressum=D(0); prevent=D(0)
for oldid,row in reg.items():
 i=int(oldid[2:]);pr,A,C,start,end,evidence,cont=spec[i];p=D(q[oldid][1].split('\\')[0]);o,m,pe=map(num,q[oldid][3:6]);h=(o+4*m+pe)/6
 il,qi=row[4].split(' / ');qi=num(qi);ex=num(row[5].split(' ')[0]);owner=role[row[7].rstrip('\\').strip()];support='CAL' if owner!='CAL' else 'ARQ'
 # A es revisión adicional de coordinación/cierre, no desarrollo ni prueba ordinaria; C particiona H0, no se agrega a él.
 A=D(A);C=D(C);pr=D(pr);R=h-C;er=pr/100*R;et=A+pr/100*C;benef=p/100*h-er;ratio=benef/et if et else None;net=benef-et
 exp=weights[pl(pr)-1]*qi;new=mapping[oldid];z=zone(exp);is_high=ex>=D('.20')
 action=resp[oldid][2].replace(' Evidencia y detalle: Tabla 8.A.2.','').replace(' Evidencia y coordinación: Tabla 8.A.2.','')
 data[new]={'old':oldid,'id':new,'owner':owner,'support':support,'p':str(p),'pr':str(pr),'h':str(h),'R':str(R),'A':str(A),'C':str(C),'initialE':str(ex),'I':int(il),'qi':str(qi),'E':str(exp),'zone':z,'er':str(er),'et':str(et),'benef':str(benef),'ratio':str(ratio) if ratio is not None else None,'net':str(net),'high':is_high,'start':start,'end':end,'evidence':evidence,'cont':cont,'action':rename(action),'trigger':resp[oldid][1]}
 prevent+=A;ressum+=er;cbtotal+=et
 # Distribución propuesta uniforme en la ventana: expectativa, no fecha de materialización.
 for month in range(start,end+1):
  for rr,share in [(owner,D('.6')),(support,D('.4'))]:monthly[month][rr]+=pr/100*h*share/D(end-start+1)

def table(number,title,label,cols,heads,lines):
 return '\n'+r'\begingroup'+'\n'+r'\renewcommand{\thetable}{'+number+'}\n'+r'\begin{landscape}'+'\n'+r'\setlength{\textwidth}{\linewidth}'+'\n'+r'\renewcommand{\arraystretch}{1.08}'+'\n'+r'\begin{tablalafrox}{'+title+'}{'+label+'}{'+cols+'}{'+' & '.join(r'\cab{'+x+'}' for x in heads)+'}\n'+'\n'.join(' & '.join(row)+r' \\' for row in lines)+'\n'+r'\end{tablalafrox}'+'\n'+r'\end{landscape}'+'\n'+r'\endgroup'+'\n'

# E: recuperar el detalle de control generado en tarea 6, conservando los CI y el evento histórico.
tree=ast.parse((r/'tmp/aplicar_tarea6.py').read_text(encoding='utf-8'))
controls=next(ast.literal_eval(n.value) for n in tree.body if isinstance(n,ast.Assign) and any(isinstance(t,ast.Name) and t.id=='controls' for t in n.targets))
old51=json.loads((r/'tmp/tarea6-baseline.json').read_text(encoding='utf-8'))['original'];reg51=rows(old51['LAFROX-Formulario-T-16.tex'])
e=r'''\clearpage
\section{Anexo 8.E: Controles internos y destinos documentales}
Los 16 asuntos retirados conservan sus CI históricos. Son obligaciones de diseño, innovación y calidad del proveedor; no integran los 35 riesgos vigentes ni sus reservas. Cada ficha propone una solución verificable, no declara una prueba ejecutada. Los trece observados por la revisión del Informe 2 (p. 37) y los tres reclasificados de tarea 5 permanecen en seguimiento hasta incorporar su diseño y evidencia en S4/S9/S13. El traslado está completado en S8; la integración externa está pendiente.

CAL verifica evidencia y JP controla la solicitud de sincronización. Las familias DAT, DES e IMP pasan a SRE desde mes 22 según Tabla 8.1. Ningún defecto crítico/alto abierto ni prueba habilitante fallida permite promover (S9, 9.2.1/9.2.6). Se conserva el alcance obligatorio si una función opcional no supera sus pruebas. Los códigos CI no se renumeran. No se archivan como riesgos del CLIENTE ni se transfieren sus 411,82 HH históricas a reserva de gestión.
'''
elines=[]
for i,(owner,dest,act,test) in controls.items():
 oldid=f'R-{i:03}';elines.append([f'CI-{i:03}',owner+' '+dest,act,test])
e+=table('8.E.1','Controles internos: solución propuesta, destino y verificación. Fuente: revisión del Informe 2 y secciones S4/S9/S13 indicadas; diseño documental propuesto.','tab:cierre-ci','G{0.08} F{0.25} Y F{0.34}',['Control','Dueño y destino a sincronizar','Solución requerida','Evidencia y condición de cierre'],elines)

# F: fichas de respuesta + residual + costo-beneficio.
ft=r'''\clearpage
\section{Anexo 8.F: Respuestas, esfuerzo y riesgo residual proyectado}
\label{sec:cierre-respuestas}
Las 35 fichas complementan 8.A y T-16. A es esfuerzo preventivo adicional total en la ventana, no costo de desarrollo ni pruebas ordinarias de la EDT. Se estima una revisión extraordinaria de excepción/coordinación/cierre por riesgo: 60\% del dueño y 40\% de CAL (ARQ cuando CAL es dueño), acumulados en toda la ventana. Para vigilancia ordinaria y aceptación pasiva A=0. C es esfuerzo de respuesta condicional total, repartido en esos perfiles y contenido en el PERT H0 de 8.B, no sumado de nuevo ni multiplicado otra vez por episodios n. Son hipótesis de dos perfiles, no compromisos ni rendimientos observados. La matriz de integración debe contrastarlos con los paquetes existentes antes de aprobarlos; si una acción ya está presupuestada, se descuenta aquí y se recalculan sumas.

El plazo preventivo es el de 8.A.2 para las 28 dependencias, antes del hito/fecha allí indicado; para los siete externos se fija en cada ficha. A se ejecuta una vez como presupuesto acumulado y se programa a D-5 del primer hito afectado; si hay revisiones repetidas (p. ej. rotación), se reparte ese total, sin multiplicarlo por 44 meses ni por n. Las HH preventivas mínimas no sustituyen capacitación, mantenimiento, respaldo o controles obligatorios ya incluidos en S7.

La probabilidad posterior p1 es un juicio de planificación de ocurrencia del mismo evento y ventana de p0, condicionado a que se ejecuten los controles y se obtenga la evidencia indicada. No es frecuencia medida ni eficacia certificada; se mantiene la probabilidad de dependencias externas que LafroX no puede modificar. En historia sanitaria, retirada del planificador, energía, SII, siniestros y cambio normativo no se reduce p0 por describir una respuesta. Los otros p1 proponen menor ocurrencia por resolver temprano la dependencia especificada; esa hipótesis se invalida si no existe su acta o prueba. I1 conserva el impacto global inicial, incluyendo consecuencias sanitarias y contractuales: ni el bloqueo de salida ni una mejora de detección borran una pérdida histórica. E1 se obtiene de la banda de p1 y el factor de I1 con los mismos umbrales de 8.1.3.

El esfuerzo condicional remanente de atención es L=H0-C; no es una nueva estimación de consecuencias sanitarias ni de plazo. El esfuerzo residual esperado es p1 L. El tratamiento esperado es T=A+p1 C. El beneficio bruto en HH es B=p0 H0-p1 L. B/T compara reducción esperada de trabajo de atención con trabajo de tratamiento; el saldo neto B-T=(p0-p1)H0-A evita doble conteo. Así, costo total posterior=T+p1 L=A+p1 H0. Estos indicadores no valorizan alimentos, multas, seguridad de personas ni aceptación contractual; un retorno menor que uno se justifica por obligación o continuidad, sin eliminar el cálculo. Las respuestas contingentes no constituyen prevención adicional gratuita.

Las ventanas y rangos de p0/O/M/P se conservan. Los intervalos de programación de 8.H son hipótesis de distribución de HH, no cambian la exposición descrita en 8.B.2 ni convierten HH en días. D-5 y D-10 son días hábiles, salvo los minutos y turnos expresamente indicados. Las fechas de respuesta no sustituyen los diez días hábiles contractuales de revisión/subsanación.
'''
fl=[];rl=[];cbl=[]
for new,x in data.items():
 A,C,pr,h,R=map(D,[x['A'],x['C'],x['pr'],x['h'],x['R']]);o=x['owner'];s=x['support'];old=x['old'];ev=x['evidence'];cont=x['cont'];end=x['end'];start=x['start']
 # Contingencia coherente con respuesta existente; fechas externas completas en cont.
 preventive=x['action']+' Evidencia de salida: '+ev
 fl.append([new,preventive,cont,f'{o} / {s}; A: {fmt(A*D(".6"))}/{fmt(A*D(".4"))}; C: {fmt(C*D(".6"))}/{fmt(C*D(".4"))} HH.',f'Ventana de programación {start}--{end}. A acumulado a D-5 del primer hito afectado; para repeticiones, repartir el total. Aplicar fechas de 8.A.2 y el plazo contingente de esta fila.'])
 exp=D(x['E']);rr='Plan adicional en 8.F.1; mantener bloqueo/escalamiento y revisar diariamente hasta cerrar evidencia.' if exp>=D('.20') else 'Revisar al verificar evidencia y en comité quincenal; si falla la hipótesis, conservar la valoración inicial y activar 8.F.1.'
 rationale=('No se reduce p0: '+ev) if pr==D(x['p']) else ('Hipótesis p1='+fmt(pr)+'\\% por resolución temprana de la dependencia: '+ev)
 rl.append([new,f'{fmt(pr)}\\% / {pl(pr)} / {fmt(weights[pl(pr)-1])}',f'{x["I"]} / {fmt(D(x["qi"]))}; {fmt(exp)} ({x["zone"]})',f'L={fmt(R)} HH; p1L={fmt(D(x["er"]))} HH.',rationale+' '+rr])
 if x['high']:
  # Sensibilidad conservadora: la mejora no ocurre, p1=p0, A se mantiene.
  p=D(x['p'])/100;pf=pr/100;et=D(x['et']);ben=D(x['benef']);ratio=D(x['ratio']);loss=p*R;ts=A+p*C;ratio_sens=(p*h-loss)/ts if ts else D(0)
  breakeven=(D(x['p'])-100*A/h)
  justification='Prioridad obligatoria: proteger trazabilidad, condiciones de aceptación y continuidad; se mantiene aun con retorno HH menor que uno. Validar capacidad y elevar su esfuerzo antes del hito.' if ratio<1 else 'Eficiencia de esfuerzo favorable bajo la hipótesis p1; mantener el tratamiento por obligación y no usar B/T como autorización de aceptación.'
  cbl.append([new,f'A={fmt(A)}; C={fmt(C)}; H0={fmt(h)}; p0={fmt(D(x["p"]))}\\%; p1={fmt(pr)}\\%.',f'B={fmt(ben)}; T={fmt(et)}; B/T={fmt(ratio)}; neto={fmt(D(x["net"]))} HH.',f'Sin mejora p1=p0: B/T={fmt(ratio_sens)}; neto=-{fmt(A)} HH. Equilibrio neto: p1<={fmt(breakeven)}\\%.',justification])
ft+=table('8.F.1','Fichas ejecutables de los 35 riesgos. Fuente: 8.A y estimaciones adicionales de planificación de S8.','tab:cierre-fichas','G{0.06} Y F{0.29} F{0.15} F{0.20}',['ID','Acción preventiva y evidencia','Contingencia y plazo desde disparador','Perfiles / HH adicionales','Momento y regla de programación'],fl)
ft+=table('8.F.2','Riesgo residual proyectado, condicionado a evidencia; no resultado observado. Fuente: hipótesis por riesgo y escalas de S8.','tab:cierre-residual','G{0.06} F{0.13} F{0.17} F{0.16} Y',['ID','p1 / nivel / factor','I1 / factor; E1 y zona','Esfuerzo residual','Fundamento, evidencia y decisión posterior'],rl)
ft+=table('8.F.3','Costo-beneficio y sensibilidad de las 15 respuestas altas/críticas iniciales (HH). Fuente: modelo explícito de 8.F.','tab:cierre-cb','G{0.06} F{0.22} F{0.22} F{0.25} Y',['ID','Entradas acumuladas','Resultado esperado','Sensibilidad / umbral','Decisión y justificación'],cbl)

# G: ejecución FMEA, 15 modos con evidencia específica y detección justificada.
g=r'''\clearpage
\section{Anexo 8.G: Análisis de modos de falla y efectos (FMEA)}
FMEA aplicado a los 15 riesgos con E0 mayor o igual a 0,20. El modo de falla es el evento de T-16 y su efecto es la consecuencia allí declarada. Se trabaja con cinco niveles propios, no con una escala atribuida a una norma: severidad S=I global (1 corrección localizada, 2 ajuste de paquete, 3 reproceso sin afectar hitos, 4 amenaza a aceptación/servicio/hito, 5 consecuencia sanitaria grave o trazabilidad irrecuperable). O usa el nivel 1--5 de la misma banda de p0/p1, dentro de la ventana del evento, no una frecuencia diaria. D es dificultad para detectar antes del efecto: 1 comprobación automática integral bloqueante; 2 control documental o ensayo completo antes de liberar; 3 muestreo/reconciliación con cobertura parcial; 4 evidencia tardía o validación dispersa; 5 dato histórico no reconstruible o defecto oculto hasta el efecto.

NPR=S por O por D prioriza modos dentro de esta escala (1--125); no equivale a E, a probabilidad ni a HH. Se actúa por severidad 5 aunque NPR sea bajo. La propuesta obliga a tratar S=5, D mayor o igual a 4 y cualquier E alta/crítica. CAL conserva expediente de modo, causa, efecto, prueba y corrección. Las puntuaciones posteriores son proyecciones condicionadas a evidencia, no una FMEA de controles ya ensayados. No se usa menor NPR para dispensar requisitos o aceptar un residual alto.
'''
gl=[]
for new,x in data.items():
 if not x['high']:continue
 old=x['old'];i=int(old[2:]);sev=x['I'];oi=pl(D(x['p']));op=pl(D(x['pr']));di=5 if i in [2,6,43] else 4;dp=3 if i in [2,6] else 2
 reason='D0=5: faltante de origen o interfaz no verificable puede permanecer oculto hasta conciliar/aceptar.' if di==5 else 'D0=4: la validación distribuida puede llegar después de la fecha necesaria.'
 projected='D1=3: aun conciliando, la cobertura histórica puede ser parcial; no se reconstruye lo inexistente.' if dp==3 else 'D1=2: acta o ensayo específico previo a habilitación; se invalida la mejora de detección si no existe evidencia.'
 gl.append([new,f'S={sev}; O={oi}; D={di}; NPR={sev*oi*di}.',resp[old][1]+'. '+reg[old][1],reason+' Control/acción: '+x['evidence'],f'S1={sev}; O1={op}; D1={dp}; NPR1={sev*op*dp}. '+projected,x['cont']+' Dueño: '+x['owner']+'; verifica CAL.'])
g+=table('8.G.1','FMEA de 15 riesgos altos/críticos y evaluación posterior proyectada. Fuente: eventos T-16 y juicios de planificación de S8.','tab:cierre-fmea','G{0.06} F{0.12} F{0.22} F{0.23} F{0.18} Y',['ID','FMEA inicial','Modo, disparador y efecto','Detección inicial y control','FMEA posterior proyectada','Acción, responsable y condición de habilitación'],gl)

# H: reserva de respuesta/materialización (sin sumar C dos veces) y gestión por escenario distinto.
event=sum(D(x['pr'])/100*D(x['h']) for x in data.values())
totalafter=prevent+event
htext=r'''\clearpage
\section{Anexo 8.H: Reservas, perfiles y propuesta de integración al cronograma}
\label{sec:cierre-reservas}
La exposición inicial de 35 riesgos se mantiene en 1.183,11 HH. La historia retirada de 16 asuntos internos suma 411,82 HH; 1.183,11+411,82=1.594,93 HH anteriores. Los 411,82 no son ahorro, reserva liberada ni costo cierto de controles; E debe resolverse dentro del trabajo ordinario de arquitectura/innovación/calidad y cualquier diferencia debe estimarse, no trasladarse automáticamente al CLIENTE.

La propuesta de contingencia específica es la suma p1 H0 de los 35 eventos: incluye atención contingente C y remanente L=H0-C. La prevención A es trabajo planificado adicional y se solicita como tal, separado de reserva. No se suman otra vez la exposición inicial, p1L y T=A+p1C a p1H0. No se calcula percentil ni suficiencia estadística: FMEA no es una simulación. Las hipótesis p1 dependen de evidencia; si no se verifica, se retiene la exposición inicial para replanificar y escalar, sin gastar una reserva proyectada como si ya estuviera aprobada.

La reserva protegida de S7, Tabla 7.4, p. 33, es 3.072 HH: 1.152 en marcha blanca E1 (13--15) y 1.920 en producción/estabilización E1 (16--20). Ya integra 220.023 HH programadas sobre 216.951 HH base/cobertura. No se suma nuevamente a esos totales ni se presta a E2. No hay evidencia suficiente de coincidencia entre esas capacidades técnicas y los perfiles, causas y períodos de los riesgos del CLIENTE; por ello el crédito inicial contra la nueva contingencia es cero. JP podrá reconocer solapamiento sólo con la triple correspondencia riesgo--paquete--perfil/mes y acta de capacidad; al hacerlo, se resta exactamente una vez de la propuesta adicional, conservando la protección E1. Las fichas preventivas también se descuentan si ya están incluidas en paquetes.

Se sustituye la cifra de gestión de 1.600 HH sin derivación por una propuesta de escenario de 160 HH, sin afirmar autorización: cuatro ciclos extraordinarios por causas todavía no identificadas, uno por bloque 1--12, 13--20, 21--38 y 39--56. Cada ciclo reúne JP 8, ARQ 16, CAL 8 y SRE 8 HH: 4 por 40=160 HH. Son tolerancias de revisión, diagnóstico, coordinación y replanificación de un asunto emergente; no incluyen remediación de un riesgo conocido, tareas CI, cambios normativos ya registrados, correcciones ordinarias ni los 35 eventos. No es 10\% de 1.600 ni una probabilidad derivada de FMEA. Si el asunto se identifica como un riesgo de T-16 se reclasifica, se anula su doble imputación y se usa su contingencia específica. Si excede el sobre de 40 HH, el Comité Ejecutivo decide capacidad/cambio antes de comprometer más trabajo. Sensibilidad de tolerancia: dos ciclos por bloque exigirían 320 HH, sin adoptar ese importe ni asegurar cobertura de eventos desconocidos.

La tabla mensual distribuye p1H0 uniformemente entre los meses de atención propuestos de cada ficha, 60\% al dueño y 40\% al apoyo (CAL, o ARQ si CAL es dueño). No predice fechas de ocurrencia ni cambia la ventana probabilística. Las cantidades de cálculo conservan precisión; el redondeo de impresión a 0,01 HH puede crear diferencias de centésimas al sumar celdas; los totales se calculan sin redondear y se ajustan por última celda sólo al cargar la planilla. Prevención y gestión tienen sus propios calendarios y no están incluidas en esa tabla. La reserva distribuida es exposición esperada, no dotación comprometida: S7/T-15 debe recalcular la ruta crítica y nivelar perfiles antes de aceptarla. No se convierten HH directamente a días.
'''
sumlines=[['Exposición inicial vigente','1.183,11','Base p0/O/M/P intacta; no sumar a la proyección posterior.'],['Trabajo preventivo adicional A',fmt(prevent),'Trabajo planificado, 60/40 por ficha; descontar coincidencia con EDT antes de aprobar.'],['Contingencia específica propuesta p1H0',fmt(event),'Incluye C y L; condición: evidencia que sustenta p1.'],['Dentro de contingencia: p1C',fmt(cbtotal-prevent),'Subconjunto; no reserva adicional.'],['Dentro de contingencia: p1L',fmt(ressum),'Subconjunto de contingencia, no sumar otra vez.'],['Esfuerzo esperado posterior A+p1H0',fmt(totalafter),'Prevención más contingencia específica; sin gestión ni protección S7.'],['Gestión propuesta', '160,00','Cuatro escenarios de 40 HH; reemplaza propuesta histórica sin derivación.'],['Protección ya programada en S7','3.072,00','Sólo E1; 1.152+1.920. Crédito demostrado inicialmente cero.'],['Estimación interna histórica excluida','411,82','No pertenece a contingencia ni gestión; controles ordinarios en E.']]
htext+=table('8.H.1','Conciliación de esfuerzo y reservas, HH. Fuente: 8.B/8.F, S7 Tabla 7.4 y escenario explícito de gestión.','tab:cierre-reserva','F{0.28} G{0.14} Y',['Concepto','HH','Tratamiento y no duplicación'],sumlines)
phase=defaultdict(lambda:defaultdict(D))
for x in data.values():
 for rr,share in [(x['owner'],D('.6')),(x['support'],D('.4'))]:phase[x['start']][rr]+=D(x['A'])*share
htext+=table('8.H.2','Trabajo preventivo adicional propuesto por mes de primera atención y perfil (HH). Fuente: fichas 8.F.1; ejecutar antes del primer hito dependiente.','tab:cierre-preventiva','G{0.07} G{0.10} G{0.10} G{0.10} G{0.10} G{0.10} G{0.10} G{0.10}',['Mes','JP','ARQ','DAT','CAL','SRE','IMP','SEG'],[[str(m)]+[fmt(vals.get(rr,D(0))) for rr in ['JP','ARQ','DAT','CAL','SRE','IMP','SEG']] for m,vals in sorted(phase.items())])
htext+=table('8.H.3','Distribución mensual propuesta de contingencia específica (HH); todavía no incorporada en T-15. Fuente: p1H0 y ventanas de 8.F.','tab:cierre-mensual','G{0.06} G{0.09} G{0.09} G{0.09} G{0.09} G{0.09} G{0.09} G{0.09} G{0.10}',['Mes','JP','ARQ','DAT','CAL','SRE','IMP','SEG','Total'],[[str(m)]+[fmt(monthly[m].get(rr,D(0))) for rr in ['JP','ARQ','DAT','CAL','SRE','IMP','SEG']]+[fmt(sum(monthly[m].values()))] for m in range(1,57)])
htext+=r'''\paragraph{Integración externa requerida.} JP llevará a S7/T-15 las fichas 8.F.1 y las tablas 8.H.1--3: enlazar cada riesgo con sus paquetes existentes de migración/datos, implantación, integración, soporte, gobierno o salida, según evidencia de 8.A/8.D; registrar identificador de paquete real, capacidad existente y diferencia antes de abrir trabajo nuevo. Asignar A en el mes inicial indicado y antes del hito, nivelar el consumo contingente propuesto por mes/perfil y mantener las 3.072 HH protegidas sólo en E1. Reservar los cuatro sobres de gestión en mes 1, 13, 21 y 39 como capacidad de decisión, con consumo sujeto a incidente emergente, no como ejecución cierta. En la operación DAT/IMP conservan familia de esfuerzo y SRE asume responsabilidad desde 22; no duplicar familias ni cargar ambas personas por relevo. Recalcular precedencias, holguras y ruta crítica después de nivelar; conservar las cuatro semanas finales de evidencia y congelamientos. Si no cabe, elevar refuerzo o cambio antes del hito, sin moverlo unilateralmente.

Para flujo de caja, entregar por mes/perfil la misma diferencia aprobada multiplicada por su tarifa neta validada del modelo económico, sin precios en S8. No sumar gestión como costo consumido ni duplicar protección ya incluida; documentar su tratamiento como reserva y su activación. No se modifica E-21 ni se declara financiamiento aprobado. Estado: propuesta completa en S8; incorporación al cronograma, capacidad y flujo requiere integración externa. JP presenta la conciliación al arranque y la actualiza en cada comité quincenal y antes de H5/H10; el Comité Ejecutivo autoriza cambios y CAL comprueba no duplicación.
'''

# I: trazabilidad, equivalencias completas y sincronización.
it=r'''\clearpage
\section{Anexo 8.I: Observaciones, equivalencias e integración externa}
\label{sec:cierre-traza}
El correo principal, punto 1.b, pide una ``Tabla de trazabilidad observación--respuesta--sección modificada'' de las observaciones del Informe 2. Se aplica al alcance S8. Las citas textuales siguientes proceden de la revisión G02--LafroX, pp. 33--38; Bases Administrativas, apartado Subdocumento 8, p. impresa 58, confirma técnica, costo-beneficio y reservas. Correo principal prevalece sobre las Bases cuando las aclara; no contiene una nueva lista técnica particular de riesgos. Los estados distinguen cumplimiento documental en S8 de integración o ejecución externa. No se atribuye a una tabla prevista valor de prueba realizada.
'''
obs=[
('01','``Definir los factores decimales de impacto en el cuerpo, corregir el solape de bandas, renumerar tablas'' (p. 38).','Factores, bandas y umbrales únicos; escala de HH condicional y máximo de dimensiones.','8.1.3; tablas 8.2--8.4; 8.C.1.','corregido en S8'),
('02','``Para cada riesgo que depende del CLIENTE, nombrar la contraparte, qué se le pide y en qué fecha, y la contingencia si no responde'' (p. 37).','Se conservan 28 coordinaciones, plazos y escalamiento; la ficha agrega esfuerzo y plazo de contingencia.','8.A.2; 8.F.1; T-16.','corregido en S8'),
('03','``Retirar del registro los 13 riesgos internos del proveedor [...] y resolverlos en la propuesta'' (p. 37).','Treinta y cinco riesgos vigentes; 16 CI con solución y cierre propuestos, incluidos los trece observados. Incorporar en S4/S9/S13 y verificar; no se declara ejecutado.','8.E.1; equivalencias 8.I.2.','requiere integración externa'),
('04','``Declarar el riesgo residual de cada riesgo después de la respuesta'' (p. 37).','35 valoraciones posteriores proyectadas con probabilidad, impacto, zona, hipótesis y evidencia. Eficacia efectiva se verifica al ejecutar.','8.F.2; resumen posterior en T-16.','corregido en S8'),
('05','``ningún riesgo puede quedar en Alta o Crítica sin un plan adicional'' (p. 37).','Los que mantienen E alta/crítica reciben plan adicional, plazo, dueño y bloqueo; no se rebaja I sanitario o contractual sin fundamento.','8.F.1--2; 8.G.1.','corregido en S8'),
('06','``Agregar los riesgos del Cap. 19 que faltan [...] y los de obsolescencia, bloqueo por proveedor y escalabilidad'' (p. 37).','Se conservan omisiones incorporadas, sus fuentes y no duplicación. Escalabilidad y consistencia del diseño se resuelven como CI; cambios externos de soporte/salida siguen como riesgos.','8.D.3; 8.E.1; T-16; 8.I.2.','parcial'),
('07','``Llevar al registro los puntos únicos de falla y riesgos residuales del S4'' (p. 37).','ERP externo sigue en T-16; identidad y stock quedan como controles internos trazados, no se trasladan defectos al CLIENTE. Faltan evidencia y sincronización de S4/S9.','8.D.1--2; 8.E.1; 8.F.2.','requiere integración externa'),
('08','``Aplicar una técnica de las exigidas (FMEA, árbol de fallas o simulación) a los riesgos críticos y altos'' (p. 38).','FMEA de 15 modos, causas/efectos, S/O/D, NPR, controles, acciones y puntuación posterior proyectada.','8.G.1; síntesis 8.2.3.','corregido en S8'),
('09','``Hacer el costo-beneficio de cada respuesta de zona alta o crítica, con plazo, y justificar las de retorno menor que 1'' (p. 38).','Quince cálculos en HH, entradas A/C/p0/p1/H0, sensibilidad y justificación obligatoria; calendario en ficha.','8.F.1/8.F.3.','corregido en S8'),
('10','``ninguna acción tiene plazo ni fecha [...] ni esfuerzo, ni contingencia específica'' (p. 36).','Treinta y cinco fichas con perfiles, HH extra y actuación contingente temporizada; controles ordinarios permanecen en EDT.','8.F.1; 8.A.1--2.','corregido en S8'),
('11','``Derivar la reserva de gestión, conciliar contingencia y reserva protegida del S7, e incorporarlas al T-15 y al cronograma'' (p. 38).','Gestión propuesta derivada por escenario, conciliación sin doble conteo y distribución mensual/perfil; integración de cronograma/flujo pendiente.','8.H.1--3; 8.3.2.','requiere integración externa'),
('12','``El S13 dice que el Anexo 8.A asigna al piloto de R-034 [histórico] [...] meses 11 a 15'' (p. 36).','CI-034: paquete 11--15, certificación 11--12, piloto real 13--15; conservar indicador y actualizar referencia S13.','8.D.1/TR-01; 8.E.1.','requiere integración externa'),
('13','``Dos tablas distintas numeradas Tabla 8.4''; ``La Tabla 8.5 tiene siete columnas''; cita incorrecta RT-20.04/RT-20.02 (p. 37).','Numeración única, tablas de resumen de cinco columnas y referencias BTT cap. 20 corregidas. RBS conserva folios y firma.','8.1.3; 8.2; 8.3.3.','corregido en S8'),
('14','``quitar académico'' (p. 38).','No se aplica por instrucción expresa del autor de conservar las citas que contienen contenido academico; se registra la excepción, no se declara cumplido.','Tablas 8.2--8.4 y declaración de IA protegidas.','parcial')]
it+=table('8.I.1','Trazabilidad observación--respuesta--sección modificada. Fuente: correo principal 1.b y revisión Informe 2, pp. 33--38.','tab:cierre-observaciones','G{0.05} F{0.28} Y F{0.15} F{0.15}',['Obs.','Pedido original y fuente','Respuesta aplicada','Ubicación','Estado'],[list(x) for x in obs])
eq=[]
short={m[0]:m[1] for m in re.findall(r'\\RBSrisk\{(R-\d{3})\}\{([^\n]+?)\}\{[^}]+\}',rb)}
for i in range(1,52):
 oldid=f'R-{i:03}';eq.append(['Histórico '+oldid,mapping.get(oldid,oldid.replace('R-','CI-')),short.get(oldid,reg51[oldid][1]),'riesgo vigente' if oldid in mapping else 'control interno; 8.E.1'])
it+=table('8.I.2','Equivalencias completas: ID anterior histórico y destino vigente. Fuente: catálogo anterior de 51 eventos; nuevo T-16 de 35 riesgos.','tab:cierre-equivalencias','F{0.14} G{0.11} Y F{0.20}',['ID anterior','ID vigente / CI','Descripción','Estado'],eq)
it+=r'''\paragraph{Regla de identificación.} R-001 a R-035 son exclusivamente el catálogo vigente. Las columnas rotuladas ``Histórico'' contienen los ID anteriores y no deben usarse como claves de T-16. Un CI mantiene su sufijo histórico, sin ocupar un número R. Al sincronizar otros documentos se consulta esta tabla; no se realiza sustitución global de dígitos, porque un ID antiguo puede coincidir con otro vigente. Las citas originales de la revisión conservan su ID histórico rotulado, sin alterar el contenido citado. Los expedientes futuros usarán ID vigente y referencia histórica sólo en metadatos.

\paragraph{Cambios externos concretos.} En S4, enlazar CI-009/010 y CI-023--027 con integración, mapas y seguridad, y CI-047/048/050 con capacidad, identidad y reconciliación; incorporar soluciones y casos de 8.E, conservar las dependencias externas del nuevo T-16 mediante equivalencia. En S9/T-13, registrar casos, requisitos, versión y evidencia de esos controles, FMEA y bloqueo habilitante; la tabla prevista no equivale a ensayo ejecutado. En S13, convertir antiguos riesgos de diseño INN-01/02/03/05 en CI y criterios de validación; mantener CI-034 y su piloto 13--15 dentro del paquete 11--15, y enlazar liquidación variable con el riesgo vigente equivalente al histórico R-039. En S7/T-14/T-15, cargar la propuesta de 8.H sólo después de conciliar paquetes y capacidad y conservar protección E1; entregar el mismo calendario al modelo económico sin duplicar reserva. En S6 y matrices transversales, actualizar identificadores con 8.I.2 y responsables/decisiones. JP registra aceptación de cada sincronización; hasta editar y comprobar esos documentos el estado sigue siendo requiere integración externa.
'''
# Renumerar todos los documentos existentes; preservar líneas protegidas byte por byte.
b,rb,a,f=map(rename,[b,rb,a,f])
# Eliminar bloques narrativos anteriores que contradicen resultados completos.
start=b.index('\\textbf{Separación del seguimiento interno.}')
end=b.index('\\subsection{Análisis cualitativo de riesgos}',start)
b=b[:start]+r'''\textbf{Seguimiento interno y equivalencia.} Los trece asuntos de diseño observados y los tres reclasificados se siguen como CI en 8.E, fuera de T-16. El registro vigente usa R-001--R-035 sin saltos; 8.I.2 relaciona los 51 ID anteriores con los 35 actuales o sus CI. La numeración antigua sólo aparece rotulada como histórica. Las brechas B-S4-01/03 conservan CI-048/050; B-S4-02 y B-S7-01 remiten a los riesgos vigentes de ERP y rotación mediante 8.I.2. CI-034 conserva paquete 11--15, H5 en 11--12 y piloto real 13--15, con I-01A de al menos 70\% y al menos 100 avisos evaluables en mes 15. La solución y evidencia propuesta de cada CI está en 8.E; su incorporación en S4/S9/S13 se solicita en 8.I y no se declara ejecutada.

'''+b[end:]
b=b.replace('conservando sus ID originales','con identificadores vigentes consecutivos').replace('con ID originales discontinuos','con ID vigentes consecutivos').replace('conserva los ID originales con discontinuidades','usa ID vigentes consecutivos').replace('conservando sus ID discontinuos','con ID vigentes consecutivos')
b=b.replace('La evaluación residual de los riesgos vigentes corresponde a la siguiente tarea de respuestas.', 'La valoración posterior proyectada y el plan adicional se presentan en 8.F; FMEA aplicado a los 15 riesgos altos/críticos iniciales se desarrolla en 8.G.')
# Reemplazar 8.3.1 y 8.3.2 completas por síntesis de cálculos y resultados, conservando sección de aceptación.
st=b.index('\\subsection{Respuestas y costo-beneficio técnico}');en=b.index('\\subsection{Factibilidad y aceptación}',st)
reszones=Counter(x['zone'] for x in data.values());highpost=[k for k,x in data.items() if D(x['E'])>=D('.20')]
b=b[:st]+r'''\subsection{Respuestas y costo-beneficio técnico}
Las 35 fichas de la Tabla 8.F.1 concretan acción preventiva, disparador de 8.A, dueño/apoyo, esfuerzo A/C, plazo preventivo y contingencia temporizada. Las 28 coordinaciones del CLIENTE siguen en 8.A.2. Los controles ordinarios de diseño, formación y soporte conservan su presupuesto en S7; A sólo estima coordinación extraordinaria y cierre de excepción, y C particiona el PERT inicial, sin sumarlo otra vez.

La Tabla 8.F.3 calcula costo-beneficio en HH de las 15 respuestas altas/críticas: B=p0H0-p1(H0-C), T=A+p1C y B/T. El saldo neto B-T evita duplicación entre atención del evento y respuesta. Se muestra el escenario sin mejora p1=p0, umbral de equilibrio y justificación de cada tratamiento; las obligaciones sanitarias, de aceptación o continuidad no se descartan por retorno HH menor que uno. No se introducen precios ni valorización monetaria en S8.

La Tabla 8.F.2 asigna a los 35 riesgos p1, I1, E1, zona y evidencia requerida. Se conserva el impacto inicial; no se borra una consecuencia sanitaria o contractual mediante mejor detección. Son proyecciones de planificación condicionadas a la acción y su prueba; no se presentan controles previstos como eficaces ya comprobados. Si no se acredita la hipótesis, permanece la valoración inicial y se escala antes del hito.

'''+f'La proyección contiene {reszones["Crítica"]} riesgo crítico, {reszones["Alta"]} altos, {reszones["Media"]} medios y {reszones["Baja"]} bajos. '+', '.join(highpost)+r''' mantienen zona alta/crítica: cada uno tiene plan adicional en 8.F.1, plazo de intervención y bloqueo de habilitación/aceptación sin evidencia. CAL verifica, JP escala y la autoridad del CLIENTE decide sus dependencias; ninguna aceptación de riesgo dispensa un requisito obligatorio.

\subsection{Reservas y cronograma}
'''+f'La exposición inicial sigue en 1.183,11 HH. Las fichas proponen {pretty(prevent)} HH preventivas planificadas y {pretty(event)} HH de contingencia específica p1H0; dentro de esta última, {pretty(cbtotal-prevent)} HH son respuesta p1C y {pretty(ressum)} HH remanente p1L. La suma posterior A+p1H0 es {pretty(totalafter)} HH, no se añade a las 1.183,11 HH iniciales. Los cálculos se realizan sin redondear; los totales impresos se redondean a dos decimales.\n\n'+r'''La Tabla 8.H.1 concilia las 411,82 HH históricas internas excluidas, las 3.072 HH ya protegidas en S7 sólo para E1 y la nueva propuesta. La cifra anterior de gestión de 1.600 HH carecía de base; se reemplaza por una propuesta derivada de 160 HH (cuatro ciclos emergentes, JP 8+ARQ 16+CAL 8+SRE 8 por ciclo), con límites, exclusiones y sensibilidad de 8.H. No se declara aprobada, financiada ni incorporada a T-15.

Las Tablas 8.H.2--3 distribuyen prevención y contingencia por mes y perfil. La gestión se reserva como sobre de decisión en los bloques 1--12, 13--20, 21--38 y 39--56; no es trabajo consumido. El crédito demostrado contra las 3.072 HH es inicialmente cero hasta conciliar paquete, perfil y mes; no se suma esa protección otra vez al total de S7 ni se usa en E2. La propuesta debe nivelarse y cargarse en T-15 y en el flujo económico con la misma correspondencia mensual, sin convertir HH directamente en días ni prestar las cuatro semanas finales de evidencia. La integración externa de cronograma, capacidad y flujo permanece pendiente y se identifica en 8.I.1.

'''+b[en:]
# Agregar síntesis FMEA al análisis cuantitativo, antes de sección 8.3.
anchor='\\section{Plan de Acción a Riesgos}'
b=b.replace(anchor,r'''\paragraph{Análisis de modos de falla.} El Anexo 8.G aplica FMEA a los 15 riesgos de zona Alta o Crítica inicial. Para cada modo se documentan efecto, disparador, severidad S, ocurrencia O, dificultad de detección D, NPR=S por O por D, control, acción y evaluación posterior proyectada. S sigue el impacto, O las bandas de p0/p1 y D una escala específica de detectabilidad antes del efecto. NPR no equivale a exposición ni a HH; un modo de severidad sanitaria 5 exige acción aun con NPR bajo. CAL verifica evidencias y conserva pruebas/defectos; el análisis no se presenta como simulación ni como resultado observado.

'''+anchor)
# Actualizar anexo existente y remisiones sin recuperar reservas/CI históricos como riesgos activos.
for name in ['a','f']:
 s=locals()[name]
 s=s.replace('con sus ID originales discontinuos','con ID vigentes consecutivos').replace('conservando sus ID discontinuos','con ID vigentes consecutivos').replace('conserva los ID originales con discontinuidades','usa ID vigentes consecutivos')
 s=s.replace('La estimación del esfuerzo y la evaluación residual corresponden al desarrollo de los tratamientos.', 'La estimación de esfuerzo por perfil, los plazos completos y la valoración residual proyectada están en 8.F.1--2; el costo-beneficio de las respuestas altas/críticas, en 8.F.3.')
 s=s.replace('Los ID retirados no se reutilizan ni se renumeran.', 'La equivalencia histórica completa está en 8.I.2; los CI conservan sus sufijos. Los ID R vigentes se renumeran consecutivamente.')
 s=s.replace('No se establece aquí una reserva cuantitativa.', 'La propuesta de reservas y su integración externa pendiente se detallan en 8.H; las valoraciones posteriores de los 35 riesgos están en el resumen T-16.2 y en 8.F.2.')
 s=s.replace('las valoraciones de impacto.', 'las valoraciones de impacto inicial.')
 locals()[name]=s
# Añadir remisión ejecutable en cada fila de respuestas y T16; no altera p0/OMP iniciales.
for sname in ['a','f']:
 s=locals()[sname];lines=s.splitlines()
 for j,l in enumerate(lines):
  if re.match(r'R-\d{3} &',l):
   cells=l.split(' & ')
   if sname=='f' and len(cells)==8:cells[6]+=' Plazos, HH y contingencia: 8.F.1; residual proyectado: 8.F.2.'
   elif sname=='a' and len(cells)==4:cells[2]+=' Plazos completos y HH: 8.F.1; residual: 8.F.2.'
   lines[j]=' & '.join(cells)
 locals()[sname]='\n'.join(lines)+'\n'
a=a.replace('Anexos 8.A--8.D','Anexos 8.A--8.I').replace('Anexos 8.A, 8.B, 8.C y 8.D','Anexos 8.A--8.I')
a=a.replace('respuestas propuestas no se consideran eficaces ni modifican $p_0$ en este cálculo.', 'respuestas no modifican la estimación inicial $p_0$ de esta tabla; la proyección posterior se calcula por separado en 8.F.')
a=a.replace('S13 mantiene', 'S13 de consulta mantiene')
# Reescribir TR02 para no conservar actualizaciones numéricas de CI como si fueran riesgos vigentes.
ls=a.splitlines()
for j,l in enumerate(ls):
 if l.startswith('TR-02 &'):ls[j]=r'TR-02 & S13, 13.1.7--13.5.7; equivalencias 8.I.2 y controles 8.E.1. & CI-034--038 y CI-040 son controles internos; la liquidación contractual permanece como '+mapping['R-039']+r' vigente. & ID y puntuaciones antiguos de S13 deben sincronizarse con el nuevo catálogo; no son valores vigentes. & JP solicita cambiar referencias usando 8.I.2, conservar indicadores/condiciones de CI y enlazar el residual del riesgo contractual en 8.F.2. Requiere integración externa. \\'
a='\n'.join(ls)+'\n'
# Fragmentos nuevos y resumen posterior en T-16 (se conserva su tabla inicial de ocho columnas).
inputs='\n'.join(r'\input{08_plan_riesgos/'+x+'}' for x in ['anexo-e-controles.tex','anexo-f-respuestas.tex','anexo-g-fmea.tex','anexo-h-reservas.tex','anexo-i-trazabilidad.tex'])
a=a.replace('\\section*{Referencias}',inputs+'\n\n\\section*{Referencias}',1)
fpost=table('T-16.2','Resumen de valoración posterior proyectada; no eficacia observada. Fuente: Anexo 8.F.2, hipótesis condicionadas a evidencia.','tab:t16-residual','G{0.08} G{0.11} G{0.11} G{0.13} F{0.14} Y',['ID vigente','p1','I1 / factor','E1 / zona','Dueño','Evidencia y tratamiento'],[[k,fmt(D(x['pr']))+r'\%',f'{x["I"]} / {fmt(D(x["qi"]))}',fmt(D(x['E']))+' / '+x['zone'],x['owner'],'Evidencia y revisión: 8.F.2; ficha ejecutable y plan adicional cuando E1 es alta/crítica: 8.F.1.'] for k,x in data.items()])
f=f.replace('\\section*{Referencias}',fpost+'\n\\section*{Referencias}',1)
# Textos que aún remiten a un desarrollo futuro quedan sustituidos por resultados identificables.
b=b.replace('su valoración no acredita por sí sola continuidad completa.', 'la prueba habilitante y su plan contingente se registran en 8.F.1--2; no se presume ensayo ejecutado.')
for p,s in zip(files,[b,rb,a,f]):
 assert [l for l in base[p].splitlines() if 'contenido academico' in l]==[l for l in s.splitlines() if 'contenido academico' in l],p
 (r/p).write_text(s,encoding='utf-8')
for p,s in [('anexo-e-controles.tex',e),('anexo-f-respuestas.tex',ft),('anexo-g-fmea.tex',g),('anexo-h-reservas.tex',htext),('anexo-i-trazabilidad.tex',it)]:
 (r/'08_plan_riesgos'/p).write_text(s,encoding='utf-8')
(r/'tmp/cierre-s8-datos.json').write_text(json.dumps({'mapping':mapping,'internal':sorted(ciids),'risks':data,'prevent':str(prevent),'event':str(event),'residual':str(ressum),'treatment':str(cbtotal),'totalafter':str(totalafter),'reszones':dict(reszones)},ensure_ascii=False,indent=2),encoding='utf-8')
print('Renumerados',len(data),'FMEA',len(gl),'posteriores',dict(reszones),'A',fmt(prevent),'contingencia',fmt(event),'residual',fmt(ressum),'tratamiento',fmt(cbtotal),'total',fmt(totalafter))
