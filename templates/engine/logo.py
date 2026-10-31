from PIL import Image; import numpy as np, os
src='/mnt/user-data/attachments/7d6cbad4-c8ea-5342-8fb9-d9ade73834bf/31c60111-image.png'
a=np.array(Image.open(src).convert('RGB')).astype(float)
bg=np.median(np.concatenate([a[5:60,5:60].reshape(-1,3),a[5:60,-60:-5].reshape(-1,3)]),0)
y0,y1,x0,x1=140,750,180,1090
c=a[y0:y1,x0:x1]; H,W,_=c.shape
split=422-y0
# letters alpha via luminance
lum=c@[0.299,0.587,0.114]; bl=bg@[0.299,0.587,0.114]
letter=np.array([84,40,22.]) # approx brown
ll=letter@[0.299,0.587,0.114]
la=np.clip((bl-lum)/(bl-ll),0,1); la[:split]=0; la[la<0.06]=0
# flag alpha via max channel distance, top part only
d=np.abs(c-bg).max(2); fa=np.clip((d-6)/90,0,1); fa[split:]=0
# also flag pixels whose lum is dark inside top
fa=np.maximum(fa,np.where(np.arange(H)[:,None]<split,la*0+np.clip((bl-lum)/(bl-ll),0,1),0))
fa=np.clip(fa,0,1); fa[fa<0.08]=0
from scipy import ndimage
solid=ndimage.binary_fill_holes(ndimage.binary_closing(fa>0.5,iterations=2))
holes=solid&(fa<0.6)
star=np.zeros_like(fa); star[holes]=1
star=np.maximum(star, np.where(solid,(1-fa),0)*(solid))
star=np.clip(star*ndimage.binary_erosion(solid,iterations=1),0,1)
fa=np.where(solid,np.maximum(fa,star),fa)
# band classification
hue=c[...,0]-c[...,2]
safe=np.maximum(fa,1e-3)[...,None]
fcol=np.clip((c-bg*(1-safe))/safe,0,255)
def build(letter_rgb, flag_mode='color', flag_rgb=None):
    out=np.zeros((H,W,4))
    out[...,:3]=letter_rgb; out[...,3]=la*255
    m=fa>0
    if flag_mode=='color':
        out[m,:3]=fcol[m]
        sm=star>0.02
        out[sm,:3]=out[sm,:3]*(1-star[sm,None])+255*star[sm,None]
        out[m,3]=fa[m]*255
    else:
        out[m,:3]=flag_rgb
        # tonal bands: yellow light, blue full, red mid; stars knocked out
        cc=fcol
        yel=(cc[...,0]>200)&(cc[...,1]>150); blu=(cc[...,2]>cc[...,0]+30); 
        w=np.full((H,W),0.72); w[yel]=0.42; w[blu]=1.0
        w=ndimage.uniform_filter(w,3)
        out[m,3]=(fa[m]*w[m]*(1-star[m]))*255
    im=Image.fromarray(out.astype(np.uint8),'RGBA')
    bb=im.getbbox(); return im.crop(bb)
os.makedirs('brand/logo',exist_ok=True)
V={'original-brown':((91,52,32),'color',None),
 'white-colorflag':((255,255,255),'color',None),
 'black-colorflag':((17,17,17),'color',None),
 'espresso-colorflag':((48,40,32),'color',None),
 'mono-white':((255,255,255),'mono',(255,255,255)),
 'mono-black':((17,17,17),'mono',(17,17,17)),
 'mono-espresso':((48,40,32),'mono',(48,40,32)),
 'mono-sand':((214,196,172),'mono',(214,196,172))}
for k,(l,mode,f) in V.items():
    im=build(np.array(l,float),mode,np.array(f,float) if f else None)
    im.save(f'brand/logo/vzla-rising-wordmark-{k}.png')
print(im.size, bg)
