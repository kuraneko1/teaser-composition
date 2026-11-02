"""Deterministic SVG composition, raster export, typography and optional asset placement."""
from pathlib import Path
import argparse,base64,io,json,math,random,sys
from html import escape
import numpy as np
from PIL import Image,ImageFont,ImageFilter,ImageOps

def hx(c):
 return np.array(tuple(int(c.lstrip('#')[i:i+2],16) for i in (0,2,4)),float)
def rgb(c): return '#'+''.join(f'{int(v):02x}' for v in np.clip(c,0,255))
class Scene:
 def __init__(self,c):
  self.c=c;self.w=1600.;self.h=self.w*c['height']/c['width'];self.parts=[];self.defs=[];self.r=random.Random(c['seed']);self.np=np.random.default_rng(c['seed'])
 def add(self,s): self.parts.append(s)
 def rect(self,x,y,w,h,fill,opacity=1,rx=0,stroke='none',sw=1):self.add(f'<rect x="{x:.3f}" y="{y:.3f}" width="{max(w,0):.3f}" height="{max(h,0):.3f}" rx="{rx}" fill="{fill}" opacity="{opacity}" stroke="{stroke}" stroke-width="{sw}"/>')
 def circle(self,x,y,r,fill,opacity=1,stroke='none',sw=1):self.add(f'<circle cx="{x:.3f}" cy="{y:.3f}" r="{max(r,0):.3f}" fill="{fill}" opacity="{opacity}" stroke="{stroke}" stroke-width="{sw}"/>')
 def path(self,d,fill='none',stroke='none',sw=1,opacity=1):self.add(f'<path d="{d}" fill="{fill}" stroke="{stroke}" stroke-width="{sw}" opacity="{opacity}" stroke-linecap="round" stroke-linejoin="round"/>')
 def polygon(self,pts,fill,opacity=1,stroke='none',sw=1):self.add(f'<polygon points="'+ ' '.join(f'{x:.2f},{y:.2f}' for x,y in pts)+f'" fill="{fill}" opacity="{opacity}" stroke="{stroke}" stroke-width="{sw}"/>')
 def line(self,x1,y1,x2,y2,color,sw=1,opacity=1):self.path(f'M{x1},{y1}L{x2},{y2}',stroke=color,sw=sw,opacity=opacity)
 def gradient(self,name,colors,radial=False):
  tag='radialGradient' if radial else 'linearGradient';attrs='cx="50%" cy="50%" r="50%"' if radial else 'x1="0%" y1="0%" x2="100%" y2="100%"'
  self.defs.append(f'<{tag} id="{name}" {attrs}>'+''.join(f'<stop offset="{i/(len(colors)-1)*100}%" stop-color="{v}"/>' for i,v in enumerate(colors))+f'</{tag}>');return f'url(#{name})'
 def raster(self,im,x=0,y=0,w=None,h=None,opacity=1):
  b=io.BytesIO();im.save(b,format='PNG');data=base64.b64encode(b.getvalue()).decode();self.add(f'<image x="{x}" y="{y}" width="{w or self.w}" height="{h or self.h}" opacity="{opacity}" href="data:image/png;base64,{data}"/>')
 def asset(self,p,box):
  # Assets are supplied imagery only; no network requests or image generation occur.
  if self.c.get('asset_box'):
   bx,by,bw,bh=self.c['asset_box'];box=(bx*self.w,by*self.h,bw*self.w,bh*self.h)
  x,y,w,h=box;im=Image.open(p).convert('RGBA');target=(max(1,int(w)),max(1,int(h)))
  if self.c.get('asset_fit','cover')=='contain':
   tile=Image.new('RGBA',target);im=ImageOps.contain(im,target,Image.Resampling.LANCZOS);tile.alpha_composite(im,((target[0]-im.width)//2,(target[1]-im.height)//2));im=tile
  else:im=ImageOps.fit(im,target,method=Image.Resampling.LANCZOS)
  self.raster(im,x,y,w,h,opacity=self.c.get('asset_opacity',1))
 def text(self,t,x,y,size=70,color='#ffffff',anchor='middle',weight=500,family='sans',maxw=None,opacity=1):
  font=self.c.get('font')
  if not font:font=('/usr/share/fonts/opentype/noto/NotoSerifCJK-Regular.ttc' if family=='serif' else '/usr/share/fonts/opentype/noto/NotoSansCJK-Bold.ttc' if weight>=600 else '/usr/share/fonts/opentype/noto/NotoSansCJK-Regular.ttc')
  if not Path(font).exists():font='/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf'
  f=ImageFont.truetype(font,max(1,int(size)))
  if maxw and f.getlength(t)>maxw:size*=maxw/f.getlength(t)
  # Embed rasterized text layers; text stays editable in JSON and Python, not as SVG text.
  scale=max(2.,self.c['width']/1600*1.5);f=ImageFont.truetype(font,max(1,int(size*scale)));bb=f.getbbox(t);ww=max(1,int(f.getlength(t))+8);hh=max(1,bb[3]-bb[1]+8)
  im=Image.new('RGBA',(ww,hh));from PIL import ImageDraw
  ImageDraw.Draw(im).text((4,-bb[1]+4),t,font=f,fill=color)
  tw,th=ww/scale,hh/scale;xx=x-tw/2 if anchor=='middle' else x-tw if anchor=='end' else x
  self.add(f'<g aria-label="{escape(t,quote=True)}" opacity="{opacity}">');self.raster(im,xx,y-th,tw,th);self.add('</g>')
 def field(self,base,blobs,grain=.8):
  w=960;h=max(64,round(w*self.h/self.w));yy,xx=np.mgrid[0:h,0:w];x=xx/w;y=yy/h;arr=np.zeros((h,w,3))+hx(base)
  for cx,cy,sx,sy,col,power in blobs:
   a=(np.exp(-(((x-cx)/sx)**2+((y-cy)/sy)**2)/2)*power)[...,None];arr=arr*(1-a)+hx(col)*a
  arr+=self.np.normal(0,grain,(h,w,1));self.raster(Image.fromarray(np.uint8(np.clip(arr,0,255))))
 def title(self,x=.5,y=.53,size=86,color='#ffffff',family='sans',align='middle',maxw=.8):
  if self.c.get('title'):self.text(self.c['title'],x*self.w,y*self.h,size,color,align,weight=self.c.get('title_weight',600 if family=='sans' else 400),family=family,maxw=self.w*maxw)
  if self.c.get('subtitle'):self.text(self.c['subtitle'],x*self.w,y*self.h+52,23,color,align,maxw=self.w*maxw,opacity=.85)
 def svg(self):return f'<svg xmlns="http://www.w3.org/2000/svg" xmlns:xlink="http://www.w3.org/1999/xlink" width="{self.c["width"]}" height="{self.c["height"]}" viewBox="0 0 {self.w} {self.h}"><title>{escape(self.c.get("title", ""))}</title><defs>'+''.join(self.defs)+'</defs>'+''.join(self.parts)+'</svg>'

def run(draw,default,presets):
 p=argparse.ArgumentParser(description=__doc__);p.add_argument('--output',default='teaser.png');p.add_argument('--config');p.add_argument('--preset',default='default');p.add_argument('--list-presets',action='store_true')
 for k in ['title','subtitle','variant','asset','font','glyph']:p.add_argument('--'+k)
 for k in ['width','height','seed']:p.add_argument('--'+k,type=int)
 a=p.parse_args()
 if a.list_presets:print('\n'.join(['default']+list(presets)));return
 if a.preset!='default' and a.preset not in presets:p.error('unknown preset; use --list-presets')
 c={'width':1600,'height':900,'seed':17,'title':'','subtitle':'','variant':'default',**default,**presets.get(a.preset,{})}
 if a.config:c.update(json.loads(Path(a.config).read_text()))
 for k in ['title','subtitle','variant','asset','font','glyph','width','height','seed']:
  if getattr(a,k) is not None:c[k]=getattr(a,k)
 if not(64<=c['width']<=8192 and 64<=c['height']<=8192):p.error('width/height must be 64..8192')
 if not isinstance(c['seed'],int) or c['seed']<0:p.error('seed must be a nonnegative integer')
 out=Path(a.output).resolve();out.parent.mkdir(parents=True,exist_ok=True);s=Scene(c);draw(s,c)
 svg=s.svg();out.with_suffix('.svg').write_text(svg)
 import cairosvg
 cairosvg.svg2png(bytestring=svg.encode(),write_to=str(out.with_suffix('.png')))
 out.with_suffix('.json').write_text(json.dumps(c,ensure_ascii=False,indent=2))
 print(out.with_suffix('.png'))
