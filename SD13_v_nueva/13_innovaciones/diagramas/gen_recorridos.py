from pathlib import Path
import importlib.util

ROOT = Path(__file__).resolve().parents[2]
DIR = ROOT / '13_innovaciones/diagramas'
spec = importlib.util.spec_from_file_location('diagramas', DIR / 'gen_diagramas.py')
g = importlib.util.module_from_spec(spec)
spec.loader.exec_module(g)
g.OUT = DIR

# Vistas propias de detalle; no son recortes de la figura general.
flows = [
('INN01', 'Vencimiento posentrega', [
'1. Datos del lote y del local<br>M2 Inventario, M9 Calidad y trazabilidad e historial de M3 Preventa',
'2. Cálculo nocturno<br>M10 Analítica sobre N-10: saldo estimado, reposición y vida útil',
'3. Aviso precargado<br>M3 entrega la lista a C-01 App de preventa; disponible sin señal',
'4. Visita al local<br>El preventista confirma saldo y ritmo, propone una acción autorizada y registra la respuesta',
'5. Retorno de la respuesta<br>Cola de sincronización de M3 al recuperar conexión; cierre de la acción comercial',
'6. Verificación del beneficio<br>I-01A: piloto del mes 15<br>I-01B e I-01C: vencimiento posentrega, sin duplicar el ahorro de bodega'],
'Control: sin datos suficientes se muestra fecha y cantidad, sin predicción. El saldo no modifica el inventario oficial; la disposición sanitaria sigue en M9.'),
('INN02', 'Reproducción de incidentes', [
'1. Incidente en terreno<br>C-01, C-03 o C-02 captura orden causal, reintentos y conectividad, con cupo de evidencia',
'2. Evidencia protegida<br>Capa 7 sanitiza; capa 8 correlaciona con OpenTelemetry y CloudWatch; SRE recoge el paquete',
'3. Admisión y reproducción<br>Calidad admite el caso; GitLab CI y Terraform crean recursos efímeros en QA o Preproducción',
'4. Corrección y contraste<br>Desarrollo corrige; se ejecuta el mismo paquete y se compara con el estado observado',
'5. Cierre comprobado<br>Reproducción satisfactoria, confirmación del actor de terreno y escenario de regresión permanente',
'6. Medición y limpieza<br>I-02A e I-02B: beneficio al mes 15; recursos destruidos aun si la prueba falla'],
'Control: un paquete con datos prohibidos detiene la captura (I-02D). Si no reproduce la causa, se conserva el diagnóstico convencional; no se crea un sexto ambiente.'),
('INN03', 'Historia térmica del lote', [
'1. Historia por tramo<br>B-01: cámara; B-03: camión. Cada lote se asocia al sensor por lugar y tiempo',
'2. Captura sin enlace<br>B-02 acumula carga en cámara; C-02 alerta en ruta y descarga el registro completo al retorno',
'3. Ingesta y asociación<br>N-08 y N-06 reciben series; capa 5 enlaza eventos EPCIS y datos del sensor con el lote',
'4. Estimación versionada<br>M10 sobre N-10 integra el modelo cinético por familia; parámetros aprobados por Calidad',
'5. Disposición y consumo<br>M9 presenta la evidencia a Calidad; M2 y M5 reciben sugerencia por familia; innovación 1 usa la estimación',
'6. Validación y recalibración<br>I-03B: contraste con Calidad en el piloto; paquete 8.3.2: revisión semestral'],
'Control: no se rellenan tramos sin datos ni se alarga la fecha impresa. La estimación no sustituye la regla graduada, el bloqueo ni el FEFO obligatorio.'),
('INN04', 'Liquidación por costo de servir', [
'1. Hechos de la operación<br>M6 Reparto, M7 Cobranza y rendición y M8 Devoluciones y envases aportan entregas y retornos',
'2. Referencia comparable<br>N-10 conserva canasta y línea base de meses 21 a 23; índices y regla estacional documentados',
'3. Cálculo de desempeño<br>M10 Analítica obtiene costo comparable y OTIF, sin excluir entregas fallidas del denominador',
'4. Ensayo sin pago<br>Finanzas reproduce tres liquidaciones en sombra en meses 21 a 23; I-04B exige 3 de 3',
'5. Liquidación desde mes 24<br>Tramo variable acotado, solo con OTIF vigente cumplido; capa 7 audita y ERP conserva dato definitivo',
'6. Acompañamiento y efecto<br>Comercial decide la recomendación de malla; se registra respuesta; I-04A se verifica al mes 36'],
'Control: no se compensan multas ni se supera el máximo. Si no rinde, se vuelve a la estructura de pago de las Bases; el costo de servir obligatorio permanece.'),
('INN05', 'Hoja de negocio del almacenero', [
'1. Datos propios del local<br>Compras y productos ausentes; vencimiento de INN-01 solo con datos confirmados',
'2. Preparación previa a ruta<br>M10 Analítica sobre N-10 calcula la hoja; capa 7 limita acceso al receptor',
'3. Visita sin internet<br>M3 Preventa muestra la hoja precargada y cifrada en C-01; el cliente no necesita dispositivo',
'4. Copia si se solicita<br>M6 Reparto imprime en cabina y entrega con la guía en la entrega siguiente; preventista sin impresora',
'5. Seguimiento de cobertura<br>I-05A separa hojas mostradas, copias pedidas y entregadas; sin pedido, la copia espera otra entrega',
'6. Comprensión y efecto<br>I-05B antes del mes 19; cobertura al mes 27; efecto comercial estimado al mes 33'],
'Control: el bloque comparativo 4 solo se activa desde mes 27 con aprobación legal, umbral de grupo y supresión; si no se aprueba, continúan los bloques 1 a 3.')]

def generate():
    for i, (code, title, nodes, guard) in enumerate(flows, 2):
        d = g.Diagram(f'Fig_13-{i}_Recorrido_{code}')
        pos = [(0,0), (310,0), (310,150), (0,150), (0,300), (310,300)]
        style = g.BOX.replace(f'fontSize={g.FS}', 'fontSize=15') + 'spacing=8;'
        accent = g.BOXACC.replace(f'fontSize={g.FS}', 'fontSize=15') + 'spacing=8;'
        ids = [d.box(t, x, y, 290, 125, accent if j in (0,5) else style) for j,(t,(x,y)) in enumerate(zip(nodes,pos))]
        for j in range(5):
            if j in (0,4): ex,en=(1,.5),(0,.5)
            elif j == 2: ex,en=(0,.5),(1,.5)
            else: ex,en=(.5,1),(.5,0)
            d.edge(ids[j], ids[j+1], exit_=ex, entry=en)
        d.box(guard, 0, 450, 600, 95, style + 'fillColor=#F4F4F4;')
        d.save()

if __name__ == '__main__':
    generate()
