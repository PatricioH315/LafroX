from pathlib import Path
import json,re
r=Path(__file__).resolve().parents[1]
d=json.loads((r/'tmp/cierre-s8-datos.json').read_text(encoding='utf-8'))
p=r/'08_plan_riesgos/anexo-e-controles.tex';s=p.read_text(encoding='utf-8')
s=s.replace('sigue en R-044.','sigue en '+d['mapping']['R-044']+'.').replace('R-004 y R-019 conservan','R-004 y '+d['mapping']['R-019']+' conservan')
p.write_text(s,encoding='utf-8')
p=r/'LAFROX-Subdocumento8-Anexos.tex';s=p.read_text(encoding='utf-8')
s=s.replace('CI-034 (antes CI-034)','CI-034 (histórico R-034)').replace('CI-009 (antes CI-009)','CI-009 (histórico R-009)')
s=s.replace('exposición de esfuerzo pendiente de conciliación en la tarea de reservas','exposición inicial de esfuerzo conciliada con la proyección y reservas propuestas de 8.H')
# La historia de CI no se convierte en la clave vigente que coincida por número.
s=s.replace('CI-048 se incorporó en tarea 5','El asunto de identidad se incorporó en tarea 5').replace('CI-050 se incorporó en tarea 5','El asunto de consolidación se incorporó en tarea 5')
s=s.replace('LafroX SpA. (2026c).', 'LafroX SpA. (2026c).')
s=s.replace('\\emph{Primera revisión del Informe 2:', '\\emph{Correo principal: aclaraciones de la licitación}. (s.f.). Punto 1.b, trazabilidad de observaciones.\n\n\\emph{Primera revisión del Informe 2:')
p.write_text(s,encoding='utf-8')
p=r/'08_plan_riesgos/anexo-i-trazabilidad.tex';s=p.read_text(encoding='utf-8')
s=s.replace('``Tabla de trazabilidad observación--respuesta--sección modificada\'\'', '``Tabla de trazabilidad de observación, respuesta y sección modificada\'\'')
# Guardar el pedido textual en tabla, con espacios que permitan composición.
s=s.replace('Los que mantienen E alta/crítica reciben plan adicional, plazo, dueño y bloqueo; no se rebaja I sanitario o contractual sin fundamento. & 8.F.1--2; 8.G.1. & corregido en S8', 'Los que mantienen E alta/crítica reciben plan adicional, plazo, dueño y bloqueo; no se acredita todavía un nivel manejable ni se rebaja I sanitario o contractual sin fundamento. & 8.F.1--2; 8.G.1. & parcial')
p.write_text(s,encoding='utf-8')
