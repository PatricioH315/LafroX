# -*- coding: utf-8 -*-
"""Traductor de códigos de la EDT (estructura por fases -> estructura por productos).

Fuente única: revision/edt_equivalencias_20261117.json (paquete actual -> paquete nuevo).
- Códigos de paquete (3 o 4 niveles): se traducen salvo que estén precedidos por una
  palabra que indica otra numeración (sección, Tabla, art., RT-, ...).
- Códigos de cuenta (2 niveles): sólo se traducen en contextos inequívocos
  («cuenta X.Y», «X.Y (QA)», «(X.Y)» dentro de una fila de diccionario...) y sólo si
  todos los paquetes de la cuenta quedan en una misma cuenta nueva. El resto se reporta.
"""
import io, json, os, re, sys

AQUI = os.path.dirname(os.path.abspath(__file__))
MAPA = json.load(io.open(os.path.join(AQUI, 'edt_equivalencias_20261117.json'), encoding='utf8'))

def _cuenta(c):
    return '.'.join(c.split('.')[:2]) if not c.startswith('3.10.') else '.'.join(c.split('.')[:3])

# cuenta actual -> conjunto de cuentas nuevas
CUENTAS = {}
for viejo, nuevo in MAPA.items():
    ca = '.'.join(viejo.split('.')[:2])
    CUENTAS.setdefault(ca, set()).add('.'.join(nuevo.split('.')[:2]))
    if viejo.startswith('3.10.'):
        CUENTAS.setdefault('.'.join(viejo.split('.')[:3]), set()).add('.'.join(nuevo.split('.')[:2]))
CUENTA_UNICA = {k: next(iter(v)) for k, v in CUENTAS.items() if len(v) == 1}

GUARDA = re.compile(r'(secci[oó]n(es)?|Secci[oó]n(es)?|[Tt]abla|[Ff]igura|art[s]?\.|[Aa]rt[ií]culo|cap\.|[Cc]ap[ií]tulo|RT-|RF-|RNF-|numeral(es)?|apartado(s)?|Anexo|p\.|pp\.|versi[oó]n|ISO|ISO/IEC|v|PHP|TLS|Android|Kotlin|PostgreSQL|Laravel|CU|INT-|subsecci[oó]n|secs?\.|SD\d+,?|Subdocumento\s+\d+,?|Cap[ií]tulo\s+\d+,?|T-\d+,|BTT,|BA,|Caso,)\s*~?$')
PAQ = re.compile(r'(?<![\d.])(\d{1,2}\.\d{1,2}\.\d{1,2}(?:\.\d{1,2})?)(?![\d]|\.\d)')

def traducir(texto, reporte=None, permitir_cuentas=True):
    """Devuelve el texto con los códigos traducidos. `reporte` acumula (tipo, original, nuevo, contexto)."""
    salida = []
    pos = 0
    for m in PAQ.finditer(texto):
        cod = m.group(1)
        antes = texto[max(0, m.start() - 25):m.start()]
        if cod not in MAPA and cod in CUENTA_UNICA and not GUARDA.search(antes.rstrip()):
            salida.append(texto[pos:m.start()])
            salida.append(CUENTA_UNICA[cod])
            pos = m.end()
            if reporte is not None:
                reporte.append(('cuenta-innovacion', cod, CUENTA_UNICA[cod], ''))
            continue
        if cod not in MAPA:
            if reporte is not None:
                reporte.append(('desconocido', cod, '', texto[max(0, m.start() - 40):m.end() + 20]))
            continue
        if GUARDA.search(antes.rstrip()):
            if reporte is not None:
                reporte.append(('protegido', cod, '', texto[max(0, m.start() - 40):m.end() + 20]))
            continue
        salida.append(texto[pos:m.start()])
        salida.append(MAPA[cod])
        pos = m.end()
        if reporte is not None:
            reporte.append(('paquete', cod, MAPA[cod], ''))
    salida.append(texto[pos:])
    texto = ''.join(salida)
    if permitir_cuentas:
        texto = traducir_cuentas(texto, reporte)
    return texto

CTA_CTX = [
    re.compile(r'(?P<pre>[Cc]uentas?\s+)(?P<c>\d{1,2}\.\d{1,2})(?![\d.])'),
    re.compile(r'(?<![\d.])(?P<c>\d{1,2}\.\d{1,2})(?P<post>\s*\((?:QA|CC|FC|interfaz)\))'),
    re.compile(r'(?P<pre>\()(?P<c>\d{1,2}\.\d{1,2})(?P<post>\))'),
]

def traducir_cuentas(texto, reporte=None):
    for rx in CTA_CTX:
        def rep(m):
            c = m.group('c')
            if c in CUENTA_UNICA:
                if reporte is not None:
                    reporte.append(('cuenta', c, CUENTA_UNICA[c], ''))
                return m.group(0).replace(c, '\x00' + CUENTA_UNICA[c] + '\x00', 1)
            if c in CUENTAS and reporte is not None:
                reporte.append(('cuenta-dividida', c, '/'.join(sorted(CUENTAS[c])), m.group(0)))
            return m.group(0)
        texto = rx.sub(rep, texto)
    return texto.replace('\x00', '')

if __name__ == '__main__':
    rep = []
    for p in sys.argv[1:]:
        t = io.open(p, encoding='utf8').read()
        traducir(t, rep)
    from collections import Counter
    print(Counter(r[0] for r in rep))
    for r in rep:
        if r[0] in ('desconocido', 'protegido', 'cuenta-dividida'):
            print(r)
