"""Extract all three PDFs and render affected pages for visual verification."""
from pathlib import Path
import json, re, hashlib
import pypdfium2 as pdfium
from PIL import Image, ImageDraw
import pdfplumber

ROOT=Path(__file__).resolve().parents[2]
QA=ROOT/'04/revision/aclaraciones_20261011'
reports=[]
for stem,short in [('LAFROX-Subdocumento4','cuerpo'),('LAFROX-Subdocumento4-Anexos','anexos'),('LAFROX-Formulario-T-11','t11')]:
    path=ROOT/'entrega'/f'{stem}.pdf'
    doc=pdfium.PdfDocument(str(path))
    texts=[]; selected=[]; figures=[]; human_pages=[]
    for i in range(len(doc)):
        page=doc[i]; tp=page.get_textpage(); t=tp.get_text_range(); tp.close()
        texts.append(t)
        clean=' '.join(t.split())
        # Cover, index, all IA pages, bibliography, corrected annex heading,
        # and all new network views are inspected at full rendering resolution.
        if i<3 or 'Álvaro Catalán:' in clean or (short=='anexos' and ('Detalle de selección por capa' in clean or 'Monitor email sending' in clean or 'WhatsApp message status' in clean)) or (short=='t11' and 'Referencias' in clean) or any(x in clean for x in ['Red de los cinco sitios y las dos regiones','Detalle de red y continuidad en los sitios','Detalle de conectividad regional y replicación']):
            selected.append(i+1)
            img=page.render(scale=1.6).to_pil()
            img.save(QA/f'{short}_{i+1:03}.png')
        if any(x in clean for x in ['Red de los cinco sitios y las dos regiones','Detalle de red y continuidad en los sitios','Detalle de conectividad regional y replicación']): figures.append(i+1)
        if 'Álvaro Catalán:' in clean: human_pages.append(i+1)
        page.close()
    alltext='\n\f\n'.join(texts)
    (QA/f'{short}.txt').write_text(alltext,encoding='utf-8')
    forbidden={name:len(re.findall(pattern,alltext,re.I)) for name,pattern in [('caso_enumerado',r'caso\s*0?2\b'),('marcador_humano',r'REVISIÓN HUMANA\]\]')]}
    # The user's correction concerns the review column, not the pre-existing
    # legal representative on the cover. Check every IA page independently.
    forbidden['alex_en_revision']=sum(len(re.findall(r'Alex\s+Aravena',texts[n-1],re.I)) for n in human_pages)
    assert not any(forbidden.values()), (stem,forbidden)
    r={'document':stem,'pages':len(doc),'selected_pages':selected,'human_pages':human_pages,'figures':figures,'forbidden':forbidden,'sha256':hashlib.sha256(path.read_bytes()).hexdigest()}
    if figures:
        with pdfplumber.open(path) as pd:
            r['diagram_font_sizes']=[]
            for n in figures:
                page=pd.pages[n-1]
                # Report the embedded diagram font separately from the
                # corporate running header, footer and caption fonts.
                fonts={}
                for ch in page.chars:
                    name=ch['fontname']
                    if ch['text'].strip():fonts.setdefault(name,[]).append(round(ch['size'],3))
                r['diagram_font_sizes'].append({'page':n,'fonts':{k:[min(v),max(v)] for k,v in fonts.items()}})
    # Contact sheets retain full PNGs as the readable inspection source.
    for k in range(0,len(selected),6):
        sheet=Image.new('RGB',(1440,1250),'#e4e8ed'); draw=ImageDraw.Draw(sheet)
        for j,n in enumerate(selected[k:k+6]):
            im=Image.open(QA/f'{short}_{n:03}.png');im.thumbnail((460,565))
            x=(j%3)*480+(480-im.width)//2;y=(j//3)*625+35
            sheet.paste(im,(x,y));draw.text(((j%3)*480+15,(j//3)*625+12),f'{short} - pagina {n}',fill='black')
        sheet.save(QA/f'{short}_contacto_{k//6+1}.png')
    reports.append(r);doc.close()
(QA/'pdf_verificacion.json').write_text(json.dumps(reports,ensure_ascii=False,indent=2),encoding='utf-8')
print(json.dumps(reports,ensure_ascii=False))
