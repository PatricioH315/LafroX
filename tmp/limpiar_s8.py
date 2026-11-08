from pathlib import Path
import re, json, shutil, hashlib

root=Path(__file__).resolve().parents[1]
internal=root/'odd/tasks/interno-s8'
internal.mkdir(parents=True,exist_ok=True)
files=[root/'08_plan_riesgos/contenido.tex',root/'LAFROX-Subdocumento8-Anexos.tex',root/'LAFROX-Formulario-T-16.tex',*sorted((root/'08_plan_riesgos').glob('anexo-*.tex')),root/'08_plan_riesgos/figuras/rbs.tex']
snapshot={str(p.relative_to(root)):p.read_text(encoding='utf-8') for p in files}
baseline=root/'tmp/limpieza-s8-base.json'
assert not baseline.exists(), 'No sobrescribir la base de comprobación'
baseline.write_text(json.dumps(snapshot,ensure_ascii=False,indent=2),encoding='utf-8')
shutil.copy2(root/'08_plan_riesgos/anexo-i-trazabilidad.tex',internal/'trazabilidad-y-equivalencias.tex')
for name in ['matriz-cierre-s8.md','prompt-sincronizacion-s8.md','cierre-s8-renumeracion-y-analisis.md']:
 p=root/'odd/tasks'/name
 if p.exists(): shutil.copy2(p,internal/name)
cis=['009','010','023','024','025','026','027','034','035','036','037','038','040','047','048','050']
cimap={f'CI-{old}':f'CT-{i:02d}' for i,old in enumerate(cis,1)}
(internal/'equivalencia-controles.md').write_text('# Coordinación interna: códigos de controles\n\nNo forma parte de los entregables al cliente.\n\n| Código anterior | Código actual |\n|---|---|\n'+'\n'.join(f'| {a} | {b} |' for a,b in cimap.items())+'\n\nLa matriz de observaciones y la equivalencia de riesgos se conservan en trazabilidad-y-equivalencias.tex y matriz-cierre-s8.md. Las referencias al Anexo 8.I de los antecedentes internos deben interpretarse como referencias a este archivo interno; no existe un Anexo 8.I en la edición destinada al cliente.\n',encoding='utf-8')

def paragraphs(text,fn):
 return '\n\n'.join(fn(p) if 'contenido academico' not in p else p for p in text.split('\n\n'))
def replace_start(text,start,new):
 return paragraphs(text,lambda p:new if p.startswith(start) else p)
def remap(text):
 for a,b in cimap.items(): text=text.replace(a,b)
 return text
def save(p,text):
 old=snapshot[str(p.relative_to(root))]
 assert [x for x in old.splitlines() if 'contenido academico' in x]==[x for x in text.splitlines() if 'contenido academico' in x],p
 p.write_text(text,encoding='utf-8')

p=root/'08_plan_riesgos/contenido.tex';s=snapshot[str(p.relative_to(root))]
s=replace_start(s,'Este subdocumento establece',r'''Este plan establece cómo LafroX identificará, valorará y tratará los riesgos de ejecución y operación de la solución para Distribuidora Puelche S.A. durante los 56 meses contractuales. Considera la integridad de los antecedentes sanitarios y comerciales, las dependencias de servicios e infraestructura, la participación de las contrapartes y la preparación de los usuarios. Su propósito es proteger la trazabilidad sanitaria, la continuidad del servicio y los hitos de aceptación mediante decisiones oportunas, responsables definidos y evidencia verificable.

La sección 8.1 define el ciclo de gestión, las responsabilidades y las escalas; la sección 8.2 presenta la RBS, la priorización y el esfuerzo esperado; y la sección 8.3 establece respuestas, reservas y condiciones de aceptación. Los anexos desarrollan las respuestas y dependencias operativas, el fundamento de las estimaciones, los controles técnicos, el análisis FMEA y la evaluación residual. T-16 contiene el registro de los 35 riesgos. Las respuestas y sus efectos posteriores son propuestas de planificación: su eficacia y aceptación requieren la evidencia indicada para cada caso.''')
s=s.replace('; CI-036 tiene $p_0=35\\%$, nivel 3 y factor 0,50','')
s=s.replace('35 riesgos vigentes de T-16','35 riesgos de T-16').replace(', con identificadores vigentes consecutivos','')
s=s.replace('se siguen como CI-009 y CI-010, fuera de T-16','se verifican mediante los controles CT-01 y CT-02 del Anexo 8.E')
s=replace_start(s,r'\textbf{Seguimiento interno y equivalencia.}',r'Los controles técnicos del Anexo 8.E establecen medidas de diseño, pruebas habilitantes, responsables y evidencia de cierre. Una prueba prevista no acredita que el control esté implementado ni que su eficacia haya sido demostrada.')
s=paragraphs(s,lambda x:x.replace(' La retirada de los CI no reduce su valoración.','') if 'retirada de los CI' in x else x)
s=replace_start(s,'La Tabla 8.H.1 concilia',r'La reserva de gestión propuesta es de 160 HH: cuatro ciclos extraordinarios de 40 HH, cada uno con JP 8, ARQ 16, CAL 8 y SRE 8 HH. El Anexo 8.H explicita sus supuestos, límites y sensibilidad, y distingue esta capacidad de decisión de la contingencia específica y de las 3.072 HH protegidas para E1. Su utilización requiere autorización; no representa trabajo consumido ni financiamiento aprobado.')
s=replace_start(s,'Las Tablas 8.H.2--3 distribuyen',r'Las Tablas 8.H.2--3 distribuyen prevención y contingencia por mes y perfil. La gestión se reserva como capacidad de decisión en los bloques 1--12, 13--20, 21--38 y 39--56. El crédito demostrado contra las 3.072 HH es inicialmente cero hasta verificar la coincidencia de paquete, perfil y mes; esa protección no se suma nuevamente ni se utiliza en E2. La programación requiere nivelación de capacidad y autorización de la línea base, manteniendo la misma distribución mensual para su valoración económica. Las HH no se convierten directamente en días y se preservan las cuatro semanas finales de evidencia.')
save(p,s)

p=root/'LAFROX-Subdocumento8-Anexos.tex';s=snapshot[str(p.relative_to(root))]
s=s.replace('Anexos 8.A--8.I','Anexos 8.A--8.H')
s=s.replace('Este documento reúne los anexos vigentes','Este documento reúne los anexos')
s=s.replace('35 riesgos vigentes, con ID vigentes consecutivos, con descripciones, disparadores y responsables alineados con el T-16','35 riesgos, con sus disparadores y responsables')
for suffix in [' Evidencia y detalle: Tabla 8.A.2.',' Evidencia y coordinación: Tabla 8.A.2.',' Plazos completos y HH: 8.F.1; residual: 8.F.2.']:
 s=s.replace(suffix,'')
s=replace_start(s,'Esta matriz desarrolla la coordinación',r'Esta matriz establece los compromisos de coordinación de los 28 riesgos que requieren insumos o decisiones del CLIENTE. La contraparte aporta antecedentes y decide dentro de su autoridad; LafroX conserva la responsabilidad de diseño, capacidad, seguridad y mantenimiento. La gestión de servicios externos, suministros, siniestros y cambios normativos se realiza mediante las respuestas específicas de la Tabla 8.A.1. Los plazos de coordinación se proponen para acuerdo en el arranque; no acreditan respuestas recibidas ni modifican las obligaciones contractuales.')
s=s.replace('Este anexo estima exposición de esfuerzo para los 35 riesgos vigentes de T-16, con ID vigentes consecutivos. Los 16 asuntos internos CI están excluidos de la exposición del CLIENTE y no constituyen reserva del CLIENTE.','Este anexo estima la exposición de esfuerzo de los 35 riesgos de T-16.')
s=s.replace('Hipótesis de la ampliación y control de doble conteo','Hipótesis de ocurrencia y esfuerzo')
s=s.replace('los ocho riesgos vigentes añadidos desde R-028','los riesgos R-028--R-035')
s=s.replace('de los nuevos riesgos. Fuente:','de R-028--R-035. Fuente:')
s=replace_start(s,'R-017 se revisa de',r'R-017 adopta $p_0=25\%$ por la exposición inicial de Concepción con un enlace sin respaldo verificado y la falla del último camino utilizable hasta mes 56. Es una hipótesis, no una frecuencia inferida del caso ni de los cortes de Talca. Se estiman ocho episodios condicionados, escenarios acumulados 24/48/144 HH, PERT de 60 HH y VE de 15 HH. R-014 adopta $p_0=20\%$ y un impacto de nivel 4 por la consecuencia R18-16 y la jubilación dentro del horizonte; el evento incierto es la transferencia insuficiente de conocimiento, no el retiro conocido.')
s=s.replace('Revisión del Informe 2, S8, análisis 8.2; S4, plataforma declarada; S7, 8.2.5.','S4, plataforma declarada; S7, 8.2.5.')
s=s.replace('Revisión del Informe 2, S8, análisis 8.2; S4, servicios gestionados; S7, 8.1.4 y fase 9.','S4, servicios gestionados; S7, 8.1.4 y fase 9.')
s=s.replace('Brecha B-S4-02; Caso,','Caso,')
s=s.replace('la base y las revisiones de estimación','el fundamento de la estimación')
start=s.index('\\clearpage\n\\section{Anexo 8.D:')
end=s.index('\\input{08_plan_riesgos/anexo-e-controles.tex}',start)
dependencies=[
('Piloto INN-01 / CT-08','Validar catálogo con Comercial/Calidad en meses 7--9. El paquete abarca 11--15; H5 corresponde a 11--12 y el piloto real a 13--15.','DAT dirige; IMP coordina; CAL verifica.','I-01A en mes 15: al menos 70\\% de aciertos sobre al menos 100 avisos evaluables. Sin cumplimiento, no ampliar a otras rutas; mantener avisos informativos y alcance obligatorio.'),
('Identidad / CT-15','Distinguir manifiesto de 26 h, caché de 24 h y credenciales de 8/14 h; no autorizar por omisión ante pérdida de identidad central.','SEG responde; ARQ diseña; SRE ejecuta con TI/Operaciones.','AL-OFF-01 antes de H5/H10: corte de 24 h y relevos de 8/16 h, expiración, denegación, revocación y reconciliación. CAL bloquea el flujo fallido.'),
('Emisión ERP / R-034','El ERP del CLIENTE es el único emisor y no se modifica. La pérdida de Talca bloquea nuevas guías hasta recuperar el ERP; sólo se usan guías válidas ya emitidas. R-008 trata la confirmación externa del SII.','ARQ coordina; SRE ejecuta con TI y Operaciones.','AL-DTE-01 y AL-DR-01 antes de H5/H10: demostrar frontera de emisión y recuperación; RTO de 4 h y RPO de 15 min. No simular disponibilidad del ERP mediante otro emisor.'),
('Stock / CT-16','Conciliar UUID/sitio y excluir al escritor anterior antes de promover otra autoridad. Mantener capturas pendientes sin confirmar stock global con una copia vencida.','DAT hasta mes 21; SRE desde 22; ARQ diseña; CAL verifica.','AL-STOCK-01/AL-DR-01 antes de H5/H10: pérdida central, promoción, retorno y conciliación sin doble reserva. R-004 corresponde al inventario inicial y R-017 a la conectividad externa.'),
('Pagos y servicios externos / CT-01--02','Consultar estado antes de reintentar pagos y conciliar con clave idempotente. Ante caída de mapas, usar sólo rutas autorizadas disponibles y mantener nuevas consultas pendientes.','ARQ diseña; DES/SRE ejecutan; CAL verifica.','Pruebas de timeout antes y después del cargo, reenvío, caída y recuperación antes de H5/H10. Imputar un mismo corte WAN una sola vez a su causa principal.'),
('Conocimiento de rutas / R-014','Transferir conocimiento en meses 1--3 y verificar fecha V-14 de retiro. La prueba debe prescindir de la intervención del planificador.','IMP con Operaciones y planificador; CAL verifica.','Prueba de planificación en meses 13--15 sin el planificador. Conservar evidencia del resultado R18-16 y escalar conocimiento no transferido antes de habilitar autonomía.'),
('Enlaces / R-017','Verificar respaldo recibido en Concepción antes de aceptar la ola. Talca/Concepción: fibra y LTE, Starlink en espera caliente. Cross-docking: Starlink y LTE Entel/Claro; conmutación menor a 30 s.','SRE con TI/Operaciones; CAL verifica recepción.','Recepción antes de H3 y aceptación ampliada antes de H5. Ensayar pérdida del último camino Starlink de madrugada en Los Ángeles. La ventana local de 3 h no reduce la autonomía exigida de 24 h.'),
('Energía / R-018','Distinguir autonomía de UPS de 30 min de continuidad de Talca de 24 h; la autonomía de un componente no demuestra la de todo el servicio.','SRE con TI/Operaciones; CAL verifica.','Ensayar pérdida de suministro, transferencia, continuidad y restitución antes de aceptación. Registrar medición por componente y servicio; no acreditar autonomía sin evidencia.'),
('Autorizaciones / R-016, R-019','La aprobación previa de residencia de datos es distinta de la decisión de promover durante un incidente. El silencio no aprueba una transferencia ni una promoción.','JP y ARQ; titular y suplente autorizados del CLIENTE.','Durante promoción regional, si el titular no responde en 15 min, decide el suplente dentro del máximo de 30 min. Validar residencia antes de habilitar transferencia; conservar actas y evidencia.'),
('Cobertura interior','Comprobar cobertura RF en cámaras reales con terminales, puertas y ocupación representativos; el número preliminar de AP no acredita cobertura.','ARQ/SRE con TI y Jefa de Bodega; CAL verifica.','Estudio y prueba antes de aceptar la instalación; corregir diseño y repetir si falla. La cobertura interior es una condición de instalación distinta del enlace WAN y de la asociación lote--sensor.'),
('Redundancia física','Verificar pares de firewall, nodos, discos y switches, junto con autoridad de escritura, recuperación y capacidad efectiva.','ARQ diseña; SRE ejecuta; CAL verifica.','Antes de aceptar infraestructura, inyectar fallas y registrar conmutación y restitución. La redundancia declarada no reemplaza la prueba del servicio ni permite doble escritor.'),
('Rotación nocturna / R-029','El 38\\% es rotación anual, no probabilidad del evento. Mantener inducción continua en meses 13--56, turno 22:00--06:00, aprendizaje máximo de dos horas y evaluación previa al trabajo autónomo.','IMP hasta mes 21; SRE desde 22; Jefa de Bodega y Operaciones aportan tutor y cobertura.','Verificar competencia de cada reemplazo y capacidad de tutoría; impedir trabajo autónomo no certificado. No imputar otra vez las HH ordinarias de capacitación ni confundir rotación con ausencia a sesiones o resistencia individual.'),
('Recuperación regional','Distinguir objetivo de recuperación de 75 min (15+60) del máximo sanitario de 2 h; no consumir ese margen como disponibilidad autorizada.','SRE ejecuta; ARQ valida frontera; Calidad del CLIENTE decide aspectos sanitarios.','Pruebas AL-OFF-01, AL-DTE-01 y AL-DR-01, con 96 salidas válidas, antes de H5/H10 y semestralmente. Medir tiempos, integridad y condiciones de reanudación por procedimiento.'),
('Cierre bajo peak / R-031, CT-14','Acordar continuidad, usuarios y congelamiento antes del mes 19; mantener seguimiento diario del cierre E2 en meses 19--20. Separar coordinación del cierre de verificación técnica de capacidad.','JP con Contraparte Técnica/Operaciones; SRE y ARQ verifican capacidad.','Comprobar carga por ventana y dependencia, incluido ERP, antes de H5/H10 y preparación del peak. Preservar las cuatro semanas finales de evidencia y elevar refuerzo o cambio antes del hito.'),
('Telemetría / R-028','Acordar finalidades, acceso y controles con Operaciones, TI y sindicato antes de incorporar cada ola; sin cámaras en cabina ni control de jornada no acordado.','JP e IMP con las contrapartes funcionales; SEG verifica privacidad.','Acta previa a la ola, prueba de controles y restricción de usos no acordados. Diferenciar el desacuerdo institucional de la adopción individual; conservar evidencia de decisión.')]
d=r'''\clearpage
\section{Anexo 8.D: Dependencias operativas y continuidad}
Las condiciones siguientes delimitan la operación, las decisiones y las pruebas habilitantes. Los responsables deben verificar la evidencia antes de autorizar el alcance afectado; describir un control no demuestra su ejecución ni acredita eficacia residual. Los meses se cuentan desde el inicio contractual. Las referencias R identifican riesgos; CT-01--CT-16 identifican controles técnicos. CT sin número designa la Contraparte Técnica.

\begingroup
\renewcommand{\thetable}{8.D.1}
\begin{landscape}
\setlength{\textwidth}{\linewidth}
\renewcommand{\arraystretch}{1.08}
\begin{tablalafrox}{Dependencias operativas, decisiones y condiciones de continuidad. Fuente: requisitos de operación del Caso 02; arquitectura, procedimientos de continuidad y programa de implantación.}{tab:sd8-dependencias-operativas}{F{0.14} Y F{0.19} F{0.31}}{\cab{Ámbito} & \cab{Condición operativa} & \cab{Responsable y contraparte} & \cab{Momento, evidencia y decisión}}
'''
d+='\n'.join(' & '.join(row)+r' \\' for row in dependencies)
d+='\n'+r'''\end{tablalafrox}
\end{landscape}
\endgroup

'''
s=s[:start]+d+s[end:]
s=s.replace('\\input{08_plan_riesgos/anexo-i-trazabilidad.tex}\n','')
s=re.sub(r'\\emph\{Correo principal: aclaraciones de la licitación\}[^\n]*\n','',s)
s=re.sub(r'\\emph\{Primera revisión del Informe 2:[^\n]*\n','',s)
s=remap(s)
s=s.replace('CT-14, CT-15 y CT-16 son controles internos y quedan fuera de esta suma.','Los controles técnicos se realizan dentro del trabajo ordinario y no se presupuestan nuevamente como contingencia.')
save(p,s)

p=root/'08_plan_riesgos/anexo-e-controles.tex';s=snapshot[str(p.relative_to(root))]
s=s.replace('Controles internos y destinos documentales','Controles técnicos preventivos')
s=replace_start(s,'Los 16 asuntos retirados',r'Los controles CT-01--CT-16 establecen obligaciones de diseño, innovación y calidad de LafroX. Cada ficha define una solución técnica, su responsable y la evidencia necesaria para verificarla. Las pruebas y medidas descritas son requisitos de habilitación; no se presentan como ejecutadas ni aprobadas. CT sin número designa la Contraparte Técnica.')
s=replace_start(s,'CAL verifica evidencia',r'CAL verifica la evidencia y JP controla el cierre. Desde el mes 22 SRE asume las responsabilidades operativas de las familias DAT, DES e IMP conforme a la Tabla 8.1. No se promueve un flujo con defectos críticos o altos abiertos ni con pruebas habilitantes fallidas. Una función opcional que no supere sus pruebas permanece deshabilitada y se conserva el alcance obligatorio.')
s=s.replace('Controles internos: solución propuesta, destino y verificación. Fuente: revisión del Informe 2 y secciones S4/S9/S13 indicadas; diseño documental propuesto.','Controles técnicos: solución, responsable y verificación. Fuente: requisitos de arquitectura, seguridad, innovación y calidad de la solución.')
s=s.replace('Dueño y destino a sincronizar','Responsable')
lines=[]
for line in s.splitlines():
 if line.startswith('CI-'):
  cols=line.split(' & ')
  cols[1]=re.split(r' S(?:4|9|13),',cols[1],maxsplit=1)[0]
  line=' & '.join(cols)
 lines.append(line)
s=remap('\n'.join(lines)+'\n')
s=s.replace('No trasladar al CLIENTE un control omitido.','Corregir hallazgos antes de promover.')
s=s.replace('Conservar el piloto bajo seguimiento interno.','Registrar los resultados del piloto.')
s=s.replace('Corregir/repetir sin presentar el fracaso de diseño como riesgo del CLIENTE.','Corregir y repetir antes de habilitar.')
s=s.replace('Una disponibilidad pendiente del IdP elegido no se transfiere al CLIENTE.','La habilitación requiere evidencia de continuidad y revocación.')
save(p,s)

p=root/'08_plan_riesgos/anexo-f-respuestas.tex';s=snapshot[str(p.relative_to(root))]
s=s.replace('La matriz de integración debe contrastarlos con los paquetes existentes antes de aprobarlos','JP debe contrastar estos esfuerzos con los paquetes existentes antes de aprobarlos')
s=s.replace('ya incluidos en S7','incluidos en el presupuesto ordinario')
s=s.replace('Las ventanas y rangos de p0/O/M/P se conservan.','La base p0/O/M/P corresponde a las ventanas de exposición del Anexo 8.B.')
save(p,s)

p=root/'08_plan_riesgos/anexo-h-reservas.tex';s=snapshot[str(p.relative_to(root))]
s=s.replace('Reservas, perfiles y propuesta de integración al cronograma','Reservas, perfiles y programación del esfuerzo')
s=replace_start(s,'La exposición inicial de 35 riesgos',r'La exposición inicial de los 35 riesgos es de 1.183,11 HH, calculada con las probabilidades y los esfuerzos condicionales del Anexo 8.B. Los controles técnicos de diseño, innovación y calidad forman parte del trabajo ordinario; una diferencia de esfuerzo requiere estimación y aprobación específica.')
s=s.replace('Se sustituye la cifra de gestión de 1.600 HH sin derivación por una propuesta de escenario de 160 HH, sin afirmar autorización:','La reserva de gestión propuesta es de 160 HH, sujeta a autorización:')
s=s.replace('tareas CI','controles técnicos ordinarios')
s=s.replace('No es 10\\% de 1.600 ni una probabilidad derivada de FMEA.','No es una probabilidad derivada de FMEA.')
s=s.replace('S7/T-15 debe recalcular la ruta crítica y nivelar perfiles antes de aceptarla','JP debe recalcular la ruta crítica y nivelar perfiles antes de solicitar su aprobación')
s=s.replace('Base p0/O/M/P intacta;','Valoración previa al tratamiento;')
s=s.replace('Cuatro escenarios de 40 HH; reemplaza propuesta histórica sin derivación.','Cuatro ciclos extraordinarios de 40 HH, con perfiles y bloques definidos.')
s='\n'.join(x for x in s.splitlines() if not x.startswith('Estimación interna histórica excluida'))+'\n'
s=s.replace('; todavía no incorporada en T-15','')
idx=s.index('\\paragraph{Integración externa requerida.}')
s=s[:idx]+r'''\paragraph{Programación y autorización.} JP asigna las fichas preventivas y la contingencia a los paquetes de migración/datos, implantación, integración, soporte, gobierno o salida que atienden cada evento. Antes de autorizar capacidad adicional debe verificar paquete, perfil, mes y capacidad existente, descontando toda coincidencia. La prevención se programa en el mes de primera atención y antes del hito dependiente; la contingencia se nivela con la distribución mensual propuesta. Las 3.072 HH protegidas mantienen su uso exclusivo en E1. Los ciclos de gestión se sitúan en los meses 1, 13, 21 y 39 como capacidad de decisión; sólo se consumen ante un asunto emergente autorizado. Las familias DAT/IMP conservan su clasificación de esfuerzo y SRE asume responsabilidad desde mes 22, sin duplicar cargas por relevo.

La programación está sujeta a nivelación y autorización de la línea base. JP verifica precedencias, holguras y ruta crítica, preservando congelamientos y las cuatro semanas finales de evidencia. Si la capacidad no permite cumplir, eleva refuerzo o cambio antes del hito, sin desplazarlo unilateralmente. La valoración económica utiliza la misma diferencia aprobada por mes y perfil, multiplicada por la tarifa neta validada; no se incorporan precios en este plan. Gestión y protección no se registran como costo consumido por el solo hecho de reservarlas. JP presenta la conciliación al arranque, la actualiza en cada comité quincenal y antes de H5/H10; el Comité Ejecutivo autoriza los cambios y CAL verifica la ausencia de doble imputación. Una propuesta de reserva no acredita financiamiento aprobado.
'''
save(p,s)

p=root/'LAFROX-Formulario-T-16.tex';s=snapshot[str(p.relative_to(root))]
s=replace_start(s,'El registro sigue el formato',r'''El registro contiene los 35 riesgos de la propuesta y sigue el Formulario T-16 de las Bases Administrativas (p. 63), ISO 31000 (ISO, 2018) y RT-19.04 de las Bases Técnicas Transversales (cap. 19, p. 33). Las condiciones de origen corresponden al Caso 02, capítulos 10 y 19. Prob. presenta el nivel y factor derivados de $p_0$ del Anexo 8.B mediante las bandas de la Tabla 8.2. Impacto presenta el mayor nivel por esfuerzo condicional, plazo, alcance, calidad sanitaria o consecuencias contractuales, justificado por ID en el Anexo 8.C. Exposición es $q_P\times q_I$; la zona se obtiene de los umbrales de la Tabla 8.4. Son juicios de planificación, no frecuencias observadas ni costos monetarios.

La Tabla 8.A.1 detalla los disparadores; la Tabla 8.A.2 establece contraparte, solicitud, evidencia, plazo y contingencia para las 28 dependencias del CLIENTE. CT significa Contraparte Técnica; D es la fecha de la actividad indicada y D-10/D-5 son días hábiles anteriores. Los plazos propuestos de coordinación no modifican la recepción formal. Cada responsable dirige su equipo; desde el mes 22 SRE asume las responsabilidades operativas de DAT e IMP, manteniendo sus familias de esfuerzo. Las fichas ejecutables, sus plazos, esfuerzo, contingencias y condiciones de habilitación están en 8.F.1; la evidencia de la valoración posterior proyectada, en 8.F.2, resumida en T-16.2. El Anexo 8.H presenta la propuesta de reservas y sus condiciones de programación y autorización. Ninguna proyección acredita eficacia comprobada ni capacidad o financiamiento aprobados.''')
s=s.replace('Fuente: contenido de licitación y subdocumentos anteriores','Fuente: análisis de riesgos de la solución y requisitos de licitación')
s=s.replace(' Plazos, HH y contingencia: 8.F.1; residual proyectado: 8.F.2.','')
s=s.replace('{G{0.08} G{0.11} G{0.11} G{0.13} F{0.14} Y}{\\cab{ID vigente} & \\cab{p1} & \\cab{I1 / factor} & \\cab{E1 / zona} & \\cab{Dueño} & \\cab{Evidencia y tratamiento}}','{G{0.12} G{0.15} G{0.20} G{0.27} Y}{\\cab{ID} & \\cab{p1} & \\cab{I1 / factor} & \\cab{E1 / zona} & \\cab{Dueño}}')
s=re.sub(r' & Evidencia y revisión: 8\.F\.2; ficha ejecutable y plan adicional cuando E1 es alta/crítica: 8\.F\.1\.', '', s)
save(p,s)

# El material de coordinación queda fuera de los inputs de publicación.
(root/'08_plan_riesgos/anexo-i-trazabilidad.tex').unlink()
(root/'tmp/limpieza-s8-build').mkdir(exist_ok=True)
print('Limpieza editorial aplicada. Material interno:',internal)
