from pathlib import Path
import re

documents = {
    'subdocumento-07': 'LafroX-Subdocumento7.md',
    'subdocumento-07-anexos': 'LafroX-Subdocumento7-Anexos.md',
    'formulario-t14': 'LafroX-Formulario-T-14.md',
    'formulario-t15': 'LafroX-Formulario-T-15.md',
    'formulario-t18': 'LafroX-Formulario-T-18.md',
}

for root, md_name in documents.items():
    tex = (Path(root) / 'contenido.tex').read_text(encoding='utf-8')
    md_path = Path(md_name)
    md = md_path.read_text(encoding='utf-8')
    refs = tex[tex.rfind(r'\section*{Referencias}'):]
    refs = refs[:refs.find(r'\end{itemize}')]
    items = re.findall(r'^\\item (.+)$', refs, re.M)
    def plain(item):
        return re.sub(r'\\emph\{([^}]*)\}', r'*\1*', item).replace(r'\&', '&')
    bibliography = ('Referencias\n\nLas fuentes citadas se listan en formato APA 7.ª edición. '
                    'Las Bases se citan con su documento y el artículo, capítulo, sección o código del requisito.\n\n'
                    + '\n\n'.join('- ' + plain(i) for i in items) + '\n')
    marker = '\nReferencias\n'
    pos = md.rfind(marker)
    if pos == -1:
        raise RuntimeError(f'Referencias absent: {md_name}')
    md = md[:pos + 1] + bibliography
    for source, short in [('Bases Administrativas', 'BA'), ('Bases Técnicas Transversales', 'BTT'), ('Caso logística', 'Caso')]:
        md = md.replace('(' + source + ',', '(' + short + ',')
        md = md.replace('; ' + source + ',', '; ' + short + ',')
    md = md.replace('Pontificia Universidad Católica de Valparaíso', 'Distribuidora Puelche S.A.')
    md = md.replace('LafroX SpA', 'LafroX')
    revised_lines = []
    for line in md.splitlines(keepends=True):
        if 'Fuente:' in line:
            head, source = line.split('Fuente:', 1)
            source = source.replace('de las Bases Administrativas', 'de Distribuidora Puelche S.A. (2026a)')
            source = source.replace('Bases Administrativas', 'Distribuidora Puelche S.A. (2026a)')
            source = source.replace('de las Bases Técnicas Transversales', 'de Distribuidora Puelche S.A. (2026b)')
            source = source.replace('Bases Técnicas Transversales', 'Distribuidora Puelche S.A. (2026b)')
            source = source.replace('del Caso logística', 'de Distribuidora Puelche S.A. (2026c)')
            source = source.replace('Caso logística', 'Distribuidora Puelche S.A. (2026c)')
            source = re.sub(r'\bCaso,', 'Distribuidora Puelche S.A. (2026c),', source)
            source = re.sub(r'Capítulo 3, Anexo 3\.([A-Z])', r'LafroX (2026j, SD3, Anexo 3.\1)', source)
            source = source.replace('Capítulo 3, Tabla 3.5', 'LafroX (2026k, SD3, Tabla 3.5)')
            line = head + 'Fuente:' + source
        revised_lines.append(line)
    md = ''.join(revised_lines)
    md_path.write_text(md, encoding='utf-8')
    print(md_name, len(items), 'references')
