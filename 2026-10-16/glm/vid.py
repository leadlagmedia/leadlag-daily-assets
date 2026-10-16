from PIL import Image, ImageDraw, ImageFont
import textwrap, subprocess
NAVY=(11,31,58);GOLD=(201,162,39);W=(245,241,230);GREY=(169,180,198)
B='/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf';R='/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf'
def frame(label,lines,size=84,color=W,y0=520):
    im=Image.new('RGB',(1080,1920),NAVY);d=ImageDraw.Draw(im)
    d.rectangle([60,150,1020,158],fill=GOLD)
    d.text((60,100),label,font=ImageFont.truetype(B,40),fill=GOLD)
    f=ImageFont.truetype(B,size);y=y0
    for ln in lines:
        d.text((60,y),ln,font=f,fill=color);y+=int(size*1.3)
    d.text((60,1780),'LEAD-LAG  |  Sources: Investing.com, TheStreet, Oct 15 2026',font=ImageFont.truetype(R,28),fill=GREY)
    return im,d
w=lambda t,n: textwrap.wrap(t,n)
im,d=frame('THE CLAIM',w('The hottest producer prices since 2022 hit Thursday. The 10-year fell anyway.',19),size=88);im.save('f1.png')
im,d=frame('THE MECHANISM',w('Bonds priced the tech selloff, not the print. The 10-year dropped about 10 basis points, its biggest fall since August 2025.',23),size=66);im.save('f2.png')
im,d=frame('THE DATA',[],size=60)
c=Image.open('ppi_vs_10y.png').resize((1000,562));im.paste(c,(40,600))
d.text((60,1260),'Headline PPI 6.3% vs 5.3% expected.',font=ImageFont.truetype(B,46),fill=W)
d.text((60,1330),'The 10-year still closed near 5.09%.',font=ImageFont.truetype(B,46),fill=W);im.save('f3.png')
im,d=frame('THE FALSIFIER',w('This breaks if the 10-year climbs back above 5.33% while stocks are calm.',22),size=72);im.save('f4.png')
im,d=frame('',[],size=60)
d.text((60,720),'The Lead-Lag Report',font=ImageFont.truetype(B,70),fill=GOLD)
d.text((60,860),'Markets as relationships,',font=ImageFont.truetype(R,56),fill=W)
d.text((60,940),'never levels in isolation.',font=ImageFont.truetype(R,56),fill=W)
d.text((60,1100),'leadlagreport.com',font=ImageFont.truetype(B,60),fill=W);im.save('f5.png')
durs=[3,8,8,5,2]
inp=[]
for i,t in enumerate(durs,1): inp+=['-loop','1','-t',str(t),'-i',f'f{i}.png']
fc=''.join(f'[{i}:v]format=yuv420p,setsar=1[v{i}];' for i in range(5))+''.join(f'[v{i}]' for i in range(5))+'concat=n=5:v=1:a=0[out]'
subprocess.run(['ffmpeg','-y',*inp,'-filter_complex',fc,'-map','[out]','-r','30','-c:v','libx264','-crf','26','-preset','medium','-movflags','+faststart','ppi_short.mp4'],check=True,capture_output=True)
Image.open('f1.png').convert('RGB').resize((540,960)).save('ppi_short_thumb.jpg',quality=88)
