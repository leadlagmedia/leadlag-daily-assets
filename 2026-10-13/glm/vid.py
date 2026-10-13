from PIL import Image, ImageDraw, ImageFont
import textwrap, subprocess
NAVY=(11,31,58);GOLD=(201,162,39);W=(245,241,230);GREY=(169,180,198)
B='/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf';R='/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf'
def frame(name,label,lines,size=84,color=W,extra=None):
    im=Image.new('RGB',(1080,1920),NAVY);d=ImageDraw.Draw(im)
    d.rectangle([60,150,1020,158],fill=GOLD)
    d.text((60,100),label,font=ImageFont.truetype(B,40),fill=GOLD)
    f=ImageFont.truetype(B,size);y=extra or 520
    for ln in lines:
        d.text((60,y),ln,font=f,fill=color);y+=int(size*1.3)
    d.text((60,1780),'LEAD-LAG  |  Source: Wells Fargo 3Q26 results, Oct 13 2026',font=ImageFont.truetype(R,30),fill=GREY)
    return im,d
def wrap(t,n): return textwrap.wrap(t,n)
fr=[]
im,d=frame('1','THE CLAIM',wrap('Wells Fargo grew loans 11% and interest income only 5%.',18),size=92);im.save('f1.png')
im,d=frame('2','THE MECHANISM',wrap('The spread is thinner, and credit costs jumped 51%: provision for credit losses went from $681M to $1.03B.',22),size=72);im.save('f2.png')
im,d=frame('3','THE DATA',[],size=60)
c=Image.open('wfc_credit.png').resize((1000,562));im.paste(c,(40,600));
d.text((60,1260),'Revenue grew only 2%.',font=ImageFont.truetype(B,64),fill=W);im.save('f3.png')
im,d=frame('4','THE FALSIFIER',wrap('This breaks if provisions fall back below $700M while the 10-year stays above 5%.',22),size=72);im.save('f4.png')
im,d=frame('5','',[],size=60)
d.text((60,720),'The Lead-Lag Report',font=ImageFont.truetype(B,70),fill=GOLD)
d.text((60,860),'Markets as relationships,',font=ImageFont.truetype(R,56),fill=W)
d.text((60,940),'never levels in isolation.',font=ImageFont.truetype(R,56),fill=W)
d.text((60,1100),'leadlagreport.com',font=ImageFont.truetype(B,60),fill=W);im.save('f5.png')
inp=[]
for i in range(1,6): inp+=['-loop','1','-t','6','-i',f'f{i}.png']
fc=''.join(f'[{i}:v]format=yuv420p,setsar=1[v{i}];' for i in range(5))+''.join(f'[v{i}]' for i in range(5))+'concat=n=5:v=1:a=0[out]'
subprocess.run(['ffmpeg','-y',*inp,'-filter_complex',fc,'-map','[out]','-r','30','-c:v','libx264','-crf','26','-preset','medium','-movflags','+faststart','wfc_short.mp4'],check=True,capture_output=True)
Image.open('f1.png').convert('RGB').resize((540,960)).save('wfc_short_thumb.jpg',quality=88)
