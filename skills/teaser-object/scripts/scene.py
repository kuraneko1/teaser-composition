from core import *
def draw(s,c):
 w,h=s.w,s.h;v=c['variant'];light=v in ('mascot','ear')
 s.field('#f1e8db' if v=='ear' else '#faf9f5' if light else '#003a96',[(.8,.18,.45,.6,'#a8eeff' if not light else '#e7ddff',.65),(.1,.8,.5,.5,'#0540b4' if not light else '#dac7fd',.55)],.5)
 cx=w*(.66 if v=='mascot' else .53);cy=h*.54
 if c.get('asset'):s.asset(c['asset'],(w*.37,h*.12,w*.5,h*.78))
 elif v=='digit':
  for i in range(26,0,-1):s.text(c.get('glyph','4'),cx+i*1.1,cy+h*.25-i*.7,h*.72,'#82bedc',maxw=w*.6,opacity=.06)
  s.text(c.get('glyph','4'),cx,cy+h*.25,h*.72,'#dbf4ff',maxw=w*.6,opacity=.76)
 elif v=='crystal':
  pts=[(cx-w*.09,cy+h*.05),(cx-w*.04,cy-h*.33),(cx+w*.06,cy-h*.39),(cx+w*.14,cy-h*.14),(cx+w*.08,cy+h*.30),(cx,cy+h*.38)]
  s.polygon(pts,s.gradient('glass',['#b1eeff','#bce8fd','#6690e8']),.84)
  for i in range(6):s.polygon([pts[i],pts[(i+1)%6],(cx,cy)],s.r.choice(['#efffff','#8abce9','#d2adfd','#3da0dc']),.48, '#c3f6ff',1)
 elif v=='ear':
  s.path(f'M{cx},{cy+h*.20} C{cx-w*.17},{cy-h*.01} {cx-w*.09},{cy-h*.32} {cx+w*.01},{cy-h*.22} C{cx+w*.14},{cy-h*.10} {cx+w*.02},{cy+h*.30} {cx},{cy+h*.20}Z',fill=s.gradient('skin',['#e9ba90','#f7d1ac','#bd8669']))
  s.path(f'M{cx},{cy+h*.11}C{cx-w*.09},{cy-h*.13} {cx+w*.08},{cy-h*.22} {cx+w*.02},{cy-h*.02}Q{cx-w*.04},{cy-h*.10} {cx-w*.02},{cy+h*.04}',stroke='#996b54',sw=13)
  for i in range(4):s.path(f'M{cx+100+i*31},{cy-90-i*15}Q{cx+165+i*36},{cy} {cx+100+i*31},{cy+90+i*15}',stroke='#b1a795',sw=1,opacity=.6)
 else:
  # An original mascot stands on a coherent floor plane; circles are annotation satellites.
  s.circle(cx,cy+h*.32,w*.11,'#7a617e',.10);s.rect(cx-78,cy+2,156,190,'#27252a',rx=50)
  s.circle(cx-68,cy-92,30,'#be8c50');s.circle(cx+68,cy-92,30,'#be8c50');s.circle(cx,cy-42,100,s.gradient('bear',['#d5a56c','#e1b57f','#ab7543'],True))
  s.circle(cx-30,cy-55,6,'#26211c');s.circle(cx+30,cy-55,6,'#26211c');s.circle(cx,cy-22,18,'#a97c4e');s.path(f'M{cx-8},{cy-23}Q{cx},{cy-13} {cx+8},{cy-23}',stroke='#29231c',sw=4)
  for x,y in [(w*.18,h*.29),(w*.83,h*.28),(w*.2,h*.73),(w*.86,h*.73)]:s.circle(x,y,58,'none',.65,'#aa85d9',1)
 if v=='mascot':s.title(x=.5,y=.18,size=85,color='#302341',maxw=.9)
 elif v=='ear':s.title(y=.87,size=36,color='#786b5c')
 elif c.get('title'):s.title(y=.88,size=45)
DEFAULT={'title':'NOVA','subtitle':'A new dimension of possibility','variant':'crystal'}
