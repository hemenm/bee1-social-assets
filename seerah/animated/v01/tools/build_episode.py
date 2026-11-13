import json, subprocess, re, os, sys
V='/home/claude/bee1-social-assets/seerah/animated/v01'
B=os.path.dirname(os.path.abspath(__file__))  
plan=json.load(open(f'{V}/beats/ep01.json'))
X=0.5
segs=[]
for i,s in enumerate(plan['shots']):
    src=s['clip'].split(' ')[0]; src=f'{V}/{src}'
    D=s['end']-s['start']; L=D+(X if i<len(plan['shots'])-1 else 0)
    avail=float(subprocess.run(['ffprobe','-v','error','-show_entries','format=duration','-of','csv=p=0',src],capture_output=True,text=True).stdout)-0.05
    f=max(1.0,L/avail)  # slow down only if clip is too short
    out=f'{B}/seg{i:02d}.mp4'
    vf=f"setpts={f:.4f}*PTS,fps=24,scale=1920:1080:force_original_aspect_ratio=increase,crop=1920:1080,setsar=1,format=yuv420p"
    if not os.path.exists(out): subprocess.run(['ffmpeg','-v','error','-y','-i',src,'-an','-vf',vf,'-t',f'{L:.3f}','-c:v','libx264','-crf','14','-preset','fast',out],check=True)
    segs.append((out,L)); print(i+1, round(D,2), round(L,2), 'speed', round(1/f,2))
inputs=sum([['-i',p] for p,_ in segs],[])
fl=[]; prev='[0:v]'; off=0
for i in range(1,len(segs)):
    off+=segs[i-1][1]-X
    lab=f'[x{i}]'
    fl.append(f'{prev}[{i}:v]xfade=transition=fade:duration={X}:offset={off:.3f}{lab}'); prev=lab
total=sum(L for _,L in segs)-X*(len(segs)-1)
fl.append(f'{prev}fade=t=in:st=0:d=0.8,fade=t=out:st={total-1.2:.3f}:d=1.2[v]')
subprocess.run(['ffmpeg','-v','error','-y',*inputs,'-filter_complex',';'.join(fl),'-map','[v]','-c:v','libx264','-crf','16','-preset','veryfast','-threads','0','-pix_fmt','yuv420p',f'{B}/video.mp4'],check=True)
print('total',round(total,2))
