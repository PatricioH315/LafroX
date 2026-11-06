from pathlib import Path
from decimal import Decimal as D, ROUND_HALF_UP
from collections import Counter
import re, json, hashlib

r=Path(__file__).resolve().parents[1]
paths=['LAFROX-Formulario-T-16.tex','LAFROX-Subdocumento8-Anexos.tex','08_plan_riesgos/contenido.tex','08_plan_riesgos/figuras/rbs.tex']
old={p:(r/p).read_text(encoding='utf-8') for p in paths}
if (r/'tmp/tarea6-baseline.json').exists():
 assert json.loads((r/'tmp/tarea6-baseline.json').read_text(encoding='utf-8'))['original']==old, 'No sobrescribir una aplicación completada'
sources={str(p.relative_to(r.parent)):hashlib.sha256(p.read_bytes()).hexdigest() for p in (r.parent/'Informe propuesta tecnica/Informe_2_LafroX').glob('Subdocumento_*/*.pdf')}
(r/'tmp/tarea6-baseline.json').write_text(json.dumps({'original':old,'source_hashes':sources},ensure_ascii=False,indent=2),encoding='utf-8')
f,a,b,rb=[old[p] for p in paths]
internal={f'R-{i:03}' for i in [9,10,23,24,25,26,27,34,35,36,37,38,40,47,48,50]}
ci=lambda rid:rid.replace('R-','CI-')
def section(s,needle):
 start=s.index(needle);return s[start:s.index('\\end{tablalafrox}',start)]
def rows(s):return [l.split(' & ') for l in s.splitlines() if re.match(r'R-\d{3}(?: / [A-Z]+)? &',l)]
def rowmap(s):return {c[0]:c for c in rows(s)}
reg=rowmap(f)
q=rowmap(section(a,'\\begin{tablalafrox}{Estimación acumulada'))
imp=rowmap(section(a,'\\begin{tablalafrox}{Fundamento del impacto inicial'))
resp=rowmap(section(a,'\\begin{tablalafrox}{Matriz de respuestas'))
ledger=section(a,'\\begin{tablalafrox}{Hipótesis de ocurrencia')
active={k:v for k,v in reg.items() if k not in internal}
num=lambda x:D(x.replace(',','.'))
round2=lambda x:x.quantize(D('.01'),rounding=ROUND_HALF_UP)
fmt=lambda x:f'{x:.2f}'.replace('.',',')
pretty=lambda x:fmt(x)[:-6]+'.'+fmt(x)[-6:] if x>=1000 else fmt(x)
ve={k:num(v[7].rstrip('\\')) for k,v in q.items()}
total=sum((ve[k] for k in active),D(0));removed=sum((ve[k] for k in internal),D(0))
top=sorted(active,key=lambda k:(-ve[k],k))[:10];topval=sum((ve[k] for k in top),D(0));share=round2(topval/total*100)
ex={k:num(v[5].split(' ')[0]) for k,v in active.items()};topqual=sorted(active,key=lambda k:(-ex[k],k))[:10]
zones=Counter(re.search(r'\(([^)]+)\)',v[5])[1] for v in active.values());cats=Counter(v[2] for v in active.values())
print('Activos',len(active),'internos',len(internal),'VE',total,'retirado',removed,'top',topval,'porcentaje',share,'zonas',zones,'ramas',cats)

# Retirar únicamente las filas activas: las fuentes completas quedan en la base de auditoría.
def filter_rows(s):
 return '\n'.join(l for l in s.split('\n') if not any(re.match(re.escape(k)+r'(?: / [A-Z]+)? &',l) for k in internal))
f=filter_rows(f);a=filter_rows(a)
deps=rows(section(a,'\\begin{tablalafrox}{Contrapartes, solicitudes'));assert len(deps)==28
for oldn,newn in [('51 riesgos','35 riesgos'),('51 registros','35 registros'),('31 riesgos','28 riesgos')]:
 f=f.replace(oldn,newn);a=a.replace(oldn,newn);b=b.replace(oldn,newn)
f=f.replace('del proyecto (R-001 a R-051); R-034 a R-040 son los riesgos de adopción de las cinco innovaciones del Subdocumento 13.', 'declarados al CLIENTE; conserva los ID originales con discontinuidades. Los 16 asuntos internos retirados, incluidos los 13 indicados por la revisión, se siguen como CI en el Anexo 8.E y no integran esta tabla.')
f=f.replace('El Anexo 8.D vincula las cuatro brechas de arquitectura y rotación con R-048, R-049, R-050 y R-042, y verifica las demás omisiones del caso.', 'El Anexo 8.D vincula las brechas con CI-048, R-049, CI-050 y R-042 y verifica las demás omisiones. CI-048 y CI-050 son verificaciones internas, no riesgos transferidos al CLIENTE.')
f=f.replace('No se establece aquí una reserva cuantitativa.', 'Los ID retirados no se reutilizan ni se renumeran. No se establece aquí una reserva cuantitativa.')
a=a.replace('para los 35 riesgos vigentes, R-001--R-051.', 'para los 35 riesgos vigentes de T-16, conservando sus ID discontinuos. Los 16 asuntos internos CI están excluidos y sus estimaciones anteriores se archivan en 8.E, sin constituir reserva del CLIENTE.')
a=a.replace('R-041--R-051 son juicios', 'los ocho riesgos vigentes añadidos desde R-041 son juicios')
a=a.replace('la remediación de capacidad pertenece a R-047.', 'la verificación y remediación de capacidad pertenece a CI-047 (Anexo 8.E).')
a=a.replace('R-049 y R-050 cuantifican fallas propias de sus dependencias.', 'R-049 cuantifica la dependencia del ERP del CLIENTE; CI-050 conserva la corrección y verificación de consolidación dentro del proveedor.')
a=a.replace('R-045--R-048 y R-050 conservan la responsabilidad técnica de LafroX: sus controles de diseño y mantenimiento ordinario se verifican en arquitectura/calidad y no se presupuestan otra vez como contingencia.', 'R-045 y R-046 conservan sólo cambios excepcionales externos de soporte o restricciones efectivas de salida. El mantenimiento, la portabilidad y las actualizaciones ordinarias son obligaciones de LafroX; no se presupuestan otra vez como contingencia. CI-047, CI-048 y CI-050 y sus hipótesis previas se archivan en 8.E, fuera de esta suma.')
a=a.replace('Total VE} & & 1594,93',f'Total VE}} & & {fmt(total)}')
a=a.replace('Este anexo estima contingencia de esfuerzo', 'Este anexo estima exposición de esfuerzo')
a=a.replace('La suma de VE se presenta como contingencia de esfuerzo,', 'La suma de VE se presenta como exposición de esfuerzo pendiente de conciliación en la tarea de reservas,')

# Rehacer la explicación de la RBS para no conservar riesgos internos dentro de sus ramas.
start=b.index('La estructura de desglose de riesgos')
end=b.index('\\subsection{Análisis cualitativo de riesgos}',start)
newrbs=r'''La estructura de desglose de riesgos (EDR o RBS) organiza los \textbf{35 riesgos vigentes de T-16} de la Figura~\ref{fig:sd8-rbs}, conservando sus ID originales. Las seis ramas identifican la fuente predominante, no la prioridad: \textbf{Solución y tecnología} (3), \textbf{Integración y legado} (6), \textbf{Operación del cliente} (13), \textbf{Personas y adopción} (8), \textbf{Contrato y licitación} (3) y \textbf{Regulatorio y externo} (2).

\parte{figuras/rbs}

\textbf{Solución y tecnología} conserva la historia sanitaria de origen que el CLIENTE debe aportar (R-002), el cambio excepcional externo de soporte/compatibilidad (R-045) y la restricción efectiva de salida o sustitución del proveedor tecnológico (R-046). La elección, el mantenimiento ordinario y la portabilidad del diseño siguen a cargo de LafroX. R-045/R-046 no cubren tecnología elegida sin soporte ni falta de un plan de salida obligatorio.

\textbf{Integración y legado} reúne certificación externa de cadenas (R-001), historia de ventas (R-003), deuda vigente adicional (R-007), respuesta del SII (R-008), interfaces legadas no documentadas (R-043) y disponibilidad del ERP del CLIENTE para emitir nuevas guías (R-049). La idempotencia del POS y la continuidad del servicio de mapas elegido se siguen como CI-009 y CI-010, fuera de T-16.

\textbf{Operación del cliente} conserva R-004--R-006, R-011--R-012, R-014, R-018--R-020, R-022 y R-028--R-030: conciliaciones y datos de aceptación, matriz térmica, equipamiento y permisos, decisiones, enlaces y energía externos y eventos de transporte. Son trece riesgos; cada episodio se imputa una sola vez a su causa principal.

\textbf{Personas y adopción} conserva ocho riesgos: firma del transportista (R-013), adopción del proceso (R-015), transferencia del conocimiento del planificador (R-016), asistencia a capacitación (R-017), sustitutos no habilitados (R-031), acuerdo de telemetría (R-041), rotación nocturna (R-042) y rechazo individual de conductores externos (R-051). El 38\% es rotación anual, no $p_0$.

\textbf{Contrato y licitación} conserva cambios de alcance (R-032), liquidación variable de INN-04 (R-039) y coordinación del cierre bajo peak/congelamiento (R-044). \textbf{Regulatorio y externo} conserva residencia/transferencia aprobada (R-021) y cambios normativos aplicables (R-033).

\textbf{Separación del seguimiento interno.} La revisión identifica trece asuntos de diseño y construcción: R-009, R-010, R-023--R-027, R-034--R-038 y R-040. Se retiran de T-16, 8.A--8.C y la RBS, sin renumerar los restantes, y pasan a CI con el mismo sufijo en el Anexo 8.E. El mismo criterio se aplica a R-047, R-048 y R-050: dimensionamiento, identidad y consistencia central son obligaciones de arquitectura/calidad, no incertidumbre transferible al CLIENTE. Las brechas B-S4-01 y B-S4-03 quedan vinculadas a CI-048 y CI-050; B-S4-02 y B-S7-01 conservan R-049 y R-042.

El Anexo 8.E fija destino propuesto en S4/S13/S9, dueño, control obligatorio, evidencia, momento de verificación y actuación ante incumplimiento. Sus valoraciones previas se conservan sólo como historia; no forman parte de la exposición ni de las reservas del registro del CLIENTE. La reubicación no declara implementado ni cerrado ningún control. Los otros subdocumentos se consultan y su sincronización queda pendiente, sin editarlos aquí.

Para CI-034 se conserva el paquete 3.10.1.4 en meses 11--15: certificación H5 en 11--12 y piloto con locales reales en 13--15. IMP coordina el piloto, DAT dirige INN-01 y Comercial/Calidad validan el catálogo en meses 7--9. I-01A exige al menos 70\% con al menos 100 avisos evaluables en mes 15; mientras no se demuestre, no se amplía la innovación. Su ubicación interna no elimina el piloto ni convierte su resultado pendiente en aceptación de un defecto.

'''
b=b[:start]+newrbs+b[end:]
# Actualizar los diez primeros a partir de las mismas valoraciones vigentes, sin revalorar.
def replace_table_rows(s,needle,newrows):
 sec=section(s,needle);ls=sec.splitlines();out=[];done=False
 for l in ls:
  if re.match(r'R-\d{3} &',l):
   if not done:out+=newrows;done=True
  else:out.append(l)
 return s.replace(sec,'\n'.join(out)+'\n')
qualrows=[f'{k} & {active[k][3].split(" / ")[1]} & {active[k][4].split(" / ")[1]} & {active[k][5].split(" ")[0]} & {re.search(r"\(([^)]+)\)",active[k][5])[1]} '+r'\\' for k in topqual]
short={m[0]:m[1] for m in re.findall(r'\\RBSrisk\{(R-\d{3})\}\{([^\n]+?)\}\{[^}]+\}',rb)}
quantrows=[f'{k} & {short[k]} & {q[k][1]} & {q[k][6]} & {q[k][7].rstrip(chr(92))} '+r'\\' for k in top]
b=replace_table_rows(b,'\\begin{tablalafrox}{Diez riesgos de mayor exposición',qualrows)
b=replace_table_rows(b,'\\begin{tablalafrox}{Diez mayores valores esperados',quantrows)
start=b.index('R-002, R-037 y R-038 conservan exposición')
end=b.index('\\subsection{Análisis cuantitativo}',start)
b=b[:start]+f'El registro del CLIENTE contiene {zones["Crítica"]} riesgo crítico, {zones["Alta"]} altos, {zones["Media"]} medios y {zones["Baja"]} bajos. R-002 conserva E=0,56 y zona Crítica; retirar CI no reduce su valoración. La Tabla 8.5 selecciona diez por producto y desempata por ID, sin sustituir el conjunto de riesgos altos. Las valoraciones históricas internas se distinguen en 8.E y no se mezclan con esta distribución. La evaluación residual de los riesgos vigentes corresponde a la siguiente tarea de respuestas.\n\n'+b[end:]
b=b.replace('del registro vigente (R-001--R-051)', 'del registro vigente, con ID originales discontinuos')
b=b.replace('739,40',fmt(topval)).replace('1.594,93',pretty(total)).replace('46,4',str((topval/total*100).quantize(D('.1'),rounding=ROUND_HALF_UP)).replace('.',','))
# La retirada es un cambio de perímetro, no un ahorro ni una liberación de reserva.
anchor='\\subsection{Reservas y cronograma}\n'
b=b.replace(anchor,anchor+f'\nLa reclasificación conserva la conciliación histórica: 1.594,93 HH de los 51 registros anteriores = {pretty(total)} HH de los 35 riesgos vigentes + {fmt(removed)} HH de los 16 asuntos internos archivados en 8.E. Es una separación de perímetro, no una reducción de esfuerzo demostrada ni reserva liberada. Las HH históricas internas no se agregan a la contingencia del CLIENTE ni se convierten automáticamente en costo de calidad. Su trabajo ordinario debe verificarse contra los paquetes existentes; cualquier diferencia requiere estimación y control de cambios, sin duplicación.\n')
b=b.replace('brechas todavía no incorporadas al registro', 'hallazgos incorporados y su clasificación vigente')
b=b.replace('El Formulario T-16 reúne el registro', 'El Anexo 8.E conserva el seguimiento interno de diseño y calidad y sus destinos propuestos. El Formulario T-16 reúne el registro')

# Filtrar RBS y actualizar contadores por rama; la figura conserva los dos folios.
rb='\n'.join(l for l in rb.split('\n') if not any('\\RBSrisk{'+k+'}' in l for k in internal))
rb=rb.replace('51 riesgos','35 riesgos')
counts=[3,6,13,8,3,2];idx=iter(counts)
rb=re.sub(r'\{\\small \d+ riesgos\}',lambda m:'{\\small '+str(next(idx))+' riesgos}',rb)

# La trazabilidad histórica D no debe afirmar que un CI permanece en T-16.
dstart=a.index('\\section{Anexo 8.D:');dend=a.index('\\section*{Referencias}',dstart)
d=a[dstart:dend]
for k in sorted(internal):d=d.replace(k,ci(k))
para_start=d.index('Las cuatro brechas se incorporan')
para_end=d.index('\\begingroup',para_start)
d=d[:para_start]+r'''Las brechas se conservan como B-S4-01 $\rightarrow$ CI-048, B-S4-02 $\rightarrow$ R-049, B-S4-03 $\rightarrow$ CI-050 y B-S7-01 $\rightarrow$ R-042. Los CI son controles internos retirados de T-16 y seguidos en 8.E; sólo los R vigentes integran 8.A--8.C. La matriz conserva el hallazgo original y actualiza su destino; una verificación prevista no demuestra control implementado ni riesgo residual aceptado.

'''+d[para_end:]
def replace_row(s,prefix,line):
 lines=s.split('\n');found=[i for i,l in enumerate(lines) if l.startswith(prefix+' &')];assert len(found)==1,(prefix,found);lines[found[0]]=line+r' \\';return '\n'.join(lines)
d=replace_row(d,'TR-01',r'TR-01 & S13, 13.1.3--13.1.7, pp. 12--17; Tabla 13.3. T-15, pp. 21 y 50, EDT 3.10.1.4. & CI-034 (antes R-034); Anexo 8.E, control de INN-01. Paquete 11--15; certificación 11--12; piloto real 13--15; I-01A mes 15. & Ventana aclarada en tarea 4; en tarea 6 se retira de T-16 por diseño de innovación. No se elimina el piloto. & IMP coordina piloto y DAT dirige INN-01; Comercial/Calidad validan catálogo 7--9. No ampliar sin al menos 70\% de aciertos con al menos 100 avisos evaluables en mes 15. Sincronizar S13 para distinguir paquete y piloto y sustituir su referencia al registro del CLIENTE por CI-034.')
d=replace_row(d,'TR-02',r'TR-02 & S13, 13.1.7--13.5.7; S8, Anexo 8.E y escalas de 8.1.3. & CI-034--CI-038 y CI-040 quedan en diseño/verificación; R-039 sigue en T-16, I=3, E=0,10 Media. & S13 conserva ID R y puntuaciones anteriores. La tarea 6 cambia ubicación; no reduce la valoración histórica de los CI ni acredita cierre. & Sincronizar S13 con 8.E: convertir seis referencias a controles internos de sus innovaciones, conservar indicador, dueño y condición de habilitación. Sólo R-039 permanece como riesgo de liquidación contractual. JP registra el cambio documental pendiente; valores anteriores de CI sólo en historia.')
d=replace_row(d,'TR-03',r'TR-03 & S4, Tabla 4 y 4.1.12, p. 78; identidad local pp. 26--27 y 46--47; AL-OFF-01 p. 81. & B-S4-01 $\rightarrow$ CI-048. CI-023/CI-027 son controles frente a compromiso de cuentas, distintos de continuidad. & R-048 se incorporó en tarea 5; la revisión de naturaleza lo retira de T-16 en tarea 6 por ser disponibilidad del diseño ofertado. & SEG responde del control, ARQ del diseño y SRE de ejecución. CAL exige antes de H5/H10 AL-OFF-01 con 24 h de corte, relevos 8/16 h, expiración, denegación y reconciliación. Anexo 8.E; destino S4, 4.1.12/4.1.15, y S9/T-13. No transferir autenticación pendiente al CLIENTE.')
d=replace_row(d,'TR-05',r'TR-05 & S4, Tabla 4, p. 78; 4.1.15--4.1.16, pp. 80--81; 4.3.2.5--4.3.2.6, pp. 183--184. & B-S4-03 $\rightarrow$ CI-050. R-004 sigue siendo conciliación inicial; R-019, enlace externo. & R-050 se incorporó en tarea 5; pasa a control interno por consistencia y autoridad de escritura de la solución, no a riesgo del CLIENTE. & DAT hasta mes 21 y SRE desde 22, con ARQ; CAL exige AL-STOCK-01 y AL-DR-01 antes de H5/H10: conciliación UUID/sitio, exclusión del escritor anterior, pendientes sin confirmación y retorno sin doble escritura. Destino S4, 4.1.16/4.3.2.5--6, y S9; seguimiento en 8.E.')
d=replace_row(d,'TR-06',r'TR-06 & S4, Tabla 4, p. 78; 4.2.5.4, p. 152. & R-008: SII externo sin confirmación. CI-009 (antes R-009): idempotencia y conciliación POS. & Se separan dependencia externa y obligación de integración. CI-009 ya no está en T-16 ni 8.A; queda en 8.E. & SRE sigue pendientes SII en R-008. ARQ verifica timeout antes/después del cargo, consulta con la misma clave y conciliación sin doble débito; CAL conserva regresión de integración. Sincronizar S4/S9/T-13. Un mismo corte WAN se imputa a R-019 una sola vez.')
d=d.replace('Incorporado como CI-048 en T-16 y 8.A--8.C.', 'Reubicado como CI-048 en 8.E.').replace('Incorporado como CI-050 en T-16 y 8.A--8.C.', 'Reubicado como CI-050 en 8.E.')
d=d.replace('Cada código B conserva el hallazgo y su ID de riesgo incorporado. La valoración está en 8.B--8.C y las respuestas en 8.A y T-16;', 'Cada código B conserva el hallazgo y su destino vigente: R-049/R-042 en T-16 y 8.A--8.C; CI-048/CI-050 en 8.E;')
d=d.replace('Brechas de cobertura incorporadas y vinculadas al T-16.', 'Brechas de cobertura y destino vigente en T-16 o seguimiento interno.')
d=d.replace('SEG es dueño del riesgo;', 'SEG responde del control interno;')
d=d.replace('La valoración debe separar incertidumbre de operación de defecto de diseño; conservar controles en arquitectura/calidad.', 'Reubicado en 8.E; no integra la exposición del CLIENTE. Destino S4/S9, cierre sujeto a prueba.')
d=d.replace('DAT es dueño hasta mes 21', 'DAT responde del control hasta mes 21')
d=d.replace('Valoración inicial en 8.B--8.C; verificar después la eficacia residual sin duplicar la corrección obligatoria del diseño.', 'Historia en 8.E; cierre por prueba de consistencia, sin transferir la corrección obligatoria al CLIENTE.')
d=d.replace('CI-047 es saturación técnica.', 'CI-047 es verificación interna de capacidad.')
d=d.replace('Validar capacidad efectiva, no sólo escalado declarado. Separar remediación técnica de la coordinación de R-044.', 'Control interno en 8.E y destino S4, 4.2.6/S9/T-13; retirado de T-16. Validar capacidad efectiva, no sólo escalado declarado; separar de R-044.')
a=a[:dstart]+d+a[dend:]

# Fichas internas: destino verificable, obligación, prueba y condición de bloqueo.
# No se declara realizada ninguna implementación o prueba.
controls={
9:('ARQ; DES implementa; CAL verifica.','S4, 4.1.2, 4.1.4.6 y 4.1.6.2; S9, 9.2.3/9.2.6; T-13, integración.','Idempotencia persistente, consulta de estado antes de reintentar, conciliación y estado pendiente sin confirmar.','Simular timeout antes/después del cargo y reenvío de la misma clave: una sola imputación y conciliación verificable. Antes de H5/H10 en el alcance aplicable; CAL bloquea promoción del flujo fallido.'),
10:('ARQ; SRE opera; CAL verifica.','S4, 4.1.4.5, 4.1.6.2 y 4.2.5.4; S9, 9.2.3; T-13, resiliencia.','Definir circuit breaker, caché de rutas autorizadas, límites y estado degradado ante caída del servicio de mapas elegido, sin dar nuevas rutas por calculadas.','Inyectar caída y recuperación del proveedor: continuidad autorizada de rutas disponibles, nuevas consultas pendientes y restitución sin pérdida. Antes de H5/H10 y tras cambio de proveedor; corregir el diseño si falla.'),
23:('SEG; DES/SRE ejecutan; CAL verifica.','S4, 4.1.3.7 y 4.1.18; S9, 9.2.3/9.2.6; T-13, seguridad.','Aplicar mínimo privilegio, controles de autenticación y sesión del diseño; detección, revocación, conservación de evidencia y recuperación frente a credencial comprometida.','Ensayar uso indebido y revocación, incluida operación sin conexión conforme a política aprobada; informe sin hallazgos críticos/altos abiertos antes de G5. No trasladar al CLIENTE un control omitido.'),
24:('ARQ; SEG valida autenticidad; CAL verifica.','S4, 4.1.2, 4.1.3.5 y 4.1.6.2; S9, 9.2.3; T-13, integración/seguridad.','Validar origen, integridad, correlación y repetición antes de procesar EDI; poner mensajes inválidos en cuarentena sin producir pedidos o avisos.','Pruebas negativas con firma/origen alterados, mensaje repetido y correlación inválida: rechazo trazable sin efecto de negocio. Antes de H10 para EDI y regresión del alcance aplicable; corregir antes de promover.'),
25:('SRE; SEG define política; CAL verifica.','S4, 4.1.3.1, 4.1.3.7 y 4.1.18; S9, 9.2.3; T-13, seguridad/terreno.','Proteger almacenamiento y sesiones, aplicar enrolamiento y capacidades de bloqueo/gestión remota disponibles; revocar accesos tras pérdida y delimitar exposición.','Ensayo de terminal extraviado en línea y sin señal: datos protegidos, acceso no autorizado denegado y revocación/bloqueo al recuperar enlace. Antes de H5/H10 y tras cambio de política; no presumir borrado remoto sin conectividad.'),
26:('SEG; SRE ejecuta; CAL verifica.','S4, 4.1.3.2, 4.2.5.2 y 4.2.6; S9, 9.2.3; T-13, seguridad/carga.','Aplicar límites, protección perimetral, aislamiento de portales y alertas; conservar capacidad para usuarios legítimos y continuidad de servicios críticos.','Inyectar ráfaga controlada en ambiente autorizado y medir bloqueo, latencia y disponibilidad contra umbrales de S4/T-13. Antes de H5/H10 y tras cambio perimetral; ningún ensayo ofensivo no autorizado en Producción.'),
27:('SEG; SRE ejecuta; CAL verifica.','S4, 4.1.3.7, 4.2.4.5 y 4.3.2.7; S9, 9.2.3/9.2.6; T-13, seguridad/recuperación.','Restringir privilegios, separar funciones, preservar auditoría y respaldos y comprobar recuperación ante cambios no autorizados de una cuenta administrativa.','Ensayar cambio indebido, detección, contención y restauración con integridad demostrada; recuperar conforme RTO/RPO exigidos. Antes de H5/H10, restauraciones y pruebas de seguridad periódicas de S9; no cerrar con evidencia comprometida.'),
34:('DAT dirige; IMP coordina piloto; CAL verifica.','S13, 13.1.4/13.1.6/13.1.7; Tabla 13.3, EDT 3.10.1.4; S9, 9.2.5.','Validar catálogo con Comercial/Calidad en 7--9, mostrar confianza y confirmar saldo en visita. Mantener alcance obligatorio; si no se valida, usar sólo aviso informativo por vida útil remanente.','Paquete 11--15: H5 en 11--12 y piloto real en 13--15. I-01A en mes 15: al menos 70\\% de aciertos sobre al menos 100 avisos evaluables. Sin cumplir, no ampliar INN-01 a otras rutas; corregir y repetir. Conservar el piloto bajo seguimiento interno.'),
35:('CAL; DES implementa; SRE aporta incidentes.','S13, 13.2.4/13.2.6/13.2.7; S9, 9.2.3--9.2.6.','Comparar reproducción con incidente de terreno y limitar captura de batería/datos. Conservar diagnóstico convencional y regresión base si la función opcional no demuestra utilidad.','Conservar casos incidente--reproducción y medición de I-02A y consumo contra lo comprometido en S13, antes de ampliar captura; corregir captura/reproducción fallida y no acreditar el indicador sin evidencia.'),
36:('SEG; DES implementa; CAL verifica.','S13, 13.2.4/13.2.7; S4, 4.1.3.7; S9, 9.2.4 y puertas 9.2.1.','Sanitizar por reglas fijas antes de sacar paquetes del terminal; minimizar datos y modelar amenazas. Suspender conjuntos afectados y producir muestra protegida ante filtración.','Pruebas con datos personales sembrados y campos no previstos: ningún dato personal sin sanitizar abandona el terminal; informe de revisión de amenazas y regresión. Bloquear la captura/exportación hasta aprobar, antes del primer uso y ante cada cambio de esquema.'),
37:('DAT; Calidad del CLIENTE valida parámetros; CAL verifica.','S13, 13.3.4/13.3.6/13.3.7; S4, 4.1.4.2; S9, 9.2.5.','Validar familias, mantener RNG-04 y no extender vencimiento por inferencia; presentar la estimación sólo en M9. Familia no validada conserva fecha impresa e historia visible.','Evidencia de I-03B por familia conforme a S13 antes de habilitar orden sugerido, con pruebas de no relajación de RNG-04. CAL bloquea familia no validada, DAT corrige y repite; la participación del CLIENTE no traslada responsabilidad de diseño.'),
38:('DAT; DES implementa; CAL verifica.','S13, 13.3.4/13.3.7; S4, 4.1.4.2--4.1.4.3 y 4.1.16; S9, 9.2.3.','Vincular lote--sensor mediante eventos de ubicación M2 y declarar tramos sin dato; impedir estimación cuando la historia esté incompleta.','Ensayar movimiento sin evento, sensor equivocado y sincronización tardía: historia incompleta visible y ninguna vida útil inferida sin fundamento. Antes de habilitar INN-03 y en regresión; corregir asociación antes de promover.'),
40:('IMP; DAT/DES implementan; SEG revisa privacidad; CAL verifica.','S13, 13.5.4/13.5.6/13.5.7; S9, 9.2.5; T-13, aceptación de usuario.','Codiseñar hoja comprensible; aplicar umbral de agregación y supresión en cada emisión comparativa y revisión legal previa. Conservar versión de un bloque si no se entiende y bloquear bloque 4 si expone terceros.','Prueba I-05B con usuarios y pruebas de inferencia conforme S13 antes de habilitar cada bloque; informe de comprensión y supresión. Corregir/repetir sin presentar el fracaso de diseño como riesgo del CLIENTE.'),
47:('SRE; ARQ dimensiona; DES corrige; CAL verifica.','S4, 4.1.19 y 4.2.6.10--4.2.6.12; S9, 9.2.3; T-13, carga/estrés.','Demostrar capacidad efectiva por ventana y dependencia, incluidos ERP, colas y recursos compartidos; ajustar el dimensionamiento ofertado sin degradar requisitos.','Pruebas de carga/estrés y p95 según S4/T-13, incluyendo peak y cuello de botella ERP, antes de H5/H10 y preparación de peak. Medir capacidad, colas, errores y recuperación; bloquear promoción si incumple. La coordinación comercial del cierre sigue en R-044.'),
48:('SEG; ARQ diseña; SRE ejecuta; CAL verifica.','S4, 4.1.12, 4.1.15, AL-OFF-01 p. 81; S9, 9.2.3; B-S4-01.','Resolver continuidad y revocación de identidad central/local. Separar manifiesto 26 h, caché 24 h y credenciales 8/14 h; denegar permisos inválidos y conservar personal autorizado sin abrir accesos por omisión.','AL-OFF-01: 24 h de corte, relevos 8/16 h, expiración, denegación y reconciliación, antes de H5/H10 y tras cambios; CAL bloquea alcance afectado si falla. Una disponibilidad pendiente del IdP elegido no se transfiere al CLIENTE.'),
50:('DAT hasta mes 21; SRE desde 22; ARQ diseña; CAL verifica.','S4, 4.1.15--4.1.16 y 4.3.2.5--4.3.2.6; S9, 9.2.3; B-S4-03.','Mantener una sola autoridad de escritura, conciliar UUID/sitio, excluir escritor anterior y conservar capturas pendientes; no confirmar stock global con copia vencida.','AL-STOCK-01/AL-DR-01 antes de H5/H10: pérdida central, promoción, retorno y reconciliación sin doble escritor ni doble reserva. CAL bloquea flujo inconsistente y exige regresión tras corrección. R-004 y R-019 conservan causas externas distintas.')}

e=r'''\clearpage
\section{Anexo 8.E: Seguimiento interno y reubicación documental}

Este anexo conserva los asuntos de diseño retirados del registro del CLIENTE, sin eliminarlos del seguimiento. La revisión del Informe 2 (sección S8, p. 34) identifica trece: R-009, R-010, R-023--R-027, R-034--R-038 y R-040. En la tarea 6 se aplica el mismo criterio a R-047, R-048 y R-050, añadidos en la tarea 5. Cada ID histórico R pasa a CI con el mismo sufijo; los ID R retirados no se reutilizan. T-16 y sus análisis contienen sólo 35 riesgos vigentes.

\subsection*{Regla de clasificación y cierre}
\addcontentsline{toc}{subsection}{Regla de clasificación y cierre}

Un CI es una obligación de diseño, construcción o verificación de LafroX. Un R vigente exige una condición externa o una decisión/aporte del CLIENTE que no puede sustituir unilateralmente LafroX. Que el CLIENTE participe en una prueba no convierte un defecto interno en riesgo transferible. Se conservan R-045 y R-046 sólo por cambios excepcionales externos de soporte y restricciones efectivas de salida; se excluyen mantenimiento ordinario, tecnología elegida sin soporte y ausencia de portabilidad debida al diseño. R-049 permanece por la restitución del ERP del CLIENTE, emisor único que LafroX no modifica; no equivale a la consistencia de su propio WMS, CI-050.

\textbf{Estado inicial de los 16 CI: reubicado; verificación pendiente.} La tabla define destino documental propuesto, no afirma que S4, S13 o S9 ya hayan cambiado. El dueño conserva una ficha con versión, requisito, caso de prueba, resultado, evidencia y defecto vinculado; CAL verifica, JP sigue el traslado y el cierre técnico. La sincronización documental permanece pendiente hasta ajustar cada destino, dentro del trabajo posterior autorizado. Los documentos externos a S8 se consultan sin editarlos.

La implementación y las pruebas se integran en los paquetes existentes de diseño, innovación y calidad; no se suman nuevamente las HH históricas a una reserva ni se presupone que cubran el costo del control. Una desviación abre un defecto según S9, 9.2.6, y repite la prueba/regresión. Las puertas G4/G5 de S9, 9.2.1, bloquean defectos críticos/altos y pruebas habilitantes fallidas; el CLIENTE no puede dispensar un requisito obligatorio mediante aceptación del riesgo. En Operación se mantiene el tratamiento de incidentes y la verificación periódica de S9, 9.3.3. Las funciones opcionales de innovación no demostradas se mantienen deshabilitadas según su ficha, conservando el alcance obligatorio.

\begingroup
\renewcommand{\thetable}{8.E.1}
\begin{landscape}
\setlength{\textwidth}{\linewidth}
\begin{tablalafrox}{Matriz de reubicación y control interno. Fuente: revisión de S8, registro anterior y destinos S4/S13/S9 indicados; criterios de verificación propuestos.}{tab:sd8-internos}{G{0.09} F{0.21} F{0.20} Y F{0.27}}{\cab{ID anterior / interno} & \cab{Evento retirado del registro del CLIENTE} & \cab{Dueño y destino documental} & \cab{Control de diseño o calidad requerido} & \cab{Evidencia, momento y actuación si falla}}
'''
for i, (owner,dest,action,test) in controls.items():
 k=f'R-{i:03}';e+=f'{k} / {ci(k)} & {reg[k][1]} & {owner} {dest} & {action} & {test} '+r'\\'+'\n'
e+=r'''\end{tablalafrox}
\end{landscape}
\endgroup

\subsection*{Historia cuantitativa excluida del registro vigente}
\addcontentsline{toc}{subsection}{Historia cuantitativa excluida del registro vigente}

Las siguientes cifras se conservan sin reestimación para auditar la separación de perímetro de la tarea 6. Son hipótesis anteriores de eventos y esfuerzo, no probabilidad residual vigente, costo de respuesta, deuda aceptada ni reserva para el CLIENTE. No demuestran cierre. Los supuestos de las tres incorporaciones recientes se archivan también en 8.E.4. El tratamiento económico y la conciliación de reservas corresponden a la tarea 8.

\begingroup
\renewcommand{\thetable}{8.E.2}
\begin{landscape}
\setlength{\textwidth}{\linewidth}
\begin{tablalafrox}{Estimaciones históricas internas excluidas de 8.B y T-16 (HH). Fuente: Anexo 8.B anterior a tarea 6, sin alterar valores.}{tab:sd8-internos-hh}{G{0.09} G{0.08} G{0.08} G{0.10} G{0.10} G{0.10} G{0.12} G{0.12}}{\cab{CI (antes R)} & \cab{$p_0$ anterior} & \cab{$n$ anterior} & \cab{O} & \cab{M} & \cab{P} & \cab{PERT} & \cab{VE anterior}}
'''
for k in sorted(internal):e+=' & '.join([ci(k)]+q[k][1:])+'\n'
e+=f'\\multicolumn{{6}}{{r}}{{Subtotal histórico interno excluido}} & & {fmt(removed)}'+r'\\'+'\n'
e+=r'''\end{tablalafrox}
\end{landscape}
\endgroup

\begingroup
\renewcommand{\thetable}{8.E.3}
\begin{landscape}
\setlength{\textwidth}{\linewidth}
\begin{tablalafrox}{Valoraciones iniciales históricas internas, sin reducción por la reubicación. Fuente: T-16 y Anexo 8.C anteriores a tarea 6.}{tab:sd8-internos-impacto}{G{0.08} F{0.16} F{0.17} Y}{\cab{CI (antes R)} & \cab{P / factor anterior} & \cab{I / factor; exposición y zona anteriores} & \cab{Justificación de impacto conservada}}
'''
for k in sorted(internal):e+=f'{ci(k)} & {reg[k][3]} & {reg[k][4]}; {reg[k][5]} & {imp[k][4]}'+'\n'
e+=r'''\end{tablalafrox}
\end{landscape}
\endgroup

\begingroup
\renewcommand{\thetable}{8.E.4}
\begin{landscape}
\setlength{\textwidth}{\linewidth}
\begin{tablalafrox}{Hipótesis previas de los CI añadidos en tarea 5; archivo fuera de la exposición del CLIENTE. Fuente: antigua Tabla 8.B.2.}{tab:sd8-internos-hipotesis}{G{0.08} F{0.19} Y F{0.28} F{0.18}}{\cab{CI / $p_0$ / $n$ previos} & \cab{Ventana anterior} & \cab{Fundamento anterior} & \cab{O/M/P y exclusiones anteriores} & \cab{Fuente de la condición}}
'''
for l in ledger.splitlines():
 if any(l.startswith(k+' / ') for k in internal):e+=ci(l)+'\n'
e+=r'''\end{tablalafrox}
\end{landscape}
\endgroup
'''
# Evitar referencias ambiguas a tablas activas dentro del archivo histórico nuevo.
e=e.replace('PERT anterior', 'PERT anterior')
a=a.replace('\\section*{Referencias}', '\\input{08_plan_riesgos/anexo-e-internos.tex}\n\n\\section*{Referencias}',1)
a=a.replace('LafroX SpA. (2026c).', 'LafroX SpA. (2026d).')
a=a.replace('Distribuidora Puelche S.A. (2026b).', 'LafroX SpA. (2026c). \\emph{Propuesta técnica: Subdocumento 9, Plan de calidad}, y formularios T-13 y T-17.\n\nDistribuidora Puelche S.A. (2026b).')

# Ninguna línea protegida se modifica.
for p,s in zip(paths,[f,a,b,rb]):
 assert [l for l in old[p].splitlines() if 'contenido academico' in l]==[l for l in s.splitlines() if 'contenido academico' in l],p
 (r/p).write_text(s,encoding='utf-8')
(r/'08_plan_riesgos/anexo-e-internos.tex').write_text(e,encoding='utf-8')
(r/'tmp/tarea6-datos.json').write_text(json.dumps({'active':list(active),'internal':sorted(internal),'total':str(total),'removed':str(removed),'top':top,'topval':str(topval),'topqual':topqual,'zones':dict(zones),'categories':dict(cats)},ensure_ascii=False,indent=2),encoding='utf-8')
