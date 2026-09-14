from pathlib import Path
import sys, subprocess, re, json
from PIL import Image, ImageDraw, ImageFont
root=Path(__file__).resolve().parent
sys.path.insert(0,str(root/'tools'))
import imageio_ffmpeg
ff=imageio_ffmpeg.get_ffmpeg_exe()
out=root/'render-work/runway';out.mkdir(parents=True,exist_ok=True)
files=sorted((root/'RunwayExport').glob('*.mp4'))
sheet=Image.new('RGB',(1000,len(files)*150),'#101820');draw=ImageDraw.Draw(sheet)
font=ImageFont.truetype('C:/Windows/Fonts/segoeui.ttf',16)
reports=[]
for row,f in enumerate(files):
    probe=subprocess.run([ff,'-hide_banner','-i',str(f)],capture_output=True,text=True).stderr
    match=re.search(r'Duration: (\d+):(\d+):(\d+\.\d+)',probe);h,m,s=map(float,match.groups());dur=h*3600+m*60+s
    reports.append({'file':f.name,'duration':dur,'audio':'Audio:' in probe,'streams':probe})
    draw.text((5,row*150+8),f.stem,font=font,fill='white');draw.text((5,row*150+34),str(dur)+' sec',font=font,fill='white')
    for j,t in enumerate([.2,dur*.5,max(.2,dur-.3)]):
        target=out/f'{f.stem}-{j}.jpg'
        subprocess.run([ff,'-loglevel','error','-y','-ss',str(t),'-i',str(f),'-frames:v','1','-vf','scale=256:144',str(target)],check=True)
        sheet.paste(Image.open(target),(215+j*260,row*150))
sheet.save(out/'contact-sheet.jpg');(out/'probe.json').write_text(json.dumps(reports,indent=2))
print(json.dumps([{k:v for k,v in r.items() if k!='streams'} for r in reports],indent=2))
