from core import *
def draw(s,c):
 w,h=s.w,s.h;v=c['variant']
 if c.get('asset'):s.asset(c['asset'],(0,0,w,h))
 elif v in ('gauge','dial'):
  s.field('#0c100f',[(.3,.5,.7,.7,'#9c8062',.8)],1.4);cx=w*.50;cy=h*1.02;r=h*.84
  s.circle(cx,cy,r,'#b6a47e',1,'#333a36',12);s.circle(cx,cy,r*.69,'#152326',1,'#626f68',6)
  for i in range(81):
   a=math.pi+i*math.pi/80;x=cx+math.cos(a)*r*.96;y=cy+math.sin(a)*r*.96;rr=.84 if i%5==0 else .90;s.line(x,y,cx+math.cos(a)*r*rr,cy+math.sin(a)*r*rr,'#151d1a',3)
   if i%10==0:s.text(str(2000+i*50),cx+math.cos(a)*r*.75,cy+math.sin(a)*r*.75,30,'#26342f')
  s.title(y=.28,size=62,family='serif')
  return
 elif v=='architecture':
  s.field('#cbd5d7',[(.5,.2,.8,.4,'#f7e7d0',.7)],.8);s.rect(0,h*.60,w,h*.40,'#b9b19c')
  s.polygon([(w*.06,h*.52),(w*.52,h*.37),(w*.96,h*.52),(w*.96,h*.77),(w*.06,h*.77)],'#c7c5b9')
  s.rect(w*.16,h*.50,w*.65,h*.19,'#eeeade');s.rect(w*.30,h*.52,w*.28,h*.16,'#3f5a58');s.polygon([(w*.32,h*.74),(w*.72,h*.74),(w*.88,h),(w*.11,h)],'#6aafb6')
 elif v in ('portrait','robots','food'):
  s.field('#121916',[(.15,.25,.30,.5,'#8b6543',.6),(.9,.1,.3,.5,'#74927e',.5)],1)
  for i in range(60):s.circle(s.r.random()*w,s.r.random()*h,s.r.uniform(2,9),'#e3be74',s.r.uniform(.03,.2))
  for j in range(2 if v in ('robots','food') else 1):
   x=w*(.38+j*.31) if v in ('robots','food') else w*.56;y=h*.43
   if v=='food':
    s.circle(x,y,95,'#dbaa63',1,'#886335',3)
    for k in range(13):a=s.r.random()*math.tau;r=s.r.random()*80;s.circle(x+math.cos(a)*r,y+math.sin(a)*r,7,'#473325')
   else:
    s.rect(x-64,y+75,128,220,'#424b44',rx=30);s.circle(x,y,70,'#909d99' if v=='robots' else '#b99577');s.rect(x-42,y-25,84,32,'#233d40',rx=10)
 else:
  s.field('#b5c1bf',[(.75,.15,.4,.35,'#f1e4c7',.6),(.2,.85,.6,.5,'#d7e0dd',.6)],.7)
  for j in range(6):
   base=h*(.36+j*.10);pts=[(-40,h)]
   for i in range(80):
    x=i*w/79;y=base-h*(.08*math.sin(i*.3+j)+.09*math.sin(i*.13+j*.9)+s.r.random()*.035);pts.append((x,y))
   pts.extend([(w+40,h),(-40,h)]);s.polygon(pts,rgb(hx('#a8b4b2')*(1-j/7)+hx('#173b46')*(j/7)))
   # Fog layers occlude mountain bases, preserving depth without a photographic texture.
   s.rect(0,base+h*.10,w,h*.09,'#d3dedb',.08)
 if v=='meadow' and not c.get('asset'):
  for i in range(750):
   x=s.r.random()*w;y=h*(.53+s.r.random()*.47);r=(y/h-.45)*4;s.circle(x,y,r,s.r.choice(['#a3b4e6','#ebead6','#80936b']),.85)
 if c.get('role')=='layer':
  s.parts=[]
  if c.get('variant')=='wordmark':s.text(c.get('title','K 3.1'),w*.5,h*.55,min(h*.38,220),'#ffffff',family='serif',maxw=w*.7)
  else:
   for i in range(30):s.path(f'M{s.r.random()*w},{s.r.random()*h}q20,-30 45,-10',stroke='#ffffff',sw=s.r.uniform(1,5),opacity=.15)
  return
 # A restrained dark veil is applied by code; the wordmark remains a separate layer.
 s.rect(0,0,w,h,'#061d26',.12)
 s.title(y=.47,size=106,family='serif',maxw=.4)
 if c.get('subtitle'):s.text('FIELD NOTES / 2026',w*.06,h*.9,16,'#e6eddf','start')
DEFAULT={'title':'Beyond the horizon','subtitle':'A quieter view of what comes next','variant':'landscape'}
