from core import *
def draw(s,c):
 w,h=s.w,s.h;v=c['variant'];cx=w*.52;cy=h*.39
 s.field('#071020',[(.51,.38,.32,.43,'#338dff',.8),(.20,.18,.42,.42,'#889cd4',.5),(.85,.55,.35,.55,'#ecb8aa',.6)],1)
 # Converging streaks create depth; the foreground silhouette gives a scale reference.
 for i in range(220):
  a=s.r.uniform(0,math.tau);r=s.r.uniform(w*.1,w*.65);x=cx+math.cos(a)*r;y=cy+math.sin(a)*r*.62
  s.line(cx+(x-cx)*.1,cy+(y-cy)*.1,x,y,s.r.choice(['#77bfff','#e5dcff','#ef9293','#ffffff']),s.r.uniform(.5,5),s.r.uniform(.04,.22))
 if v=='planet':
  s.circle(cx,h*.4,h*.52,s.gradient('sun',['#ff7296','#ff414c','#ed8c29'],True));s.rect(0,h*.88,w,h*.12,'#18101b');cx=w*.51;cy=h*.77
  s.circle(cx,cy,55,'#26202c');s.circle(cx-19,cy-12,9,'#fb8e7a');s.circle(cx+19,cy-12,9,'#fb8e7a');s.rect(cx-36,cy+38,72,58,'#292230',rx=22)
  s.title(y=.34,size=100)
 else:
  if c.get('asset'):s.asset(c['asset'],(w*.34,h*.12,w*.35,h*.88))
  else:
   s.circle(cx,cy+25,32,'#111d31');s.path(f'M{cx-22},{cy+53} Q{cx-54},{h*.64} {cx-68},{h*.77} L{cx-110},{h*1.05} L{cx+40},{h*1.05} L{cx+50},{h*.71} Q{cx+80},{h*.56} {cx+27},{cy+54}Z',fill='#142238')
   if v=='dancer':s.path(f'M{cx-20},{cy+85}L{cx-170},{cy+120}M{cx+15},{cy+85}L{cx+170},{cy+125}',stroke='#142238',sw=28)
  s.title(y=.25,size=76)
DEFAULT={'title':'WONDER 2.5','subtitle':'A wider world in motion','variant':'dancer'}
