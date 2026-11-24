"""Comprueba las correcciones cruzadas LaTeX/PDF y reproduce la medición SLA.

Ejecutar desde el proyecto: python RUTA_SD10/verificacion/verificar_coherencia_interdocumental.py
Admite --workspace para localizar los checkouts y --output para guardar evidencia.
No modifica documentos. Los controles pendientes se informan separados de errores.
"""
from pathlib import Path
import argparse
import hashlib
import json
import re
import math
from pypdf import PdfReader
from pypdf.generic import ContentStream


def union(intervals):
    result = []
    for start, end in sorted(intervals):
        assert 0 <= start <= end, (start, end)
        if start == end:
            continue
        if result and start <= result[-1][1]:
            result[-1][1] = max(result[-1][1], end)
        else:
            result.append([start, end])
    return result


def intersection(left, right):
    return union([[max(a, c), min(b, d)]
                  for a, b in union(left) for c, d in union(right)
                  if max(a, c) < min(b, d)])


def duration(intervals):
    return sum(end - start for start, end in union(intervals))


def availability(calendar, approved, outages):
    eligible_approved = intersection(calendar, approved)
    eligible_outages = intersection(calendar, outages)
    t0, a = duration(calendar), duration(eligible_approved)
    i = duration(eligible_outages) - duration(intersection(eligible_outages, eligible_approved))
    t = t0
    assert 0 <= i <= t <= t0
    return {'T0': t0, 'A': a, 'T': t, 'I': i,
            'D': 100 * (1 - i / t) if t else None,
            'presupuesto': .001 * t if t else None}


def normalize(value):
    return re.sub(r'\s+', '', value).casefold()


def printed_figure_font(native, body):
    """Mide el texto de la figura después de su escala real dentro del PDF final."""
    fonts = []
    page = PdfReader(native).pages[0]
    page.extract_text(visitor_text=lambda text, cm, tm, font, size:
                      fonts.append(size) if text.strip() else None)
    reader, scales = PdfReader(body), []

    def multiply(m, n):
        a, b, c, d, e, f = m
        g, h, i, j, k, l = n
        return [a*g+b*i, a*h+b*j, c*g+d*i, c*h+d*j, e*g+f*i+k, e*h+f*j+l]

    for final in reader.pages:
        ctm, stack = [1, 0, 0, 1, 0, 0], []
        objects = final['/Resources'].get('/XObject', {})
        if hasattr(objects, 'get_object'):
            objects = objects.get_object()
        for args, op in ContentStream(final.get_contents(), reader).operations:
            if op == b'q': stack.append(ctm[:])
            elif op == b'Q': ctm = stack.pop()
            elif op == b'cm': ctm = multiply([float(x) for x in args], ctm)
            elif op == b'Do':
                obj = objects[args[0]].get_object()
                box = obj.get('/BBox')
                if box and abs(float(box[2])-float(page.mediabox.right)) < .01 and abs(float(box[3])-float(page.mediabox.top)) < .01:
                    matrix = multiply([float(x) for x in obj.get('/Matrix', [1,0,0,1,0,0])], ctm)
                    a, b, c, d = matrix[:4]
                    total = a*a+b*b+c*c+d*d
                    # Menor valor singular: conservador también ante escala desigual.
                    scale = math.sqrt(max(0, (total-math.sqrt(max(0,total*total-4*(a*d-b*c)**2)))/2))
                    scales.append(scale)
    assert fonts and len(scales) == 1, 'No se localiza una única figura general en el PDF final'
    return min(fonts)*scales[0]


def check(root, output=None):
    sd4 = root / 'tmp/sd4-corrigiendo-integracion'
    sd5 = root / 'tmp/lafrox-revision-sd4-20261114/SD5'
    sd10 = Path(__file__).resolve().parents[1]
    checks, errors = [], []

    def require(condition, message):
        (checks if condition else errors).append(message)

    def source(base, file):
        return (base / file).read_text(encoding='utf-8-sig')

    fig = sd4 / '04/figuras/logica/capas/ARQL-01_General_legible.pdf'
    layers = source(sd4, '04/partes/4.1_logica/04_capas_de_la_arquitectura.tex')
    require('ARQL-01_General_legible.pdf' in layers and (sd4 / '04/figuras/logica/capas/ARQL-01_General_definitivo.pdf').is_file(),
            'Vista general legible y figura original conservada')
    fig_text = normalize(PdfReader(fig).pages[0].extract_text())
    require('valkey(amazonelasticache)' in fig_text and 'redis(elasticache' not in fig_text,
            'Figura 1 usa Valkey (Amazon ElastiCache)')
    figure_font = printed_figure_font(fig, sd4/'entrega/LAFROX-Subdocumento4.pdf')
    require(figure_font >= 9, 'Figura 1 cumple 9 puntos después de la escala final')
    xml = source(sd4, '04/figuras/fuentes/Arquitectura-logica-general-y-8-capas.drawio.xml')
    require('value="Redis' not in xml and 'value="Valkey' in xml, 'XML editable sincronizado con la figura')
    domains = source(sd4, '04/partes/4.1_logica/06_modelo_de_datos_conceptual.tex')
    require('es un nombre lógico; el motor es Valkey' in domains, 'Identificador lógico separado del motor')
    body = source(sd5, '05_modelo_datos/partes/5_2_gestion.tex')
    route = source(sd5, '05_modelo_datos/anexos/tablas/A_23.tex')
    offline = source(sd5, '05_modelo_datos/tablas/limites_offline.tex')
    require('sin superar 16 horas desde su emisión' in body
            and '30 minutos después del fin programado' in body
            and 'antes de cumplir las 14 horas' not in body
            and 'cota de 16 h' in route
            and '8 h bodega / 14 h terreno' not in offline
            and 'como máximo 16 h desde emisión' in source(sd5, '05_modelo_datos/anexos/contenido.tex'),
            'SD5 conserva el mínimo de autonomía y aplica la asignación de reparto de SD4')
    service = source(sd10, '10_servicios_operacion/partes/10_1_servicios.tex')
    require('2026h, apartados 8.1.1 y 10.1.2' not in service
            and '2026g, T-14, paquete 10.1.2' in service, 'Cita SD8 separada de T-14')
    guides = source(sd10, '10_anexos/partes/10_c_guias.tex')
    require('respaldo sintético representativo' in guides
            and 'no lo presenta como restauración de una copia productiva' in guides,
            'Restauraciones sintéticas identificadas con su alcance')
    matrix = source(sd10, '10_anexos/partes/10_e_matriz.tex')
    require('borrador' not in matrix, 'Matriz SD10 identificada como contenido del subdocumento')
    closure = source(sd4, '04/anexos/fisica/17_anexo_4x_detalle_tecnico.tex')
    require(all(token in closure for token in ('CD-ERP', 'CD-RPO', 'CD-TLS')),
            'Decisiones de continuidad y compatibilidad identificadas')
    annex = source(sd10, '10_anexos/contenido.tex')
    require(all(token in annex for token in ('CD-SLA', 'CD-MESA', 'CD-UI', 'Cada registro distingue')),
            'Cierre de servicio enlazado a decisiones y evidencia')

    cases = json.loads(Path(__file__).with_name('casos_sla.json').read_text(encoding='utf-8'))
    sla_results = []
    for case in cases:
        result = availability(case['calendario'], case['aprobado'], case['fallas'])
        require(all(result[key] == value for key, value in case['esperado'].items()),
                'SLA: ' + case['id'])
        sla_results.append({'id': case['id'], **result})
    example = next(row for row in sla_results if row['id'] == 'exceso_de_ventana')
    measurement = source(sd10, '10_anexos/partes/10_b_medicion.tex')
    require(r'\text{43.200}' in measurement and '$T=T_0$' in measurement,
            'Miles expresados sin conversión a coma decimal de la plantilla')
    require(f"{example['D']:.5f}".replace('.', ',') in measurement and example['T'] == 43200,
            'Ejemplo publicado de medición coincide con el cálculo de intervalos')

    for base in (sd4, sd5, sd10):
        for path in base.rglob('*.tex'):
            if '_build' not in path.parts:
                require(chr(167) not in path.read_text(encoding='utf-8-sig'),
                        'Referencia sin símbolo de sección: ' + str(path.relative_to(base)))
    require('AL-DTE-01' in guides and 'AL-DR-01' in guides and 'sin aceptación' in guides,
            'Guías conservan las pruebas de recuperación y su límite de aceptación')
    record = json.loads((sd10 / 'trazabilidad/cierres_interdocumentales.json').read_text(encoding='utf-8'))
    for item in record['decisiones']:
        require(item['estado'] in ('criterio_adoptado', 'limite_residual', 'verificacion_por_etapa'),
                'Decisión de diseño sin aprobación supuesta: ' + item['id'])
        require('consulta' not in item and item['evidencia_ejecucion'] == [],
                'No se simula consulta o prueba real: ' + item['id'])
    security = source(sd4, '04/anexos/logica/partes/21_anexo_4_1_r_controles_seguridad.tex')
    require('usa TLS 1.2 como excepción' not in security and 'rechazo de versiones inferiores' in security,
            'TLS 1.2 no se ofrece como excepción')
    require('no reduce el denominador' in source(sd10, '10_servicios_operacion/partes/10_2_niveles.tex'),
            'Cuerpo y anexo conservan calendario íntegro')
    reserve = json.loads((sd10/'trazabilidad/propuesta_mesa_C.json').read_text(encoding='utf-8'))
    peaks = reserve['meses_peak']
    require(sum(m['incremento_HH_mesa'] for m in peaks) == 2010
            and sum(m['incremento_HH_NOC'] for m in peaks) == 308,
            'Reserva C conciliada por seis meses peak')
    require(len(peaks) == 6 and peaks[0]['mes_contractual'] == 23,
            'Reserva incluye diciembre anterior a M25')
    require(all(m['propuesta_C_HH_mesa'] - m['base_HH_mesa'] == m['incremento_HH_mesa']
                and m['propuesta_C_HH_mesa'] <= m['propuesta_C_plazas']*128 for m in peaks),
            'Incrementos y capacidad de reserva por mes coherentes')
    result = {'proyecto': 'LafroX', 'passed': not errors, 'controles': len(checks),
              'errors': errors, 'sla': sla_results, 'fuente_minima_figura_1_pt': figure_font,
              'decisiones': record['decisiones'],
              'limite': 'Verificación documental y aritmética; no acredita pruebas reales, contratación ni acuerdos del CLIENTE.'}
    if output:
        output.write_text(json.dumps(result, ensure_ascii=False, indent=2), encoding='utf-8')
    print(json.dumps({'passed': result['passed'], 'controles': len(checks),
                      'errors': errors, 'limites_residuales': [i['id'] for i in record['decisiones'] if i['estado']=='limite_residual']},
                     ensure_ascii=False, indent=2))
    return 0 if result['passed'] else 1


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--workspace', type=Path, default=Path(__file__).resolve().parents[2])
    parser.add_argument('--output', type=Path)
    args = parser.parse_args()
    raise SystemExit(check(args.workspace, args.output))
