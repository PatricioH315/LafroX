from pathlib import Path
import json,re
r=Path(__file__).resolve().parents[1]
d=json.loads((r/'tmp/tarea6-datos.json').read_text(encoding='utf-8'))
p=r/'LAFROX-Subdocumento8-Anexos.tex';a=p.read_text(encoding='utf-8')
a='\n'.join(l for l in a.split('\n') if not any(l.startswith(k+' / ') for k in d['internal']))
a=a.replace('para cada riesgo R-001--R-051 del registro vigente','para cada uno de los 35 riesgos vigentes, con sus ID originales discontinuos')
a=a.replace('y R-041--R-051.', 'y R-041--R-046, R-049 y R-051.')
a=a.replace('Los 13 riesgos internos señalados en la revisión inicial conservan su tratamiento hasta revisar su ubicación; la coordinación de las nuevas entradas tampoco transfiere los controles técnicos de LafroX al CLIENTE.', 'Los trece asuntos internos señalados por la revisión, más los tres reclasificados en esta etapa, se siguen en 8.E fuera de esta matriz; la coordinación de los riesgos vigentes no transfiere los controles técnicos de LafroX al CLIENTE.')
a=a.replace('corrección técnica de una saturación pertenece a R-047.', 'corrección técnica de una saturación pertenece a CI-047 (8.E).')
a=a.replace('los mismos 51 eventos del T-16.', 'los mismos 35 eventos vigentes del T-16; los impactos históricos internos se archivan en 8.E.3.')
p.write_text(a,encoding='utf-8')
p=r/'08_plan_riesgos/contenido.tex';b=p.read_text(encoding='utf-8').replace('de las hallazgos','de los hallazgos').replace('entre los 51,','entre los 35,')
p.write_text(b,encoding='utf-8')
p=r/'08_plan_riesgos/anexo-e-internos.tex';e=p.read_text(encoding='utf-8').replace('coordinación de CI-044.','coordinación de R-044.').replace('corte de CI-004.','corte de R-004.')
p.write_text(e,encoding='utf-8')
