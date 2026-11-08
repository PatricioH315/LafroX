from pathlib import Path
root=Path(__file__).resolve().parents[1]
changes={
'08_plan_riesgos/anexo-e-controles.tex':{
'Los 16 asuntos retirados':'Los controles CT-01--CT-16 establecen obligaciones de diseño, innovación y calidad de LafroX. Cada ficha define una solución técnica, su responsable y la evidencia necesaria para verificarla. Las pruebas y medidas descritas son requisitos de habilitación; no se presentan como ejecutadas ni aprobadas. CT sin número designa la Contraparte Técnica.'},
'08_plan_riesgos/anexo-h-reservas.tex':{
'La exposición inicial de 35 riesgos':'La exposición inicial de los 35 riesgos es de 1.183,11 HH, calculada con las probabilidades y los esfuerzos condicionales del Anexo 8.B. Los controles técnicos de diseño, innovación y calidad forman parte del trabajo ordinario; una diferencia de esfuerzo requiere estimación y aprobación específica.'},
'08_plan_riesgos/contenido.tex':{
'El registro del CLIENTE contiene':'El registro contiene 1 riesgo crítico, 14 altos, 15 medios y 5 bajos. R-002 tiene E=0,56 y zona Crítica. La Tabla 8.5 selecciona diez por producto y desempata por ID, sin sustituir el conjunto de riesgos altos. La valoración posterior proyectada y el plan adicional se presentan en 8.F; el análisis FMEA de los 15 riesgos altos y críticos iniciales se desarrolla en 8.G.'}}
for name,mapping in changes.items():
 p=root/name;s=p.read_text(encoding='utf-8');lines=s.splitlines()
 for i,line in enumerate(lines):
  for prefix,replacement in mapping.items():
   if line.startswith(prefix): lines[i]=replacement
 s='\n'.join(lines)+'\n'
 if name.endswith('contenido.tex'):
  s=s.replace('35 riesgos del registro vigente, con ID vigentes consecutivos','35 riesgos del registro')
  s=s.replace(', vinculada a B-S4-02','')
 p.write_text(s,encoding='utf-8')
print('Ajustes de introducciones y referencias completados.')
