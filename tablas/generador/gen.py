from pathlib import Path
import json,re
from comun import tex,tabla,fila
from datos_rt import cargar
from datos_registros import DECISIONES,REGLAS,grupos
ROOT=Path(__file__).resolve().parents[3]
OUT=Path(__file__).resolve().parents[1]
D=json.loads(Path(__file__).with_name('consolidado.json').read_text(encoding='utf8'))
def note(what,need): return '\\par\\noindent\\textbf{Nota de trabajo:} '+tex(what)+'. Para completarlo se requiere '+tex(need)+'.\\par\n'
def put(name,title,headers,rows,widths,source,extra=''):
 label='tab:'+name.replace('_','-')
 out='%% Generado por gen.py desde consolidado.json y las Bases.\n'
 out+='La Tabla~\\ref{'+label+'} presenta '+tex(title.lower())+'.\\par\n'
 out+=tabla(tex(title)+'. Fuente: '+tex(source)+'.',label,widths,headers,[fila([tex(v) for v in row]) for row in rows])
 out+=extra
 (OUT/(name+'.tex')).write_text(out,encoding='utf8')
def generate():
 verified=[x for x in D['rf'] if x['desc']]
 pending=[x for x in D['rf'] if not x['desc']]
 put('anx_rf','Requerimientos funcionales con desarrollo respaldado',['ID','Descripción y actor','Precondición','Resultado','Prioridad / etapa','Origen'],[[x['id'],x['desc']+' Actor: '+x['actor'],x['pre'],x['res'],x['prio']+' / '+x['etapa'],x['origen']] for x in verified],'L{1.65cm} Y L{3.1cm} L{3.6cm} L{1.7cm} L{4.4cm}','Bases del caso y SD2, anexo 2.1',note('La descomposición es parcial; las etapas vacías no están asignadas','cerrar las materias del registro siguiente y la correspondencia del catálogo'))
 put('anx_rf_vacios','Identificadores RF conservados sin desarrollo adoptado',['ID','Materia del catálogo de trabajo','Descripción','Etapa','Prioridad'],[[x['id'],x['titulo'],'','',''] for x in pending],'L{1.8cm} Y L{4cm} L{1.6cm} L{1.6cm}','inventario previo del SD3; no constituye compromiso',note('Estos identificadores conservan su materia, pero no un requisito aprobado','contrastar cada materia con las Bases y completar actor, precondición, resultado, origen y prioridad'))
 put('anx_correspondencia','Correspondencia entre RF resumidos del SD2 y RF detallados del SD3',['RF del SD2','RF del SD3 con desarrollo respaldado','Etapa SD2','Prioridad SD2'],D['mapping'],'L{2cm} Y L{2.5cm} L{3cm}','SD2, anexo 2.1; consolidación del SD3',note('RF-05 y RF-09 del SD2 aún no tienen una correspondencia detallada validada; los demás enlaces son parciales','descomponer cross-docking y acuse tributario, y revisar cobertura completa sin reutilizar identificadores con otro significado'))
 put('anx_rnf','RNF con umbral respaldado',['ID','Materia','Umbral','Método de verificación','Origen'],[[x['id'],x['titulo'],x['umbral'],x['metodo'],x['origen']] for x in D['rnf'] if x['umbral']],'L{1.8cm} L{4cm} Y L{4cm} L{5cm}','Bases y SD2',note('Los métodos vacíos todavía no constituyen pruebas diseñadas','definir procedimiento, datos, instrumento y evidencia'))
 put('anx_rnf_vacios','Identificadores RNF sin umbral adoptado',['ID','Materia del catálogo de trabajo','Umbral','Método'],[[x['id'],x['titulo'],'',''] for x in D['rnf'] if not x['umbral']],'L{2cm} Y L{4cm} L{4cm}','inventario previo del SD3; no constituye compromiso',note('No se trasladan cifras del catálogo previo sin contraste','documentar umbral, fuente exacta, método y etapa por requerimiento'))
 put('anx_supuestos','Supuestos y decisiones pendientes de completar',['ID','Materia','Contenido respaldado','Fuente del contenido','Nota de trabajo: falta completar'],D['supuestos'],'L{1cm} L{3.3cm} Y L{4.1cm} L{6cm}','registro previo; SD2 y Bases para las decisiones expresamente desarrolladas',note('Los campos vacíos no representan decisiones adoptadas ni conformidad del CLIENTE','resolver cada decisión del numeral 16.1 y los supuestos adicionales'))
 put('anx_exclusiones','Exclusiones explícitas',['ID','Exclusión'],D['exclusiones'],'L{1.8cm} Y','Caso, cap. 11')
 put('anx_restricciones','Restricciones del caso',['ID','Restricción','Origen'],D['restricciones'],'L{1.6cm} Y L{4cm}','Caso, cap. 10',note('La interpretación de las restricciones no define una arquitectura implementada','completar diseño y evidencia respetando estas condiciones'))
 put('anx_decisiones','Registro de decisiones de alcance y diseño',['ID','Materia','Decisión','Fundamento'],DECISIONES,'L{1.3cm} L{5cm} Y L{6cm}','registro de decisiones y Bases',note('Las decisiones son propuestas de la oferta; su aceptación se verifica en la instancia de gobierno correspondiente','conservar la evidencia de validación y sus efectos en la planificación'))
 put('anx_reglas','Registro de reglas de negocio',['ID','Materia','Qué y dónde se captura','Quién decide','Consecuencia y RF'],REGLAS,'L{1.4cm} L{4.3cm} Y L{4cm} L{5cm}','Caso, cap. 16.1 y 17.1; reglas_de_negocio.md',note('Cada regla debe validarse durante el levantamiento y mantenerse configurable cuando dependa de un parámetro comercial o sanitario','registrar la evidencia de esa validación'))
 put('anx_vacios','Vacíos e inconsistencias para revisión',['ID','Materia','Nota de trabajo: evidencia requerida'],D['vacios_revision'],'L{1.5cm} Y L{10cm}','contraste de Bases, SD2 y SD3')
 put('anx_grupos','Participación de los 19 actores consolidados',['Actor','Participación coherente con SD2','Momento','Responsable','Indicador'],grupos(D['actores']),'L{4cm} Y L{2.7cm} L{2.7cm} L{3.3cm}','SD2, sección 2.4 y anexo 2.3',note('Las actividades se detallan durante el inicio y cada ola; los indicadores se revisan en comité de proyecto','conservar minutas, asistencia y resultados de adopción'))
 put('anx_r18','Resultados de aceptación exigidos por el caso',['ID','Resultado exigido','Situación actual','Meta propia','Momento / método'],[[*x,'',''] for x in D['r18']],'L{1.7cm} Y L{5cm} L{2cm} L{4cm}','Caso, cap. 18, p. 35',note('Los límites expresos del caso se conservan; las metas a cargo del proponente y la verificación aún están vacías','fijar OTIF, envases y ocupación, así como momento y protocolo de medición por resultado'))
 put('anx_glosario','Siglas utilizadas',['Sigla','Significado'],[['RF','Requerimiento funcional; los RF-01 a RF-14 del SD2 son resúmenes, no equivalen por número a las épicas del SD3.'],['RNF','Requerimiento no funcional.'],['RT','Requisito codificado de las Bases Técnicas Transversales.'],['ERP','Sistema de gestión empresarial conservado como registro contable y emisor tributario.'],['WMS','Sistema de gestión de almacenes.'],['FEFO','Primero en vencer, primero en salir.'],['OTIF','Entregas completas y a tiempo; su regla de cómputo aún debe cerrarse.'],['POD','Prueba de entrega.'],['EDI','Intercambio electrónico estructurado de documentos.'],['RTO / RPO','Objetivos de tiempo de recuperación y pérdida de datos admisible.']],'L{2.4cm} Y','terminología de las Bases y SD2')
 # No se genera ninguna asignación arquitectónica, de EDT, prueba o cumplimiento.
 put('t12_caso','Parte A: estado de respuesta RF y RNF',['ID','Requerimiento / materia','Cumple','Componente','EDT','Prueba','Sección','Criterio','Origen respaldado'],[[x['id'],x.get('desc') or x.get('umbral') or 'Materia sin desarrollar: '+x['titulo'],'','','','','','',x['origen']] for x in D['rf']+D['rnf']],'L{1.8cm} Y L{1.25cm} L{1.7cm} L{0.9cm} L{1.25cm} L{1.25cm} L{1.25cm} L{4.3cm}','catálogo de trabajo contrastado',note('La descripción respaldada no demuestra cumplimiento ni trazabilidad completa','revisar arquitectura del Subdocumento 4, EDT del Subdocumento 7 y pruebas del T-13; completar también criterio de aceptación por requerimiento'))
 rt=cargar(); groups={}
 for x in rt: groups.setdefault(x['id'][3:5],[]).append(x)
 out=''
 for cap,items in groups.items():
  label='tab:rt-'+cap
  out+='Los requisitos del capítulo '+cap+' se reproducen en la Tabla~\\ref{'+label+'}.\\par\n'
  out+=tabla('Requisitos transversales, capítulo '+cap+'. Fuente: Bases Técnicas Transversales.',label,'L{1.8cm} Y L{2cm} L{1.4cm} L{2.2cm} L{1.5cm} L{2cm}',['Código','Exigencia','Carácter','Cumple','Componente','Sección','Evidencia'],[fila([tex(x['id']),tex(x['desc'].replace('**','')),tex(x['car']),'','','','']) for x in items])
 (OUT/'t12_rt.tex').write_text(out,encoding='utf8')
 print('Generados:',len(verified),'RF desarrollados;',len(pending),'RF sin desarrollo;',sum(bool(x['umbral']) for x in D['rnf']),'RNF con umbral;',len(rt),'RT sin cumplimiento automático')
if __name__=='__main__': generate()
