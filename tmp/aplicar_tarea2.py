from pathlib import Path
from decimal import Decimal as D
import re, json, hashlib

root = Path(__file__).resolve().parents[1]
body = root/'08_plan_riesgos/contenido.tex'
ann = root/'LAFROX-Subdocumento8-Anexos.tex'
form = root/'LAFROX-Formulario-T-16.tex'
rbs = root/'08_plan_riesgos/figuras/rbs.tex'
texts = {p: p.read_text(encoding='utf-8') for p in [body,ann,form,rbs]}
# Dimensión no HH y nivel: juicio de planificación sobre el evento declarado,
# sin descontar eficacia futura de las respuestas.
judgments = {
1:(4,'Aceptación','La certificación EDI incompleta amenaza la evidencia de E2 y sus cuatro semanas finales; la carga manual no acredita ese alcance.'),
2:(5,'Calidad sanitaria','Los vínculos sanitarios sin evidencia de origen pueden ser irrecuperables; el saneamiento no reconstruye una historia que no existe.'),
3:(3,'Alcance','El historial incompleto exige reproceso de la carga y excepciones de reposición; el evento declarado no demuestra pérdida definitiva del alcance.'),
4:(4,'Aceptación','Las diferencias sin explicación ni ajuste aprobado bloquean la aceptación de inventario antes del corte, condición de marcha blanca del art. 17.3.'),
5:(4,'Aceptación','Sin saldo inicial conciliado no puede demostrarse M8 con carga aceptada; requiere resolver la evidencia de aceptación de los arts. 18.1--18.2.'),
6:(4,'Aceptación','La ausencia de antecedentes verificables impide respaldar las comparaciones de OTIF o cuadratura exigidas para aceptar el período de referencia.'),
7:(3,'Alcance','La deuda viva adicional obliga a extraer y conciliar nuevamente el entregable; no se declara pérdida de datos ni incumplimiento definitivo.'),
8:(3,'Plazo','El cierre tributario queda pendiente de confirmación externa y requiere seguimiento y conciliación del entregable; el silencio no acredita aprobación.'),
9:(3,'Calidad','El resultado incierto del pago exige investigación y conciliación antes de cerrar la operación; no se afirma un cargo duplicado consumado.'),
10:(4,'Servicio','La caída puede interrumpir la planificación de rutas durante operación y amenaza el servicio; la continuidad propuesta no se descuenta como eficacia probada.'),
11:(4,'Aceptación sanitaria','La falta de aprobación bloquea la certificación térmica y el cierre de marcha blanca; el evento es aprobación pendiente, sin afirmar daño sanitario consumado.'),
12:(4,'Plazo','La falta de equipos bloquea instalación y pruebas de una ola y amenaza su aceptación y secuencia de implantación.'),
13:(4,'Alcance','Sin acuerdo no se acredita la cobertura del transportista ni sus pruebas de la ola, por lo que se amenaza la aceptación del alcance comprometido.'),
14:(4,'Aceptación sanitaria','La negativa impide integrar el termógrafo y acreditar temperatura de la ruta; amenaza la aceptación sin demostrar por sí sola daño sanitario grave.'),
15:(4,'Aceptación','El registro exclusivo fuera de la solución impide acreditar adopción y puede extender el cierre de la ola y su marcha blanca.'),
16:(3,'Alcance','La indisponibilidad obliga a reconstruir y validar reglas con el ayudante y antecedentes; el evento no establece pérdida irrecuperable ni atraso contractual probado.'),
17:(4,'Aceptación','Usuarios sin evaluación completa no acreditan capacitación y certificación, condición acumulativa de cierre de marcha blanca del art. 17.3.'),
18:(4,'Plazo','La decisión pendiente bloquea tareas de diseño, prueba o aceptación y consume holgura, amenazando hitos que requieren decisión coordinada.'),
19:(4,'Servicio','La interrupción limita servicios centrales y acumula sincronización; amenaza continuidad y niveles de servicio, sin suponer eficacia del respaldo.'),
20:(4,'Servicio','Superar la autonomía deja componentes sin servicio hasta restituir energía; amenaza continuidad sin imputar pérdidas ajenas al proyecto.'),
21:(4,'Aceptación','Sin aprobación de residencia no puede habilitarse ni acreditarse la recuperación propuesta; requiere decisión antes de aceptar los entornos.'),
22:(4,'Contrato','La autorización pendiente enfrenta congelamiento y plazo de remediación, amenazando cumplimiento; no demuestra por sí sola pérdida de continuidad contractual.'),
23:(4,'Seguridad y servicio','La autenticación como tercero puede alterar la atribución de operaciones y exige contención; amenaza integridad y aceptación, sin afirmar pérdida irrecuperable.'),
24:(4,'Calidad','Aceptar un mensaje falso o alterado puede modificar pedidos o avisos; amenaza integridad del intercambio EDI y su aceptación.'),
25:(4,'Seguridad','La pérdida de custodia expone datos y accesos del terminal y exige contención; amenaza seguridad del servicio sin afirmar daño irreversible.'),
26:(4,'Servicio','Las ráfagas impiden accesos legítimos y amenazan disponibilidad y tiempos de respuesta del servicio.'),
27:(5,'Trazabilidad y contrato','El acceso privilegiado permite borrar o alterar respaldos y evidencia; la pérdida irrecuperable potencial compromete trazabilidad y recuperación obligatorias.'),
28:(2,'Plazo','El efecto declarado se limita a repetir casos de un recorrido dentro del paquete de validación; no se establece afectación de un hito contractual.'),
29:(2,'Plazo','Se evalúa la repetición de casos de prueba interrumpidos; las consecuencias personales del siniestro se atienden por el procedimiento del transportista y no son HH del proyecto.'),
30:(2,'Plazo','El efecto del proyecto es reprogramar y repetir el recorrido de validación; la valoración no incluye pérdidas de vehículo o carga.'),
31:(3,'Alcance','El reemplazo requiere habilitación, formación extraordinaria y verificación de registros del entregable de implantación.'),
32:(3,'Contrato','El efecto estimado es evaluar y tramitar la solicitud; el desarrollo adicional sólo existe tras aprobación y ajuste de línea base.'),
33:(4,'Contrato','Una exigencia aplicable obliga a adecuar y validar controles de la solución; amenaza cumplimiento y requiere decisión contractual, sin presumir una reforma o multa concreta.'),
34:(4,'Aceptación','No alcanzar I-01A impide liberar la innovación ofertada; amenaza aceptación de esa función, aunque no suprima el servicio base.'),
35:(4,'Aceptación','No alcanzar I-02A amenaza el beneficio e indicador de aceptación de la innovación ofertada y exige revisar su liberación.'),
36:(4,'Seguridad y aceptación','La exposición de datos personales incumple el propósito de sanitización y obliga a suspender paquetes; amenaza seguridad y aceptación (RT-26.07), sin presumir terminación contractual.'),
37:(5,'Calidad sanitaria','Las sugerencias erróneas para refrigerados o congelados pueden inducir una salida sanitaria insegura si se interpreta la estimación como permiso para relajar RNG-04.'),
38:(5,'Calidad sanitaria','Una asociación lote--sensor errónea produce historia térmica falsa y estimaciones sin fundamento, con potencial consecuencia sanitaria grave.'),
39:(3,'Contrato','La discrepancia afecta el cálculo y la liquidación de un período del tramo variable; el evento no establece interrupción ni terminación contractual.'),
40:(4,'Seguridad y aceptación','La inferencia de cifras de terceros amenaza confidencialidad y el incumplimiento de I-05B amenaza aceptación de la hoja; se toma la mayor consecuencia del evento compuesto.'),
}

def num(s): return D(s.replace(',','.'))
def fmt(v): return f'{v:.2f}'.replace('.',',')
def plevel(p): return next((i for i,t in enumerate([10,30,50,70,100],1) if p<=t))
def hlevel(h): return next((i for i,t in enumerate([24,80,160,320,D('Infinity')],1) if h<=t))
def zone(e): return 'Baja' if e<D('.08') else 'Media' if e<D('.20') else 'Alta' if e<D('.40') else 'Crítica'
pf={i:D(v) for i,v in enumerate(['.10','.30','.50','.70','.90'],1)}
im={i:D(v) for i,v in enumerate(['.05','.10','.20','.40','.80'],1)}
rows={}
for line in texts[ann].splitlines():
 if re.match(r'R-\d{3} &',line) and r'\%' in line:
  c=line.split(' & '); rid=c[0]; rows[rid]={'p0':int(c[1].split('\\')[0]),'h':num(c[6])}
assert len(rows)==40
changes=[]
newlines=[]
for line in texts[form].splitlines():
 if re.match(r'R-\d{3} &',line):
  c=line.split(' & '); rid=c[0]; d=rows[rid]; n=int(rid[2:]); dh,dim,why=judgments[n]
  d.update(ph=plevel(d['p0']),ih=hlevel(d['h']),dim=dim,dh=dh,why=why)
  d['impact']=max(d['ih'],dh); d['qp']=pf[d['ph']]; d['qi']=im[d['impact']]; d['e']=d['qp']*d['qi']; d['zone']=zone(d['e'])
  d['old_i']=c[4]; d['old_e']=c[5]
  c[3]=f"{d['ph']} / {fmt(d['qp'])}"; c[4]=f"{d['impact']} / {fmt(d['qi'])}"; c[5]=f"{fmt(d['e'])} ({d['zone']})"
  if c[4]!=d['old_i'] or c[5]!=d['old_e']: changes.append(rid)
  if n==11: c[6]=c[6].replace('La zona crítica depende de una aprobación que solo puede emitir Calidad.','La zona alta corresponde al bloqueo de aceptación por una aprobación que solo puede emitir Calidad.')
  if n==17: c[6]=c[6].replace('Aceptar pasivamente. Respetar la zona baja asignada por el equipo y observar asistencia y certificaciones con los controles existentes.','Escalar. Elevar a la Contraparte Técnica la disponibilidad de usuarios requerida para cumplir la certificación de la ola y observar asistencia y evaluaciones.')
  if n==24: c[6]=c[6].replace('Se acepta la exposición residual de zona baja;','La zona baja corresponde a la valoración inicial;')
  line=' & '.join(c)
 newlines.append(line)
newform='\n'.join(newlines)+'\n'
newform=newform.replace('Exposición y zona reproducen los valores del análisis cualitativo, no una estimación monetaria.',r'El nivel de probabilidad se deriva de $p_0$ del Anexo 8.B mediante las bandas de la Tabla 8.2; su factor es una ponderación de categoría. El impacto es el mayor nivel por esfuerzo condicional, plazo, alcance, calidad sanitaria o consecuencias contractuales (Tabla 8.3 y respaldo por ID en el Anexo 8.C). Exposición es $q_P\times q_I$ y la zona resulta de los umbrales de la Tabla 8.4.').replace('La columna Mitigación conserva la columna del Formulario T-16 y presenta el disparador observable, la controlabilidad y la detectabilidad del CSV; no representa una acción de mitigación.','La columna Mitigación presenta la estrategia y la respuesta propuesta; el disparador observable se detalla en el Anexo 8.A.')

b=texts[body]
start=b.index('Para analizar los riesgos, se definen')
end=b.index('\\subsection{Registro y cierre}', start)
old=b[start:end]
# Preserve the exact source captions requested by the user.
captions=re.findall(r'\\begin\{tablalafrox\}\{([^\n]+?)\}\{(tab:tabla-[^}]+)\}',old)
caps={label:caption for caption,label in captions}
scales=r'''La probabilidad inicial $p_0$ estima la ocurrencia de al menos un episodio en la ventana de exposición de cada riesgo, tanto para el análisis cualitativo como para el cuantitativo. El nivel P se obtiene de esa misma estimación con las bandas de la Tabla 8.2. Su factor $q_P$ representa la categoría para priorizar; no constituye una segunda probabilidad del evento. Por ejemplo, R-002 tiene $p_0=60\%$, nivel 4 y factor 0,70; R-016 tiene $p_0=20\%$, nivel 2 y factor 0,30; R-036 tiene $p_0=35\%$, nivel 3 y factor 0,50. Para calcular las HH esperadas se utiliza $p_0$, conservando la misma ventana y el supuesto de episodios del Anexo 8.B.

\begin{tablalafrox}{PROBCAP}{tab:tabla-probabilidad}
{G{0.08} F{0.27} Y G{0.15}}
{\cab{Nivel P} & \cab{Banda de $p_0$} & \cab{Descripción} & \cab{Factor $q_P$}}
1 & $0\%\leq p_0\leq10\%$ & Muy baja & 0,10 \\
2 & $10\%<p_0\leq30\%$ & Baja & 0,30 \\
3 & $30\%<p_0\leq50\%$ & Media & 0,50 \\
4 & $50\%<p_0\leq70\%$ & Alta & 0,70 \\
5 & $70\%<p_0\leq100\%$ & Muy alta & 0,90 \\
\end{tablalafrox}

El impacto I representa la afectación que tendría el evento si se materializa, antes de descontar la eficacia de las respuestas propuestas. Se evalúan por separado esfuerzo, plazo, alcance, calidad sanitaria y consecuencias contractuales; se adopta el mayor nivel aplicable, sin promediar dimensiones. Las HH se clasifican por el PERT condicional acumulado del Anexo 8.B, no por su valor esperado. La Tabla 8.3 define los criterios propios de planificación; el Anexo 8.C documenta su aplicación a los 40 riesgos. Una amenaza a aceptación o servicio es nivel 4; el nivel 5 requiere la consecuencia grave indicada, no una aprobación simplemente pendiente.

\begin{tablalafrox}{IMPCAP}{tab:tabla-impacto}
{G{0.07} G{0.12} F{0.19} Y}
{\cab{Nivel I} & \cab{Factor $q_I$} & \cab{PERT condicional (HH)} & \cab{Plazo, alcance, calidad o contrato}}
1 & 0,05 & $H\leq24$ & Corrección localizada dentro de la tarea, sin afectar aceptación. \\
2 & 0,10 & $24<H\leq80$ & Repetición o ajuste dentro del paquete, sin desplazar hitos. \\
3 & 0,20 & $80<H\leq160$ & Reprogramación interna o reproceso de entregable, conservando requisitos e hitos contractuales. \\
4 & 0,40 & $160<H\leq320$ & Amenaza a un hito contractual, aceptación o nivel de servicio; exige decisión y recuperación coordinadas. \\
5 & 0,80 & $H>320$ & Consecuencia sanitaria grave, pérdida irrecuperable de trazabilidad o incumplimiento que compromete el alcance obligatorio o la continuidad contractual. \\
\end{tablalafrox}

Las condiciones de aceptación de los arts. 17.3 y 18.1--18.3, y los compromisos de continuidad descritos en 8.3.3, permiten reconocer amenazas contractuales. La gravedad se valora por la consecuencia del evento documentado, sin presumir multas concretas, terminación contractual ni daños no descritos. Las HH no se convierten directamente en días; el efecto calendario depende de secuencia, perfiles y holguras.

La exposición es $E=q_P\times q_I$. Las bandas, factores y umbrales son definiciones propias del proyecto, no valores prescritos por Project Management Institute (PMI, 2017, cap. 11, §11.3, Tabla 11-1, p. 407). El producto es un índice de priorización; no representa una probabilidad, un importe ni HH esperadas.

\begin{tablalafrox}{EXPCAP}{tab:tabla-exposicion}
{F{0.40} F{0.20}}
{\cab{Exposición decimal} & \cab{Zona de prioridad}}
$E<0.08$ & Baja \\
$0.08\leq E<0.20$ & Media \\
$0.20\leq E<0.40$ & Alta \\
$E\geq0.40$ & Crítica \\
\end{tablalafrox}

La zona se calcula obligatoriamente con estos umbrales: los límites 0,08, 0,20 y 0,40 pertenecen, respectivamente, a Media, Alta y Crítica. Se conservan nivel y factor para hacer trazable el cálculo. La Tabla 8.5 y la RBS reflejan las zonas calculadas del T-16.

'''
for key,label in [('PROBCAP','tab:tabla-probabilidad'),('IMPCAP','tab:tabla-impacto'),('EXPCAP','tab:tabla-exposicion')]: scales=scales.replace(key,caps[label])
b=b[:start]+scales+b[end:]
b=b.replace('La probabilidad porcentual estimada para el análisis cuantitativo ($p_0$) se mantiene separada de $q_P$, como establece el procedimiento.', 'El nivel de probabilidad y su factor se derivan de la misma estimación $p_0$ utilizada en el análisis cuantitativo, conforme a la Tabla 8.2.').replace('La zona se transcribe del análisis cualitativo;','La zona se calcula con los umbrales de la Tabla 8.4;')
top=sorted(rows,key=lambda k:(-rows[k]['e'],k))[:10]
st=b.index('R-002 & 0,70', b.index('\\subsection{Análisis cualitativo de riesgos}')); en=b.index('\\end{tablalafrox}',st)
b=b[:st]+''.join(f"{rid} & {fmt(rows[rid]['qp'])} & {fmt(rows[rid]['qi'])} & {fmt(rows[rid]['e'])} & {rows[rid]['zone']} \\\\\n" for rid in top)+b[en:]
st=b.index('R-002, R-037 y R-038 encabezan'); en=b.index('\\subsection{Análisis cuantitativo}',st)
from collections import Counter
counts=Counter(d['zone'] for d in rows.values())
b=b[:st]+f"R-002, R-037 y R-038 encabezan la selección con exposición 0,56 y zona Crítica. El registro revisado contiene {counts['Crítica']} riesgos críticos, {counts['Alta']} altos, {counts['Media']} medios y {counts['Baja']} bajos. Los restantes riesgos seleccionados tienen exposición 0,28; los empates se resuelven por ID ascendente. El respaldo del impacto por ID está en el Anexo 8.C. La priorización conserva los 40 eventos y no descuenta eficacia de respuestas futuras. Los indicadores de validación de las innovaciones siguen siendo condiciones de habilitación (Subdocumento 13, secciones 13.2.7 y 13.3.7).\n\n"+b[en:]
# Correct the displayed conditional PERT values to the unchanged source in 8.B.
st=b.index('\\begin{tablalafrox}{Diez mayores valores esperados'); en=b.index('\\end{tablalafrox}',st)
part=b[st:en]
part=re.sub(r'^(R-\d{3} & .*? & \d+\\% & )[^&]+( & .*?)$', lambda m:m[1]+fmt(rows[m[1][:5]]['h'])+m[2],part,flags=re.M)
b=b[:st]+part+b[en:]
b=b.replace('C.5 sólo compara hipótesis. ', '')
b=b.replace('Anexo 8.B, que presenta las estimaciones de esfuerzo y sus valores esperados.', 'Anexo 8.B, que presenta las estimaciones de esfuerzo y sus valores esperados, y el Anexo 8.C, que justifica las valoraciones de impacto.')

nrbs=texts[rbs]
for rid,d in rows.items(): nrbs=re.sub(r'(\\RBSrisk\{'+rid+r'\}\{[^\n]+\})\{[^}]+\}',lambda m:m[1]+'{'+d['zone']+'}',nrbs)

a=texts[ann].replace('Anexos 8.A--8.B','Anexos 8.A--8.C').replace('Anexos 8.A y 8.B','Anexos 8.A, 8.B y 8.C')
support=r'''
\clearpage
\section{Anexo 8.C: Respaldo de la valoración inicial}

Se aplican las escalas de 8.1.3 a los mismos 40 eventos del T-16. $I_{HH}$ es el nivel de esfuerzo del PERT condicional acumulado del Anexo 8.B; $I_D$ es el mayor nivel de las dimensiones no HH identificadas en la justificación; $I=\max(I_{HH},I_D)$. La justificación señala la dimensión determinante y distingue una amenaza a aceptación (nivel 4) de una consecuencia grave (nivel 5). Son juicios iniciales de planificación sobre el evento declarado, sin descuento por eficacia futura ni cálculo de riesgo residual. La probabilidad se deriva de $p_0$ del Anexo 8.B; no se modifica ninguna estimación de ese anexo. Las referencias contractuales corresponden a las disposiciones ya descritas en 8.3.3; no se estiman multas ni importes.

\begingroup
\renewcommand{\thetable}{8.C.1}
\begin{tablalafrox}{Fundamento del impacto inicial de los 40 riesgos. Fuente: eventos del T-16, PERT del Anexo 8.B y escalas de 8.1.3.}{tab:sd8-impactos-respaldo}{G{0.08} G{0.17} G{0.12} G{0.12} Y}{\cab{ID} & \cab{PERT HH / $I_{HH}$} & \cab{$I_D$ / I} & \cab{$q_I$} & \cab{Dimensión y fundamento}}
'''
for rid,d in rows.items(): support+=f"{rid} & {fmt(d['h'])} / {d['ih']} & {d['dh']} / {d['impact']} & {fmt(d['qi'])} & {d['dim']}: {d['why']} \\\\\n"
support+='\\end{tablalafrox}\n\\endgroup\n\n'
a=a.replace('\\section*{Referencias}',support+'\\section*{Referencias}',1)

snapshot={'quantitative_rows':[l for l in texts[ann].splitlines() if re.match(r'R-\d{3} &',l) and r'\%' in l], 'protected':{str(p.relative_to(root)):[l for l in s.splitlines() if 'contenido academico' in l] for p,s in texts.items()},'changes':changes}
for p,s in [(body,b),(ann,a),(form,newform),(rbs,nrbs)]: p.write_text(s,encoding='utf-8')
(root/'tmp/tarea2-baseline.json').write_text(json.dumps(snapshot,ensure_ascii=False,indent=2),encoding='utf-8')
note=['# Tarea 2: escalas y valoraciones iniciales','', 'Aplicada solamente al subdocumento 8, anexos y T-16. Tareas 3–9 pendientes.','', '## Reglas', '', 'p0 del Anexo 8.B es la base única. Bandas: [0,10], (10,30], (30,50], (50,70], (70,100] %. Factores P: 0,10/0,30/0,50/0,70/0,90. Factores I: 0,05/0,10/0,20/0,40/0,80. Impacto máximo entre dimensiones; respaldo en Anexo 8.C.', '', '## Cambios para sincronización posterior', '', '| ID | Impacto anterior | Impacto nuevo | Exposición y zona anteriores | Exposición y zona nuevas |','|---|---|---|---|---|']
for rid in changes:
 d=rows[rid];note.append(f"| {rid} | {d['old_i']} | {d['impact']} / {fmt(d['qi'])} | {d['old_e']} | {fmt(d['e'])} ({d['zone']}) |")
note+=['','## Uso al terminar las tareas', '', 'S13: sincronizar las valoraciones de R-034–R-040 y referencias al respaldo; conservar IDs hasta resolver la reubicación de internos en tarea 6. S4/S7: contrastar referencias a niveles de riesgo, sin alterar arquitectura ni cronograma en esta tarea. El prompt final deberá consolidar estas variaciones con las tareas restantes; este registro no sustituye ese prompt.', '', 'p0, O/M/P, episodios, PERT, VE y reservas no se modificaron. En la Tabla 8.6 del cuerpo se corrigió la visualización de PERT que antes mostraba M, para reproducir el Anexo 8.B sin alterar sus cálculos.', '',f"Resultado: {dict(counts)}. Las estrategias se desarrollarán en tarea 7; R-017 se escala por el bloqueo de certificación ahora valorado como Media. Otros subdocumentos no editados."]
(root/'odd/tasks/tarea-2-escalas-y-sincronizacion.md').write_text('\n'.join(note)+'\n',encoding='utf-8')
print('Cambios:',changes); print('Zonas:',dict(counts)); print('Top 10:',top)
