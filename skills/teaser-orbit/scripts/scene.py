from core import *
def earth(s,cx,cy,r):
 # Analytic spherical shading + seeded fractal geography. No source photograph is sampled.
 n=900;yy,xx=np.mgrid[-1:1:complex(n),-1:1:complex(n)];rr=xx*xx+yy*yy;z=np.sqrt(np.maximum(0,1-rr));mask=rr<=1
 lon=np.arctan2(xx,z);lat=np.arcsin(np.clip(yy,-1,1));terrain=np.zeros_like(xx)
 for k in range(1,6):terrain+=np.sin(lon*(2.3*k)+np.sin(lat*3.1*k)+k)*np.cos(lat*(2.7*k)-k*.6)/(k**1.1)
 # Smaller coherent detail breaks up continents and cloud bands.
 fine=np.zeros_like(xx)
 for k in range(6,17):fine+=np.sin(lon*(k*4.3)+np.sin(lat*k*2.1))*np.cos(lat*k*3.7+lon*2)/(k**1.3)
 terrain+=fine*.5
 sea=np.zeros((n,n,3))+hx('#174e7c');land=terrain>.32
 sea[land]=hx('#6c8d70')+fine[land,None]*35;ice=np.abs(lat)>1.22;sea[ice]=hx('#c4ced0')
 clouds=np.clip((np.sin(lon*24+np.sin(lat*17)*1.8+fine*15)+np.cos(lat*31+lon*9)+fine*6-1.0)*.55,0,.8)
 sea=sea*(1-clouds[...,None])+hx('#e4eef1')*clouds[...,None]
 lighting=np.clip((-.62*xx-.32*yy+.71*z),0,1);sea*=.07+.93*lighting[...,None]
 rim=np.exp(-z*24)*mask;sea+=rim[...,None]*hx('#57c7ff')*.75
 out=np.zeros((n,n,4),np.uint8);out[:,:,:3]=np.uint8(np.clip(sea,0,255));out[:,:,3]=mask*255;s.raster(Image.fromarray(out),cx-r,cy-r,2*r,2*r)
def draw(s,c):
 w,h=s.w,s.h;v=c['variant'];s.field('#020c17',[(.65,.4,.55,.65,'#163343',.22)],.8)
 for i in range(700):
  x=s.r.random()*w;y=s.r.random()*h;r=s.r.choices([.55,1,1.8,3.2],[.56,.3,.12,.02])[0];s.circle(x,y,r,'#d9e9ee',s.r.uniform(.15,.7))
 if v=='horizon':
  s.rect(0,0,w,h,'#070c16')
  for i in range(160):
   yy=h*.48+i*.75;rr=h*1.38+i*.2;col=rgb(hx('#3680bc')*(1-i/160)+hx('#ff933c')*(i/160));s.path(f'M{-w*.1},{yy+h*.11}Q{w*.5},{yy-h*.16} {w*1.1},{yy+h*.11}',stroke=col,sw=3,opacity=.65)
  s.title(y=.42,size=82,family='serif');return
 if v=='galaxy':
  cx=w*.51;cy=h*.49
  for i in range(3700):
   arm=i%3;t=s.r.random()**.60;r=t*h*.52;a=arm*math.tau/3+t*math.pi*4.2+s.r.gauss(0,.12+.15*t);x=cx+math.cos(a)*r*1.28;y=cy+math.sin(a)*r*.72
   s.circle(x,y,s.r.uniform(.35,1.8),s.r.choice(['#accbdf','#faf0d8','#ffffff']),s.r.uniform(.1,.85))
  s.circle(cx,cy,14,s.gradient('core',['#f8feff','#497a9b','#0a1829'],True));s.title(y=.54,size=78);return
 if v in ('sun','duality'):
  x=w*.14 if v=='duality' else w*.59;r=h*.17
  for k in range(25,0,-1):s.circle(x,h*.36,r+k*3,'#ffd36c',.008)
  s.circle(x,h*.36,r,'#fff8d0')
  if v=='duality':s.circle(w*.92,h*.89,h*.26,'#98cbe4');s.circle(w*.95,h*.86,h*.26,'#020c17')
  s.title(x=.5,y=.57,size=75);return
 if v=='moon':
  s.circle(w*.58,h*.52,h*.23,'#a0d8f0');s.circle(w*.64,h*.48,h*.235,'#020c17');s.title(y=.83,size=55);return
 # Terra's structural idea: a cropped world dominates the right half; typography bridges two scales.
 cx=w*1.01;cy=h*.56;r=h*.83
 if c.get('asset'):s.asset(c['asset'],(w*.48,0,w*.52,h))
 else:
  for k in range(16,0,-1):s.circle(cx,cy,r+k*2,'#6cbfef',.009)
  earth(s,cx,cy,r)
  s.circle(w*.50,h*.19,13,'#fff7d0',.85)
 title=c.get('title','TERRA');parts=title.split('|')
 s.text(parts[0].strip(),w*.07,h*.53,84,'#ffffff','start',maxw=w*.42)
 if len(parts)>1:s.text(parts[1].strip(),w*.93,h*.53,77,'#ffffff','end',maxw=w*.34)
 if c.get('subtitle'):s.text(c['subtitle'],w*.07,h*.60,24,'#b4c6d1','start',maxw=w*.38)
DEFAULT={'title':'NOVA 6.1 | Terra','subtitle':'A world of possibility','variant':'terra'}
