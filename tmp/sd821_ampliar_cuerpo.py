from pathlib import Path
import subprocess,json,hashlib,re

r=Path(__file__).resolve().parents[1]
p=r/'08_plan_riesgos/contenido.tex';raw=p.read_bytes();s=raw.decode('utf-8').replace('\r\n','\n')
assert subprocess.check_output(['git','branch','--show-current'],cwd=r,text=True).strip()=='Lafrox_Subdocumento_8_Latex_Revision'
out=r/'tmp/sd821';out.mkdir(exist_ok=True)
assert not (out/'contenido-antes.tex').exists(),'Aplicación única'
(out/'contenido-antes.tex').write_bytes(raw)
manifest={name:hashlib.sha256((r/name).read_bytes()).hexdigest() for name in [
 'LAFROX-Subdocumento8-Anexos.tex','LAFROX-Subdocumento8-Anexos.pdf','LAFROX-Formulario-T-16.tex','LAFROX-Formulario-T-16.pdf',
 '08_plan_riesgos/anexo-e-controles.tex','08_plan_riesgos/anexo-f-respuestas.tex','08_plan_riesgos/anexo-g-fmea.tex','08_plan_riesgos/anexo-h-reservas.tex']}
manifest['ramas']=subprocess.check_output(['git','for-each-ref','--format=%(refname) %(objectname)','refs/heads'],cwd=r,text=True)
(out/'conservacion.json').write_text(json.dumps(manifest,ensure_ascii=False,indent=2),encoding='utf-8')

def table(number,label,title,cols,headers,rows):
    # Preserve every existing table number, including the IA declaration.
    return ('\n\\begingroup\n\\edef\\sdTablaAnterior{\\number\\value{table}}\n'
            '\\renewcommand{\\thetable}{'+number+'}\n'
            '\\renewcommand{\\theHtable}{sd821-'+label+'}\n'
            '\\begin{tablalafrox}{'+title+'}{tab:sd821-'+label+'}{'+cols+'}{'+headers+'}\n'
            +'\n'.join(' & '.join(row)+r' \\' for row in rows)+'\n'
            '\\end{tablalafrox}\n\\setcounter{table}{\\sdTablaAnterior}\n\\endgroup\n')

old=next(line for line in s.splitlines() if line.startswith('\\paragraph{Análisis de modos de falla}'))
fmea=r'''\paragraph{Análisis de modos de falla y decisión de tratamiento}
El FMEA del Anexo 8.G comprende los 15 riesgos inicialmente Altos o Crítico.
La Tabla~\ref{tab:sd821-fmea} muestra los cinco que siguen en esas zonas aun
con el tratamiento proyectado. La severidad $S$ sigue el impacto global; la
ocurrencia $O$ es la banda ordinal de la probabilidad del evento en su ventana,
y $D$ expresa dificultad de detección antes del efecto. El número de prioridad
es $NPR=S\times O\times D$, en una escala de 1 a 125. El índice organiza la
atención de los modos de falla, mientras $E=q_P\times q_I$ determina su zona:
no son magnitudes intercambiables ni porcentajes de eficacia.
'''
fmea+=table('8.2.3-A','fmea','FMEA aplicado a los cinco riesgos prioritarios. Fuente: Anexo 8.G.1; valores posteriores proyectados, sujetos a evidencia.',
 'F{0.12} F{0.20} F{0.20} Y',r'\cab{Riesgo} & \cab{S/O/D; NPR inicial} & \cab{S1/O1/D1; NPR1} & \cab{Lectura para decidir}',[
 ('R-002','5/4/5; 100','5/4/3; 60','La conciliación detecta faltantes, pero no reconstruye historia sanitaria inexistente. Conservar gravedad 5 y bloqueo del lote sin trazabilidad.'),
 ('R-006','4/4/5; 80','4/3/3; 36','El cotejo temprano puede recuperar fuentes; la cobertura histórica puede seguir incompleta. Mantener pendiente la comparación sin referencia reproducible.'),
 ('R-029','4/4/4; 64','4/3/2; 24','La mejora requiere tutor y evaluación de cada alta, con cobertura certificada del turno. Una capacitación aislada no demuestra capacidad sostenida.'),
 ('R-030','4/3/5; 60','4/3/2; 24','El ensayo debe verificar la interfaz y extracción reales. Un contrato escrito o archivo leído sin conciliación no habilita integración.'),
 ('R-031','4/3/4; 48','4/3/2; 24','La revisión diaria mejora detección del incumplimiento, pero no elimina la amenaza al cierre ni crea ventanas de cambio en septiembre.')])
fmea+=r'''
R-002 mantiene prioridad obligatoria por severidad 5, aunque su NPR proyectado
baje de 100 a 60. En los otros cuatro casos, la reducción de NPR procede de
hipótesis de ocurrencia y detección; la severidad permanece en 4. Por tanto,
un NPR menor no autoriza a declarar manejable el riesgo ni a reducir su impacto.
CAL debe contrastar el ensayo o acta con el alcance y período expuestos; sin esa
evidencia se retienen las puntuaciones iniciales para decidir. La respuesta
ejecutiva y sus condiciones se sintetizan en 8.3.1; el detalle de los quince
modos y sus fundamentos permanece en 8.G.1.
'''
s=s.replace(old,fmea)

needle='La matriz 8.F.2a concreta para esos cinco riesgos'
start=s.index(needle);end=s.index('\\subsection{Reservas y cronograma}',start)
responses=r'''\paragraph{Tratamiento ejecutivo de los riesgos que conservan prioridad}
La Tabla~\ref{tab:sd821-respuestas} concentra qué se hace, quién actúa y qué
permite continuar. E0 es la valoración inicial y E1 la proyección del tratamiento
completo; A/C son HH preventivas adicionales y HH de respuesta contenidas en el
esfuerzo condicional. C no se suma otra vez a H0. Las fechas de coordinación
mantienen los plazos y restricciones de 8.A.2 y 8.F.1.
'''
responses+=table('8.3.1-A','respuestas','Respuestas prioritarias y puertas de decisión. Fuente: Anexos 8.A.2, 8.F.1, 8.F.2 y 8.F.2a.',
 'F{0.13} F{0.23} F{0.23} F{0.10} Y',r'\cab{ID / E0--E1} & \cab{Medida y responsable} & \cab{Disparador y plazo} & \cab{A/C (HH)} & \cab{Evidencia y bloqueo}',[
 ('R-002 / 0,56--0,56; Crítica','DAT concilia vínculos por lote y aísla excepciones; Calidad del CLIENTE decide V-07.','Faltante al perfilar: aislar el mismo día. Política en mes 2; excepciones a D-5 y decisión antes del corte.','12/24','Origen verificable y prueba de exclusión de carga/despacho. Sin vínculos exigidos, lote bloqueado incluso con resolución firmada.'),
 ('R-006 / 0,28--0,20; Alta','IMP/CAL reproducen OTIF y cuadratura; Comercial, Operaciones y Finanzas validan fuentes V-10.','Referencia al cierre del mes 1. Ante bloqueo, JP reúne áreas en dos días hábiles y exige evidencia o eleva en cinco.','8/16','Fuentes, período y cálculo reproducibles. Sin historia verificable, comparación y aceptación afectadas bloqueadas; las mediciones futuras no la sustituyen.'),
 ('R-029 / 0,28--0,20; Alta','IMP hasta mes 21, SRE desde 22: verificar altas, tutoría y cobertura certificada con Bodega/Operaciones.','Antes del turno y de cada alta autónoma, meses 13--56. Revisar a diario; proponer refuerzo en dos días hábiles.','12/32','Tutor disponible, aprendizaje máximo dos horas y evaluación aprobada antes de autonomía. Si falla o desborda capacidad, impedir trabajo autónomo y revalidar refuerzo.'),
 ('R-030 / 0,20--0,20; Alta','ARQ/DAT ensayan con TI intercambio y extracción ERP/WMS; CAL verifica.','Brecha: elevar al finalizar semana 2 del mes 1. Contrato inicial al cierre del mes 1; ensayo aprobado antes de integración.','12/24','Entradas/salidas, tiempos y conciliación contra origen; integridad, latencia y emisión por ERP. Bloquear integración dependiente si falla; corregir y repetir.'),
 ('R-031 / 0,20--0,20; Alta','JP/CAL verifican habilitaciones, continuidad y las seis condiciones acumulativas de cierre con Operaciones.','Antes de congelamiento; control diario en meses 19--20. Escalar incumplimiento el mismo día y acordar recuperación en dos días hábiles.','8/16','Ensayo previo y período completo de evidencia, incluidas cuatro semanas finales y acta. Una condición incumplida mantiene cierre pendiente; respetar ventanas y R-020.')])
responses+=r'''
CAL distingue resultado satisfactorio, insuficiente y fallido conforme a 8.F.2a.
Sólo el satisfactorio permite proponer levantar el bloqueo concreto y reevaluar
con las escalas de 8.1.3 y la aprobación competente. Los otros dos exigen
corrección y nueva verificación, conservando la valoración inicial para decidir.
El objetivo de seguimiento es $E<0,20$ en la misma ventana de exposición;
las proyecciones de estos cinco riesgos todavía no lo alcanzan. Tampoco basta
una habilitación puntual para rebajar toda la ventana del riesgo.

Las A/C de la tabla son las hipótesis vigentes de esfuerzo, no dotación
comprometida. Antes de programar conciliaciones y ensayos completos, cada dueño
contrasta preparación, ejecución, corrección y repetición con volumen y capacidad.
JP identifica lo ya cubierto por la EDT y somete cualquier diferencia a nivelación
y autorización. El trabajo ordinario de capacitación, pruebas y corrección del
diseño conserva su presupuesto; se evita cargarlo también como contingencia.

\paragraph{Decisión ante un retorno de esfuerzo menor que uno}
El costo-beneficio de 8.F.3 compara exclusivamente HH. El beneficio bruto es
$B=p_0H_0-p_1(H_0-C)$ y el trabajo de tratamiento es $T=A+p_1C$; el saldo
$B-T=(p_0-p_1)H_0-A$ descuenta prevención y evita contar dos veces la respuesta.
La Tabla~\ref{tab:sd821-retorno} expone dos tratamientos obligatorios cuyo retorno
estimado no cubre el trabajo invertido. Los valores se presentan con dos
decimales; el cálculo conserva la precisión original.
'''
responses+=table('8.3.1-B','retorno','Tratamientos que se mantienen aun con retorno HH menor que uno. Fuente: Anexo 8.F.3.',
 'F{0.12} F{0.36} F{0.27} Y',r'\cab{Riesgo} & \cab{Entradas del modelo} & \cab{Resultado en HH} & \cab{Decisión}',[
 ('R-002',r'H0=194,67; p0=p1=60\%; A=12; C=24.','B=14,40; T=26,40; B/T=0,55; neto=-12,00.','Conservar tratamiento sanitario obligatorio. Aislar limita exposición operativa, pero no reduce la ocurrencia de historia irrecuperable.'),
 ('R-031',r'H0=73,33; p0=45\%; p1=35\%; A=8; C=16.','B=12,93; T=13,60; B/T=0,95; neto=-0,67.','Conservar continuidad y condiciones contractuales del cierre. Corregir capacidad o programación no equivale a aceptar un hito sin evidencia.')])
responses+=r'''
En R-002, p0=p1 deja el saldo en menos 12 HH: la respuesta atiende el evento,
pero no recupera el trabajo preventivo ni restituye información inexistente.
Por eso la inversión se justifica por protección sanitaria y trazabilidad, no
por ahorro neto en HH. En R-031, la reducción de ocurrencia propuesta todavía
deja un saldo negativo de 0,67 HH; el equilibrio requeriría justificar p1 no mayor
que 34,09\%, frente al 35\% proyectado. Se mantiene el tratamiento para proteger
el cierre, sin atribuirle esa mejora adicional. Ningún indicador HH valoriza
mercadería, multas o seguridad ni sustituye un criterio de aceptación.

'''
s=s[:start]+responses+s[end:]

start=s.index('La exposición inicial es de 1.199,52 HH.');end=s.index('La reserva de gestión propuesta es de 160 HH:',start)
reserves=r'''La Tabla~\ref{tab:sd821-reservas} distingue la exposición de esfuerzo de los
fondos de capacidad que se proponen o ya están programados. Esta separación
permite que JP presente una necesidad adicional identificable, sin sumar un
subconjunto como si fuera otra reserva. Los importes son HH, no dinero ni días.
'''
reserves+=table('8.3.2-A','reservas','Lectura ejecutiva de exposición, tratamiento y reservas. Fuente: Anexos 8.B.1 y 8.H.1--3.',
 'F{0.32} F{0.16} Y',r'\cab{Concepto} & \cab{HH} & \cab{Uso y regla de no duplicación}',[
 ('Exposición inicial p0H0','1.199,52','Referencia previa al tratamiento; no se agrega al total posterior.'),
 ('Prevención adicional A','180,00','Trabajo planificado por aprobar y contrastar con paquetes ordinarios.'),
 ('Contingencia específica p1H0','837,53','Incluye respuesta y remanente. Se nivela por mes/perfil y depende de la evidencia que sustenta p1.'),
 ('Respuesta p1C, dentro de contingencia','142,00','Subconjunto de 837,53 HH; no sumar como reserva independiente.'),
 ('Remanente p1L, dentro de contingencia','695,53','L=H0-C; completa la contingencia junto con p1C.'),
 ('Total posterior A+p1H0','1.017,53','Prevención más contingencia; excluye gestión y protección del SD7.'),
 ('Gestión propuesta','160,00','Cuatro ciclos de 40 HH por causas aún no identificadas, sujetos al Comité Ejecutivo.'),
 ('Protección programada de E1','3.072,00','Ya incluida en SD7; crédito inicial cero contra la propuesta de contingencia. No se presta a E2.')])
reserves+=r'''
La igualdad $142,00+695,53=837,53$ muestra que respuesta y remanente particionan
la contingencia; $180,00+837,53=1.017,53$ integra el esfuerzo posterior. Estas
sumas impresas resumen el modelo calculado sin redondeo intermedio. Las
3.072 HH ya forman parte de 202.108,62 HH programadas sobre 199.036,62 HH
base/cobertura; añadirlas de nuevo duplicaría capacidad. Sus componentes,
1.152 HH en meses 13--15 y 1.920 HH en 16--20, conservan protección exclusiva E1.

'''
s=s[:start]+reserves+s[end:]

needle='La suspensión del proveedor de lácteos'
start=s.index(needle)
controls=r'''\paragraph{Pruebas que habilitan continuidad y capacidad}
El cuadro siguiente permite decidir por alcance, sin confundir riesgo externo
con obligación de diseño. R-034 conserva la dependencia del ERP; CT-15,
CT-03 y CT-14 son controles ordinarios. R-036 registra la incertidumbre del perfil
real, no traslada al CLIENTE un dimensionamiento insuficiente del peak conocido.
'''
controls+=table('8.3.3-A','habilitacion','Condiciones ejecutivas de habilitación por alcance. Fuente: Anexos 8.D.3 y 8.E.1; R-034/R-036 de T-16.',
 'F{0.16} F{0.27} F{0.37} Y',r'\cab{Alcance} & \cab{Decisión de diseño} & \cab{Prueba y evidencia exigida} & \cab{Responsable y puerta}',[
 ('ERP / R-034','ERP único emisor. Recuperar WMS no recupera ERP; sin guía válida se bloquea la salida.','AL-DTE-01: 96 salidas, guía vigente y cambio de carga. AL-DR-01: pérdida de sala, restitución y tiempos frente a RTO 4 h/RPO 15 min. Bloqueo correcto no demuestra continuidad de las 96 salidas.','ARQ/SRE con TI, Finanzas y Operaciones; CAL verifica antes de H5/H10.'),
 ('Stock / CT-15','Confirmar reserva central sólo con retención local durable y autoridad única por ámbito.','AL-STOCK-01: última unidad, UUID/época, acuse perdido y reintento sin doble reserva ni stock negativo. AL-DR-01: exclusión de escritor, promoción, retorno y conciliación. E1: preventa real; E2: portal y EDI reales.','DAT hasta 21; SRE desde 22; ARQ diseña y CAL verifica. No aceptar E2 mediante simulador.'),
 ('Identidad / CT-03','Identidad conectada/local, mínimo privilegio y vigencia que no se amplía por reinicio o reloj.','AL-ID-01/AL-OFF-01: manifiesto 26 h, corte una hora después, relevos 8/16 h; ruta 14,5 h y máximo 16 h. Cero accesos indebidos; baja local y central aislada diferenciadas, cola conservada y conciliación única.','SEG responde; ARQ diseña; DES/SRE ejecutan; CAL verifica antes de H5/H10. Seguridad conserva G5.'),
 ('Capacidad / CT-14 y R-036','Soportar peak y crecimiento comprometidos; confirmar concentración temporal y mezcla del perfil real.','Comparar perfil validado/observado; carga y estrés por ventana, ERP, colas, errores, p95 y recuperación frente a requisitos vigentes. Si satura dentro del alcance, LafroX corrige y repite como trabajo ordinario.','SRE/ARQ, DES y CAL con Operaciones/TI. Perfil en mes 1; revalidar antes de H5/H10, peak y cambios.')])
controls+=r'''
En los cuatro alcances, el expediente identifica versión, configuración, datos
de entrada, resultado esperado y observado, incidencias y repetición tras
corrección. Evidencia insuficiente o prueba fallida mantiene la promoción
afectada pendiente. Sólo evidencia satisfactoria y aprobación competente
habilitan ese alcance; el hito requiere además el acta. Así se distingue una
prueba prevista, una implementación verificada y una aceptación contractual.
Los ensayos detallados y su trazabilidad por etapa permanecen en 8.D.3 y 8.E,
sin agregar contingencia por controles ordinarios ni declarar pruebas ejecutadas.

'''
s=s[:start]+controls+s[start:]
s=s.replace('\\textbf{Operación del cliente} (13)','\\textbf{Operación del cliente} (14)')
s=s.replace('Los anexos desarrollan las respuestas y dependencias operativas, el fundamento de las estimaciones, los controles técnicos, el análisis FMEA y la evaluación residual.',
 'El cuerpo presenta FMEA aplicado, decisiones de respuesta, costo-beneficio en HH, reservas y puertas de habilitación. Los anexos conservan las fichas exhaustivas, dependencias, fundamentos de estimación, controles y evaluaciones completas para verificar y ejecutar esas decisiones.')
p.write_bytes(s.replace('\n','\r\n' if b'\r\n' in raw else '\n').encode('utf-8'))
print('Cuerpo ampliado: cinco cuadros técnicos y decisiones; anexos/T-16 sin cambios.')
