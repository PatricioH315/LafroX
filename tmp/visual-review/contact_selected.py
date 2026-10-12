from PIL import Image,ImageOps,ImageDraw
from pathlib import Path
import sys
p=Path(sys.argv[1]); fs=sorted(p.glob('page-*.png'),key=lambda x:int(x.stem.split('-')[-1])); w=480; pad=14; ims=[]
for f in fs:
 im=Image.open(f).convert('RGB'); h=round(im.height*w/im.width); ims.append((f.name,ImageOps.expand(im.resize((w,h)),border=1,fill='gray')))
cols=2; rows=(len(ims)+1)//2; ch=max(i.height for _,i in ims)+24
sheet=Image.new('RGB',(cols*(w+pad)+pad,rows*ch+pad),'white'); d=ImageDraw.Draw(sheet)
for n,(name,im) in enumerate(ims):
 x=pad+(n%2)*(w+pad); y=pad+(n//2)*ch; d.text((x,y),name,fill='black'); sheet.paste(im,(x,y+22))
sheet.save(p/'contact.png')
