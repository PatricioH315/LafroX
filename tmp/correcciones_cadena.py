from pathlib import Path

p=Path('LAFROX-Formulario-T-12.tex')
rows=p.read_text(encoding='utf8').splitlines(keepends=True)
changes={
 'RF-01.11': [('M2 Inventario (servicio de recepción y aplicación de bodega)', 'M2 Inventario (servicio de inventario y aplicación de bodega)')],
 'RF-03.03': [('M3 confirma reservas en el servidor central, ordenadas por recepción en ese servidor y sin depender del ERP', 'M3 solicita la reserva y confirma el pedido solo después del acuse durable de la retención; M2 central ordena las solicitudes por recepción y mantiene la reserva sin depender del ERP')],
 'RF-04.08': [('M4 Rutas (optimizador ECS Fargate, INT-10, mapas y geocodificación); M4 alimenta el costo de servir y el modelo calcula costo por entrega y cliente', 'M10 Analítica calcula el costo por entrega y cliente; M4 Rutas aporta datos de ruta mediante INT-10 y el optimizador')],
 'RF-12.04': [('M11 transforma el mensaje válido y la ACL INT-06 lo deriva al ERP', 'M11 normaliza el mensaje válido y lo entrega a M3, dueño del pedido; la ACL INT-06 integra el pedido con el ERP')],
 'RF-12.16': [('el portal de clientes permite consultar el estado de entregas y documentación disponible', 'el portal de clientes permite consultar el estado de las entregas y la ventana de entrega comprometida')],
 'RF-19.05': [('detección.; materia absorbida', 'detección; materia absorbida')],
}
seen=set(); out=[]
for line in rows:
    ident=line.strip().split(' & ',1)[0]
    if ident in changes:
        cols=line.split(' & '); assert len(cols)==6
        for old,new in changes[ident]:
            assert cols[3].count(old)==1, ident
            cols[3]=cols[3].replace(old,new)
        if ident=='RF-03.03':
            assert cols[4]=='3.4.6'
            cols[4]='3.4.6, 3.4.2'
        line=' & '.join(cols); seen.add(ident)
    out.append(line)
assert seen==set(changes), seen
p.write_text(''.join(out),encoding='utf8',newline='')
print('Filas:',', '.join(sorted(seen)))
