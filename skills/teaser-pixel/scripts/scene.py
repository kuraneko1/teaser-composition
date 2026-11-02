from core import *
PATTERNS={'cat':['00100100','01111110','11011011','11111111','01111110','00111100','01100110'], 'flower':['0011100','0101010','0111110','0011100','0001000','0101010','0011100'], 'hourglass':['1111111','0111110','0011100','0001000','0011100','0111110','1111111'], 'microphone':['0011100','0111110','0111110','0111110','1011101','1000001','0111110','0001000','0011100'],'shield':['1111111','1111111','0111110','0111110','0011100','0001000']}
def stamp(s,x,y,size,kind,color):
 grid=PATTERNS.get(kind,PATTERNS['cat']);cell=size/len(grid[0])
 for j,row in enumerate(grid):
  for i,ch in enumerate(row):
   if ch=='1':s.rect(x+i*cell,y+j*cell,cell+.2,cell+.2,color)
def draw(s,c):
 w,h=s.w,s.h;v=c['variant'];color=c.get('accent','#0783ed');side=c.get('side','right');s.field('#12131e',[(.9,.8,.6,.8,'#242739',.6)],.8)
 if c.get('asset'):s.asset(c['asset'],(0,0,w,h))
 for i in range(1,9):s.line(i*w/8,0,i*w/8,h,'#4c4b5b',.6,.25)
 for i in range(1,6):s.line(0,i*h/6,w,i*h/6,'#4c4b5b',.6,.25)
 s.path(f'M{-w*.1},{h*.95} Q{w*.55},{-h*.55} {w*1.1},{h*.35}',stroke='#777587',sw=.6,opacity=.15)
 # Mosaic is anchored at the edge, with a protected title region opposite it.
 base=w*.62 if side=='right' else -w*.22;cell=min(w*.061,h*.11)
 for j in range(10):
  for i in range(11):
   if s.r.random()<.80 and (i+j)%7!=0:s.rect(base+i*cell,j*cell,cell+.3,cell+.3,s.r.choice([color,'#59c6ff','#1039a1','#a9d9ff','#edf3e9']))
 kind=c.get('motif','microphone')
 if v=='asset':
  s.parts=[];s.rect(0,0,w,h,'#ebe9e0');stamp(s,w*.3,h*.14,min(w*.4,h*.7),kind,color);return
 if v=='thumbnail':
  s.rect(w*.42,h*.30,w*.22,h*.40,'#eeeede');stamp(s,w*.48,h*.38,w*.10,kind,color)
 elif v=='duo':
  stamp(s,w*.12,h*.25,w*.25,'cat','#ff9c00');stamp(s,w*.63,h*.32,w*.22,'cat','#252837')
 elif v=='partner':
  s.title(x=.5,y=.69,size=65);stamp(s,w*.42,h*.14,160,'cat','#ff7d00')
 else:
  stamp(s,w*.045,h*.25,64,kind,color);s.title(x=.045,y=.53,size=80,align='start',maxw=.5)
 for k in range(18):s.circle(s.r.random()*w,s.r.random()*h,1.3,'#ffffff',.4)
DEFAULT={'title':'Introducing SIGNAL','subtitle':'Open models, new perspectives','variant':'cover','motif':'microphone'}
