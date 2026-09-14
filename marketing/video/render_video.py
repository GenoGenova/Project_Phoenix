import sys,json,subprocess,wave,textwrap,concurrent.futures
from pathlib import Path
from PIL import Image,ImageDraw,ImageFont,ImageFilter
import numpy as np
ROOT=Path(__file__).resolve().parent
sys.path.insert(0,str(ROOT/'tools'))
import imageio_ffmpeg
FF=imageio_ffmpeg.get_ffmpeg_exe()
WORK=ROOT/'render-work'; WORK.mkdir(exist_ok=True)
ART=ROOT.parents[1]/'ThePixelPool'/'illustrations'
scenes=json.loads((ROOT/'cut-55s.json').read_text())
def run(args):
 p=subprocess.run([FF,'-hide_banner','-loglevel','error','-y',*map(str,args)],capture_output=True,text=True)
 if p.returncode: raise RuntimeError(p.stderr)
def font(size): return ImageFont.truetype('C:/Windows/Fonts/segoeui.ttf',size)
def render(item):
 i,(duration,name,title,line)=item
 img=Image.open(ART/name).convert('RGB')
 bg=img.resize((1920,1080)).filter(ImageFilter.GaussianBlur(30))
 bg=Image.blend(bg,Image.new('RGB',bg.size,'#080e13'),.65)
 img.thumbnail((1920,910),Image.Resampling.LANCZOS)
 bg.paste(img,((1920-img.width)//2,35))
 bg.save(WORK/f'frame-{i:02}.png')
 overlay=Image.new('RGBA',(1920,1080)); d=ImageDraw.Draw(overlay)
 d.rectangle((0,950,1920,1080),fill=(8,14,19,255))
 d.text((44,10),'PROJECT PHOENIX  /  CONCEPT TRAILER',font=font(17),fill='#e8bd77')
 d.text((1875,10),f'{i+1:02} / 14',font=font(17),fill='#aebcc4',anchor='ra')
 d.text((960,957),title,font=font(23),fill='#87e3d4',anchor='mt')
 lines=textwrap.wrap(line,width=100)
 for k,l in enumerate(lines): d.text((960,995+k*34),l,font=font(29),fill='#f4f0e8',anchor='mt')
 d.rectangle((0,1076,int(1920*(i+1)/14),1079),fill='#87e3d4')
 overlay.save(WORK/f'overlay-{i:02}.png')
 with wave.open(str(WORK/f'voice-{i:02}.wav')) as w: length=w.getnframes()/w.getframerate()
 speed=max(1,length/(duration-.55))
 (WORK/f'voice-{i:02}-duration.txt').write_text(str(length))
 # The frame inset leaves room for captions; slow motion remains behind the stationary overlay.
 filt=f"[0:v]zoompan=z='min(zoom+0.000035,1.012)':x='iw/2-iw/zoom/2':y='ih/2-ih/zoom/2':d={duration*24}:s=1920x1080:fps=24[v];[v][1:v]overlay=0:0,fade=t=in:st=0:d=0.18,fade=t=out:st={duration-.18}:d=0.18[out];[2:a]atempo={speed},adelay=180:all=1,apad,atrim=0:{duration},afade=t=out:st={duration-.12}:d=0.12[a]"
 run(['-i',WORK/f'frame-{i:02}.png','-i',WORK/f'overlay-{i:02}.png','-i',WORK/f'voice-{i:02}.wav','-filter_complex',filt,'-map','[out]','-map','[a]','-t',duration,'-c:v','libx264','-preset','fast','-crf','20','-pix_fmt','yuv420p','-threads','2','-c:a','aac','-b:a','192k','-ar','48000',WORK/f'scene-{i:02}.mp4'])
 print(f'Rendered {i+1}/14',flush=True)
 return i
with concurrent.futures.ThreadPoolExecutor(max_workers=2) as pool: list(pool.map(render,enumerate(scenes)))
listing=WORK/'concat.txt';listing.write_text('\n'.join(f"file 'scene-{i:02}.mp4'" for i in range(len(scenes))))
run(['-f','concat','-safe','0','-i',listing,'-c','copy',WORK/'joined.mp4'])
# Subtle original tonal ambience, kept far below narration.
rate=48000;n=55*rate;t=np.arange(n)/rate
bed=np.zeros(n)
for hz,amp in [(55,.012),(82.4069,.008),(110,.004),(164.8138,.002)]: bed+=amp*np.sin(2*np.pi*hz*t)*(.75+.25*np.sin(2*np.pi*.09*t))
bed*=np.minimum(t/2,1)*np.minimum((55-t)/3,1)
with wave.open(str(WORK/'ambience.wav'),'wb') as w:
 w.setnchannels(1);w.setsampwidth(2);w.setframerate(rate);w.writeframes((bed*32767).astype('<i2').tobytes())
out=ROOT/'Project-Phoenix-presentation-55s-v1.mp4'
run(['-i',WORK/'joined.mp4','-i',WORK/'ambience.wav','-filter_complex','[0:a][1:a]amix=inputs=2:duration=first:normalize=0,alimiter=limit=0.9[a]','-map','0:v','-map','[a]','-c:v','copy','-c:a','aac','-b:a','192k','-t','55','-movflags','+faststart',out])
def stamp(s): return f'00:{int(s)//60:02}:{int(s)%60:02},000'
cursor=0;subs=[]
for i,(dur,name,title,line) in enumerate(scenes):
 subs.append(f'{i+1}\n{stamp(cursor)} --> {stamp(cursor+dur)}\n{line}\n');cursor+=dur
(ROOT/'Project-Phoenix-presentation-55s-v1.srt').write_text('\n'.join(subs),encoding='utf-8')
run(['-i',out,'-ss','00:00:36','-frames:v','1',ROOT/'presentation-preview.jpg'])
print(out,flush=True)
