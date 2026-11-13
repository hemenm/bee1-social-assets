import json
from PIL import ImageFont, Image, ImageDraw
V='/home/claude/bee1-social-assets/seerah/animated/v01'
ep=json.load(open(f'{V}/source/ep01.episode.json')); au=json.load(open(f'{V}/source/ep01.audio.json'))
AR=ImageFont.truetype('/root/.fonts/Amiri-full.ttf',57,layout_engine=ImageFont.Layout.RAQM)
EN=ImageFont.truetype('/usr/share/fonts/opentype/inter/Inter-Regular.otf',31)
def wrap(text,font,maxw,rtl=False):
    words=text.split(); lines=[]; cur=''
    for w in words:
        t=(cur+' '+w).strip()
        wd=font.getlength(t,direction='rtl') if rtl else font.getlength(t)
        if wd>maxw and cur: lines.append(cur); cur=w
        else: cur=t
    lines.append(cur); return lines
def ts(t):
    h=int(t//3600); m=int(t%3600//60); s=t%60; return f'{h}:{m:02d}:{s:05.2f}'
cards=au['cards']; P=ep['paragraphs']; total=155.17
ev=[]
for i,c in enumerate(cards):
    p=P[c['paragraph']-1]
    st=c['start']-0.15; en=(cards[i+1]['start']-0.15) if i+1<len(cards) else total-0.3
    ar=p['ar'].replace('⁠','')
    arl=wrap(ar,AR,1560,True); enl=wrap(p['en'],EN,1500)
    cite=None
    if p.get('voice')=='quran': cite=f"QUR'AN {p['quran'].replace(':',' : ')}   ·   RECITATION: SHAYKH ABDULAZIZ SALAR RASOUL"
    y=1030; parts=[]
    if cite: parts.append((f'{{\\an2\\pos(960,{y})\\fnInter\\fs22\\c&H7CC8E8&\\fsp2}}{cite}')); y-=40
    parts.append(f'{{\\an2\\pos(960,{y})\\fnInter\\fs31\\c&HE6E6E6&}}'+'\\N'.join(enl)); y-=len(enl)*40+14
    parts.append(f'{{\\an2\\pos(960,{y})\\fnAmiri\\fs100\\c&HFFFFFF&}}'+'\\N'.join(arl))
    for t in parts: ev.append(f'Dialogue: 0,{ts(st)},{ts(en)},Base,,0,0,0,,{{\\fad(250,250)}}'+t)
# title
T=[('{\\an8\\pos(960,70)\\fnInter\\fs28\\fsp6\\c&HDDDDDD&}LIFE OF PROPHET MUHAMMAD {\\fnAmiri\\fs56\\fsp0}ﷺ'),
   ('{\\an8\\pos(960,128)\\fnInter\\fs24\\fsp3\\c&H7CC8E8&}VOLUME 1  ·  EPISODE 1'),
   ('{\\an8\\pos(960,165)\\fnAmiri\\fs130\\c&HFFFFFF&}'+ep['title_ar']),
   ('{\\an8\\pos(960,300)\\fnInter\\fs38\\c&HFFFFFF&}'+ep['title_en'])]
for t in T: ev.append(f'Dialogue: 1,{ts(0.8)},{ts(7.5)},Base,,0,0,0,,{{\\fad(700,700)}}'+t)
hdr="""[Script Info]
ScriptType: v4.00+
PlayResX: 1920
PlayResY: 1080
WrapStyle: 2
ScaledBorderAndShadow: yes

[V4+ Styles]
Format: Name, Fontname, Fontsize, PrimaryColour, SecondaryColour, OutlineColour, BackColour, Bold, Italic, Underline, StrikeOut, ScaleX, ScaleY, Spacing, Angle, BorderStyle, Outline, Shadow, Alignment, MarginL, MarginR, MarginV, Encoding
Style: Base,Inter,31,&H00FFFFFF,&H00FFFFFF,&H64000000,&H96000000,0,0,0,0,100,100,0,0,1,0.6,1.6,2,60,60,40,1

[Events]
Format: Layer, Start, End, Style, Name, MarginL, MarginR, MarginV, Effect, Text
"""
open('ep01.ass','w').write(hdr+'\n'.join(ev)+'\n')
# bottom gradient + top vignette for title
g=Image.new('RGBA',(1920,1080),(0,0,0,0)); d=ImageDraw.Draw(g)
for y in range(560,1080):
    a=int(170*((y-560)/520)**1.4); d.line([(0,y),(1920,y)],fill=(0,0,0,a))
g.save('grad.png')
tg=Image.new('RGBA',(1920,1080),(0,0,0,0)); d=ImageDraw.Draw(tg)
for y in range(0,420):
    a=int(150*(1-y/420)**1.3); d.line([(0,y),(1920,y)],fill=(0,0,0,a))
tg.save('topgrad.png')
print(len(ev))
