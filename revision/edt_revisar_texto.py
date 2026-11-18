# -*- coding: utf-8 -*-
"""Controles de texto tras la reorganización de la EDT: códigos inexistentes, palabras prohibidas
y cifras anteriores que no deberían quedar. Uso: python revision/edt_revisar_texto.py archivo.tex ..."""
import io, json, os, re, sys
sys.stdout.reconfigure(encoding='utf-8')
RAIZ = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
MAPA = json.load(io.open(os.path.join(RAIZ, 'revision', 'edt_equivalencias_20261117.json'), encoding='utf8'))
NUEVOS = set(MAPA.values())
CUENTAS_N = {'.'.join(v.split('.')[:2]) for v in NUEVOS}
GUARDA = re.compile(r'(secci[oó]n(es)?|Secci[oó]n(es)?|[Tt]abla|[Ff]igura|art[s]?\.|cap\.|RT-|numeral|apartado|Anexo|p\.|pp\.|SD\d+,|Subdocumento\s+\d+,|T-\d+,|BTT,|BA,|Caso,|secs?\.)\s*~?$')
PROH = re.compile(r'(pendiente de|por resolver|estructura anterior|versi[oó]n anterior|se reorganiz|reestructur|CODEX|Texto vigente|no acredita|no se presume|no demuestra|no garantiza|como exige|conforme a lo solicitado|§|\.md\b|\.py\b|\.json\b|\.csv\b|[Ff]ase 8\b|[Ff]ases 1 a 4|cuentas? 3\.(8|9)\b|83 ventanas|60 plazas|32 plazas|401 eventos|625 relaciones|hasta el H2)')
for f in sys.argv[1:]:
    t = io.open(f, encoding='utf8').read()
    sin_tablas = re.sub(r'\\begin\{(itemize|tablalafrox)\}.*?\\end\{\1\}', lambda m: '\n' * m.group(0).count('\n'), t, flags=re.S)
    print('==', f)
    for i, l in enumerate(sin_tablas.split('\n'), 1):
        if l.lstrip().startswith('%'): continue
        for m in re.finditer(r'(?<![\d.])(\d{1,2}\.\d{1,2}\.\d{1,2}(?:\.\d{1,2})?)(?![\d]|\.\d)', l):
            if m.group(1) not in NUEVOS and not GUARDA.search(l[:m.start()].rstrip()):
                print('  código inexistente l.%d: %s | %s' % (i, m.group(1), l[max(0, m.start() - 60):m.end() + 20]))
        for m in PROH.finditer(l):
            print('  revisar l.%d: «%s» | %s' % (i, m.group(0), l[max(0, m.start() - 70):m.end() + 40]))
