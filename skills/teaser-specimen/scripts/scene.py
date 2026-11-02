from core import *
def draw(s,c):
 w,h=s.w,s.h;v=c['variant'];s.field('#e5d8b7',[(.5,.4,.8,.8,'#f4ecd1',.45)],1.2)
 glyph=c.get('glyph','5');font=ImageFont.truetype('/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf',600)
 mask=Image.new('L',(700,750));from PIL import ImageDraw
 d=ImageDraw.Draw(mask);bb=d.textbbox((0,0),glyph,font=font);d.text(((700-(bb[2]-bb[0]))/2-bb[0],70-bb[1]),glyph,font=font,fill=255)
 # Distribute specimens through the actual chosen glyph, leaving intentional gaps.
 valid=np.argwhere(np.asarray(mask)>100);selected=[]
 for _ in range(5000):
  yy,xx=valid[s.r.randrange(len(valid))];x=w*.5+(xx-350)*min(h/850,w/950);y=h*.48+(yy-360)*min(h/850,w/950)
  if all((x-a)**2+(y-b)**2>(h*.052)**2 for a,b in selected):selected.append((x,y))
  if len(selected)>=58:break
 for i,(x,y) in enumerate(selected):
  r=s.r.uniform(h*.018,h*.028);a=s.r.uniform(0,math.tau)
  if c.get('specimen_assets'):
   s.add(f'<g transform="rotate({a*180/math.pi} {x} {y})">');s.asset(c['specimen_assets'][i%len(c['specimen_assets'])],(x-r*1.3,y-r*1.3,r*2.6,r*2.6));s.add('</g>');continue
  if v=='pebbles':
   s.circle(x+2,y+4,r,'#776c52',.15);s.circle(x,y,r,s.r.choice(['#b3aa8e','#c2b795','#898b75','#d0bb93']))
   for k in range(7):s.circle(x+s.r.uniform(-r*.6,r*.6),y+s.r.uniform(-r*.6,r*.6),s.r.uniform(.5,1.8),'#554f3c',.4)
  elif v=='butterflies':
   col=s.r.choice(['#475044','#b49153','#766e50','#455348']);s.path(f'M{x},{y}C{x-r*2},{y-r*2} {x-r*1.8},{y+r} {x},{y+3}C{x+r*1.8},{y+r} {x+r*2},{y-r*2} {x},{y}Z',fill=col);s.line(x,y-r*.3,x,y+r*.8,'#293b2b',2)
  else:
   dx=math.cos(a)*r*1.5;dy=math.sin(a)*r*1.5;col=s.r.choice(['#4e6546','#798a58','#374d3a'])
   s.path(f'M{x-dx},{y-dy}Q{x-dy*1.2},{y+dx*1.2} {x+dx},{y+dy}Q{x+dy*1.2},{y-dx*1.2} {x-dx},{y-dy}Z',fill=col);s.line(x-dx,y-dy,x+dx,y+dy,'#b2b788',.7)
   if i%6==0:
    for j in range(5):s.circle(x+math.cos(j*1.256)*r*.5,y+math.sin(j*1.256)*r*.5,r*.37,'#d79148')
 if c.get('title'):s.text(c['title'],w*.5,h*.94,25,'#4f5143',maxw=w*.8)
DEFAULT={'title':'Intelligence, naturally','variant':'botanical','glyph':'5'}
