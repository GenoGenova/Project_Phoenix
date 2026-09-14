"""Assemble the reviewed Runway exports into a 40-second clean picture cut."""
from pathlib import Path
import sys, subprocess, json
root=Path(__file__).resolve().parent
sys.path.insert(0,str(root/'tools'))
import imageio_ffmpeg
ff=imageio_ffmpeg.get_ffmpeg_exe()
work=root/'render-work/runway-cut';work.mkdir(parents=True,exist_ok=True)
# filename number, duration, title, optional narration/subtitle
shots=[
 (14,3,'Galaxy opening','Far from Earth, a new future awaits.'),
 (13,4,'Discover Numens','Awaken your Numen: a living frame, guided by your pilot.'),
 (12,2,'Mission preview','Explore a divided galaxy.'),
 (11,3,'Squad selection','Build your squad of four.'),
 (10,3,'Cockpit departure','Lead them into the unknown.'),
 (9,4,'Tactical battle','Use cover. Coordinate abilities. Make every move count.'),
 (8,2,'Artefact collection','Recover Neural Artefacts.'),
 (7,3,'Neural Artefact','Knowledge with the power to transform.'),
 (6,2,'Upgrade selection','Link. Adapt. Evolve.'),
 (5,4,'Extreme upgrade','Unlock new equipment, abilities, and a second form.'),
 (4,3,'Carrier expansion','Expand your carrier. Build your home.'),
 (2,2,'Pilot stories','Discover your pilots\' stories.'),
 (1,2,'Corporate factions','Face competing visions of survival.'),
 (15,3,'Next horizon','NUMEN. Your next horizon.'),
]
def run(args):
    p=subprocess.run([ff,'-hide_banner','-loglevel','error','-y',*map(str,args)],capture_output=True,text=True)
    if p.returncode:raise RuntimeError(p.stderr)
timeline=[];cursor=0
for i,(n,dur,title,line) in enumerate(shots):
    source=root/'RunwayExport'/f'PitchRawVideo-{n:02}.mp4'
    # Straight cuts preserve total timing and the existing UI. Uniform 1080p24 exports.
    vf='scale=1920:1080:force_original_aspect_ratio=decrease,pad=1920:1080:(ow-iw)/2:(oh-ih)/2,setsar=1,fps=24'
    if i==0:vf+=',fade=t=in:st=0:d=0.3'
    if i==len(shots)-1:vf+=f',fade=t=out:st={dur-.5}:d=0.5'
    run(['-i',source,'-an','-t',dur,'-vf',vf,'-c:v','libx264','-crf','18','-preset','fast','-pix_fmt','yuv420p','-threads','4',work/f'{i:02}.mp4'])
    timeline.append(dict(shot=i+1,source=source.name,start=cursor,duration=dur,title=title,narration=line));cursor+=dur
    print(f'Assembled {i+1}/14: {title}',flush=True)
assert cursor==40
(work/'concat.txt').write_text('\n'.join(f"file '{i:02}.mp4'" for i in range(len(shots))))
output=root/'NUMEN-Runway-trailer-40s-v1.mp4'
run(['-f','concat','-safe','0','-i',work/'concat.txt','-c','copy','-movflags','+faststart',output])
(root/'NUMEN-Runway-trailer-40s-v1-timeline.json').write_text(json.dumps(timeline,indent=2))
def stamp(t):return f'00:00:{t:02d},000'
(root/'NUMEN-Runway-trailer-40s-v1.srt').write_text('\n\n'.join(f"{i+1}\n{stamp(s['start'])} --> {stamp(s['start']+s['duration'])}\n{s['narration']}" for i,s in enumerate(timeline)),encoding='utf-8')
run(['-ss','27','-i',output,'-frames:v','1',root/'NUMEN-Runway-trailer-preview.jpg'])
print(output,flush=True)
