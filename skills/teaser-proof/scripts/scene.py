from core import *
def draw(s,c):
 w,h=s.w,s.h;v=c['variant'];s.rect(0,0,w,h,'#f0f1ef')
 if c.get('asset'):
  s.asset(c['asset'],(w*.04,h*.05,w*.92,h*.90));return
 if v=='workspace':
  s.rect(w*.04,h*.06,w*.92,h*.88,'#ffffff',1,6,'#b5bec2',1)
  s.rect(w*.04,h*.06,w*.92,h*.08,'#dfe5e7');s.rect(w*.04,h*.14,w*.14,h*.8,'#ebeff0')
  for i in range(5):s.rect(w*.06,h*(.18+i*.14),w*.10,h*.10,'#ffffff',1,3,'#c2c9cb',1)
  s.text(c.get('title','Evidence in context'),w*.25,h*.25,42,'#1f353d','start',maxw=w*.62)
  for i in range(4):
   x=w*(.28+i*.09);hh=h*(.09+.085*i);s.rect(x,h*.78-hh,w*.05,hh,'#577e5c')
  s.line(w*.24,h*.78,w*.67,h*.78,'#aab8b9',2)
  for i in range(7):s.rect(w*.73,h*(.4+i*.055),w*(.15 if i%3 else .11),3,'#becbca')
  s.text('ILLUSTRATIVE DATA',w*.27,h*.87,15,'#708178','start')
 else:
  colors=['#173d5b','#d96b53','#d3b55c','#799785','#a1b4be']
  for j in range(3):
   for i in range(7):
    x=i*w/7;y=j*h/3;col=colors[(i+j*2)%len(colors)];s.rect(x+4,y+4,w/7-8,h/3-8,col)
    s.circle(x+w/14,y+h/7,35,'#e3dcc5',.6);s.path(f'M{x+20},{y+h/3-20}L{x+w/14},{y+80}L{x+w/7-20},{y+h/3-20}Z',fill='#172b30',opacity=.45)
  s.rect(w*.19,h*.34,w*.62,h*.32,'#faf7ed',.95)
  s.title(y=.54,size=75,color='#1f3437',maxw=.58)
DEFAULT={'title':'A universe of possibilities','subtitle':'One system. Many expressions.','variant':'mosaic'}
