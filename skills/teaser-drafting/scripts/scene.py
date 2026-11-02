from core import *
def draw(s,c):
 w,h=s.w,s.h;v=c['variant'];blue=v=='blue';bg='#0751cf' if blue else '#f4f4f0';ink='#d0e3ff' if blue else '#292d31';line='#86aaf0' if blue else '#c1c7c9'
 s.rect(0,0,w,h,bg);cx=w*.56;cy=h*.50;sz=min(h*.44,w*.25)
 for i in range(-4,5):
  s.line(cx+i*sz/4,cy-sz,cx+i*sz/4,cy+sz,line,.65,.55);s.line(cx-sz,cy+i*sz/4,cx+sz,cy+i*sz/4,line,.65,.55)
 if v=='cube':
  cx=w*.53;cy=h*.64;a=sz*.60
  s.polygon([(cx-a,cy-a*.5),(cx,cy-a),(cx+a,cy-a*.5),(cx,cy)],'#ffa93b');s.polygon([(cx-a,cy-a*.5),(cx,cy),(cx,cy+a*1.35),(cx-a*.8,cy+a*.6)],'#b2b5b3');s.polygon([(cx,cy),(cx+a,cy-a*.5),(cx+a*.5,cy+a*.85),(cx,cy+a*1.35)],'#e4e5e0')
  if c.get('asset'):s.asset(c['asset'],(w*.38,h*.43,w*.30,h*.49))
  s.title(y=.19,size=65,color=ink,maxw=.85)
 elif v=='magnetic':
  for k in range(45):
   a=k*.14;r=sz*(.35+k*.017);s.path(f'M{cx-r},{cy} C{cx-r},{cy-r} {cx+r},{cy-r} {cx+r},{cy} C{cx+r},{cy+r} {cx-r},{cy+r} {cx-r},{cy}',stroke=ink,sw=.7,opacity=.55)
  s.title(y=.9,size=36,color=ink)
 else:
  s.circle(cx,cy,sz*.83,'none',1,line,1);s.polygon([(cx-sz,cy+sz*.5),(cx+sz*.7,cy+sz*.5),(cx+sz*.7,cy-sz*.9)],'none',1,ink,1.4)
  for i in range(25):
   a=i/24;s.line(cx-sz+a*sz*1.7,cy+sz*.5,cx+sz*.7,cy+sz*.5-a*sz*1.4,line,.65)
  s.line(cx-sz*.8,cy-sz*.85,cx+sz,cy+sz*.85,line,.8)
  s.text(c.get('title','Hy 5'),w*.26,h*.69,170,ink,'start',family='serif',maxw=w*.5)
  s.text(c.get('subtitle','preview'),cx+sz*.1,cy,42,ink,'start',family='serif',maxw=w*.28)
 for x,y in [(cx-sz,cy+sz*.5),(cx+sz*.7,cy-sz*.9),(cx+sz*.7,cy+sz*.5)]:s.circle(x,y,5,bg,1,ink,1.2)
 for i in range(7):s.text(str(i),cx-sz+i*sz/3,cy-sz-22,10,ink)
DEFAULT={'title':'Hy 5','subtitle':'preview','variant':'diagram'}
