from core import *
def draw(s,c):
 w,h=s.w,s.h;v=c['variant']
 if c.get('asset'):
  s.rect(0,0,w,h,'#020910');s.asset(c['asset'],(0,0,w,h));s.title(y=.52,size=80);return
 if v=='petals':
  s.field('#c3d7fd',[(.8,.12,.5,.5,'#b6cbfa',.6),(.3,.8,.5,.6,'#d59af0',.4)],.5)
  cx=w*.52;cy=h*.70
  for j in range(30):
   a=-math.pi+.09*j;length=h*(.47+.17*math.sin(j*.8));tx=cx+math.cos(a)*length*.96;ty=cy+math.sin(a)*length
   # Translucent curved leaves, not a generic blurred color field.
   fill=s.gradient('petal'+str(j),['#ffb151','#ffcc62','#f78dd1','#bba6fb'])
   s.path(f'M{cx},{cy} Q{tx-h*.13},{ty-h*.23} {tx},{ty} Q{tx+h*.16},{ty+h*.07} {cx},{cy}Z',fill=fill,opacity=.65)
   for k in range(6):
    off=(k-3)*4;s.path(f'M{cx+off},{cy} Q{tx+off},{ty+h*.13} {tx},{ty}',stroke='#fff1b7',sw=.7,opacity=.28)
  s.title(y=.51,size=94)
 elif v=='tunnel':
  s.rect(0,0,w,h,'#070b13');cx=w*.55;cy=h*.5
  for i in range(40):
   rr=h*(.04+i*.035);pts=[]
   for k in range(9):
    a=k*math.tau/8+i*.035;pts.append((cx+math.cos(a)*rr*1.5,cy+math.sin(a)*rr))
   s.polygon(pts,'none',.15+i*.015,'#1685db' if i%3 else '#f3e8d2',1.4)
  s.title(y=.53,size=80)
 else:
  s.rect(0,0,w,h,'#020910');cx=w*.60;cy=h*.50
  # A coherent parametric sheet is more legible than uniformly scattered particles.
  for j in range(65):
   pts=[]
   for i in range(105):
    u=i/104;v0=j/64;x=w*(.08+u*.89);y=h*(.51+.19*math.sin(u*6.1+v0*2.5)+.30*(v0-.5)*math.sin(u*3.1+.6));r=.65+1.15*math.sin(v0*math.pi)
    if c['variant']=='network':y=h*(.5+.27*math.sin(u*math.tau)*math.sin(v0*math.pi*2))
    col=rgb(hx('#2872e9')*(1-v0)+hx('#b4f2ff')*v0);s.circle(x,y,r,col,.48+.4*math.sin(u*math.pi));pts.append((x,y))
   if j%3==0:s.path('M'+'L'.join(f'{x:.2f},{y:.2f}' for x,y in pts),stroke='#3c93d1',sw=.5,opacity=.30)
  s.title(y=.27,size=77)
DEFAULT={'title':'FORM 5.0','subtitle':'Intelligence in continuous motion','variant':'sheet'}
