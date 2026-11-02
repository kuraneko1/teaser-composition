from core import *
def draw(s,c):
 w,h=s.w,s.h;purple=c['variant']=='violet';bg='#a08aef' if purple else '#ff5d4c';dark='#7751ec' if purple else '#e1272b';light='#cab9ff' if purple else '#ff9981';accent='#6145e4' if purple else '#ff9b00'
 s.rect(0,0,w,h,bg)
 # Oversized forms are cropped; the title is the stable axis across variants.
 for i,(x,y,r) in enumerate([(-.03,.65,.5),(.44,-.1,.56),(.82,.92,.5),(1.05,.22,.4)]):
  s.circle(x*w,y*h,r*h,dark if i%2==0 else light,.66)
 s.polygon([(w*.13,h),(w*.41,-h*.12),(w*.65,-h*.12),(w*.36,h)],dark,.9)
 s.polygon([(w*.57,h),(w*.8,h*.18),(w*.98,h)],accent,.9)
 s.rect(w*.58,h*.03,w*.2,h*.16,light,.8)
 for x,sign in [(0,1),(w,-1)]:
  for j in range(3):
   yy=h*(.43+j*.067);s.line(x,yy,x+sign*w*(.13-j*.02),yy,'#ffffff',1,.65);s.circle(x+sign*w*(.13-j*.02),yy,3,'#ffffff')
 for i in range(3):s.circle(w*.77,h*.86,60+i*27,'none',.25,'#ffffff',1.2)
 if c.get('asset'):
  old=c.get('asset_opacity',1);c['asset_opacity']=old if 'asset_opacity' in c else .10;s.asset(c['asset'],(0,0,w,h));c['asset_opacity']=old
 s.title(size=97,color='#ffffff')
DEFAULT={'title':'NOVA 3.0','subtitle':'Build what comes next','variant':'coral'}
