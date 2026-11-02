from core import *
def draw(s,c):
 w,h=s.w,s.h;v=c['variant']
 if v=='light':s.field('#d7e1ed',[(.18,.22,.36,.50,'#f0f3f9',.85),(.85,.8,.48,.6,'#b8d0e4',.4)],.4);color='#536071'
 elif v in ('purple','fabric'):
  s.field('#4433d3',[(.18,.18,.48,.45,'#e3d9ff',.9),(.9,.78,.4,.65,'#7e36ee',.9)],.8);color='#ffffff'
  for i in range(35):
   y=h*(.25+i*.017);s.path(f'M-60,{y} C{w*.3},{y+h*.4} {w*.55},{y-h*.34} {w+40},{y+h*.06}',stroke='#a7a0ff',sw=1+i*.25,opacity=.12)
 else:
  s.field('#0a0b0f',[(.16,.08,.40,.60,'#53545f',.44),(.83,.92,.40,.34,'#373846',.7)],.5);color='#ffffff'
  if v!='dark':
   for i in range(100):
    r=210+i*.8;x=w*.71+math.cos(i*.013)*80;y=h*.49+math.sin(i*.013)*35
    s.path(f'M{x-r},{y-r*.1} C{x-r*.8},{y-r*1.2} {x+r*.8},{y-r*.9} {x+r*.65},{y} C{x+r*.4},{y+r*.7} {x-r*.4},{y+r*.95} {x-r*.72},{y+r*.4}',stroke='#e3e1ef',sw=2.2,opacity=.005+i*.00025)
 if c.get('asset'):s.asset(c['asset'],(0,0,w,h))
 s.title(size=83,color=color)
DEFAULT={'title':'A quieter kind of intelligence','subtitle':'NEW POSSIBILITIES','variant':'vortex'}
