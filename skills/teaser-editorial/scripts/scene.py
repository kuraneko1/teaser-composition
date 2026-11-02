from core import *
def paper(s,x,y,w,h,base='#eee7d8',pattern='hatch'):
 s.rect(x,y,w,h,base)
 if pattern=='dots':
  for j in range(0,int(h),9):
   for i in range(0,int(w),9):s.circle(x+i,y+j,1.3,'#333e48',.55)
 elif pattern=='grain':
  for i in range(600):s.rect(x+s.r.random()*w,y+s.r.random()*h,s.r.uniform(1,5),s.r.uniform(1,4),'#313a3e',.28)
 elif pattern=='veins':
  for k in range(25):
   yy=y+k*h/24;s.path(f'M{x},{yy}Q{x+w*.5},{yy+h*.09} {x+w},{yy-h*.10}',stroke='#223228',sw=1.2,opacity=.5)
 else:
  for k in range(30):s.line(x+k*w/30,y,x+k*w/30,y+h,'#9c9c83',.7,.5)
def draw(s,c):
 w,h=s.w,s.h;v=c['variant'];s.rect(0,0,w,h,'#f2eee5')
 if v in ('halftone','textile'):
  paper(s,0,0,w*.45,h,'#a5bbc6','dots');paper(s,w*.45,0,w*.55,h,'#c7c4d3','grain')
  s.polygon([(0,h),(w*.45,0),(w*.5,h)],'#426da2',.4)
  s.title(size=80,color='#1c2526',family='serif');return
 if v=='panel':
  paper(s,0,0,w*.5,h,'#dc805f','grain');paper(s,w*.5,0,w*.5,h,'#c6d6cc','dots')
  s.path(f'M{w*.24},{h*.67}C{w*.08},{h*.39} {w*.43},{h*.15} {w*.38},{h*.57} Q{w*.25},{h*.57} {w*.30},{h*.78}',stroke='#1e2827',sw=9)
  pts=[(.21,.32),(.30,.40),(.21,.51),(.36,.57),(.31,.25)]
  for i,(x,y) in enumerate(pts):
   if i:s.line(pts[i-1][0]*w,pts[i-1][1]*h,x*w,y*h,'#fff9e8',8)
   s.circle(x*w,y*h,18,'#fff9e8')
  s.title(x=.75,y=.54,size=48,color='#253b36',family='serif',maxw=.4);return
 # Narrow material swatches flank a central window. The title crosses its quiet upper third.
 paper(s,0,0,w*.14,h,'#efc737','veins');paper(s,0,h*.65,w*.34,h*.35,'#b7ad88','veins')
 paper(s,w*.86,0,w*.14,h,'#9f4d35','dots')
 if c.get('asset'):s.asset(c['asset'],(w*.15,0,w*.69,h))
 else:
  s.rect(w*.15,0,w*.71,h,'#131c25');s.circle(w*.51,h*1.23,h*.75,s.gradient('earth',['#142b49','#6a9cbd','#c3d9de'],True))
  for i in range(18):s.path(f'M{w*.17},{h*(.63+i*.014)}Q{w*.5},{h*(.50+i*.01)} {w*.85},{h*(.64+i*.014)}',stroke='#c2d1d3',sw=1.8,opacity=.22)
 s.title(y=.40,size=79,color='#f6f1e7',family='serif',maxw=.65)
 s.path(f'M{-w*.05},{h*.84}Q{w*.47},{h*.45} {w*1.05},{h*.86}',stroke='#2c3026',sw=1.6,opacity=.65)
DEFAULT={'title':'A new perspective','subtitle':'Ideas in the material world','variant':'collage'}
