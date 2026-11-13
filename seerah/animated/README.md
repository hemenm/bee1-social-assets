# Life of Prophet Muhammad ﷺ: Animated Series

An animated version of the Seerah, built a little at a time from the Higgsfield credits left over at the end of each month. The still-image Reels/Shorts stay the main series; this one grows alongside it and is put together episode by episode once enough clips exist.

## How each monthly run works

Volume 1 is animated **one episode at a time, in order**, using the same tools as the "Stories of the Prophets" animated series: Nano Banana Pro keyframes and Seedance 2.5 video. Each finished episode is fully animated from start to end and cut to its existing narration.

1. Check the Higgsfield balance. Keep **10%** back for the still-video series; the rest is this month's animation budget.
2. Open `v01/shotlist.json` and take the first episode whose status is not `done`.
3. **Beat plan** (once per episode, before generating anything). Use `v01/source/epNN.audio.json` (paragraph timings), `epNN.episode.json` (the text), and `epNN.mp3` (the narration) to map the whole runtime into shots. Each shot is 4 to 15 seconds, and long takes are welcome where the narration lingers. Reuse a shot already made for the volume wherever it fits instead of generating a new one. Save the plan to `v01/beats/epNN.json`: one entry per shot with start, end, paragraph(s), a description, status `todo`, and the clip file once made.
4. For each shot in the beat plan, in order:
   - **Keyframe**: Nano Banana Pro, 2K, 16:9, in the series style below (about 2 credits).
   - Check the keyframe against the depiction rules before animating it. Anything that breaks a rule is regenerated or the shot redesigned; it is never kept.
   - **Clip**: Seedance 2.5 (`seedance_2_5`) from the keyframe as start frame, `mode: std`, `1080p`, `generate_audio: false`, duration matched to the beat (about 72 credits per 8 seconds). Check the finished clip against the same rules.
5. Save keyframes to `v01/keyframes/epNN/` and clips to `v01/clips/epNN/`, named by shot number. Keep each file under 20 MB.
6. Update the beat plan and `shotlist.json` (episode status `in progress` or `done`, credits spent, month) and commit as you go.
7. Stop when the budget is spent. Never dip into the 10% reserve. A half-finished episode simply continues next month.
8. Report: shots finished, credits spent, credits left, and whether an episode is now complete.

When an episode is `done`, it is assembled: the clips are cut to the episode narration and recitation, with the same Arabic/English cards, logo, titles and layout as the still series. Arabic text is never drawn by an image or video model. It is always composited (Amiri font). The animation is made at 16:9; vertical versions are cropped from it.

## Style

**3D animated film.** Feature-animation quality CG: soft global illumination, warm golden-hour and moonlit palettes, stylised but grounded proportions, rich textures (sand, stone, cloth, palm). Arabian Peninsula, 6th century: no modern objects, no anachronistic architecture. Camera moves are slow and deliberate. Landscape and atmosphere shots may drift dreamily. Narrative action stays at natural speed.

Use the same style words in every prompt so the series stays consistent. Once the first approved keyframes exist, use them as reference images for later shots.

## Depiction rules (mandatory)

- **Prophets** (Muhammad ﷺ, Ibrahim, Isma'il and every other prophet): never shown in any form. That includes no silhouette, no hands, no shadow and no back view. Their presence is told through the camera's point of view, the environment and the people around them.
- **Prophets' wives** (e.g. Hajar, both of Isma'il's wives, Khadijah and the other Mothers of the Believers): never shown in any form, the same as prophets.
- **Angels**: never shown in any form. Their presence is light and stillness only.
- **Everyone else** may be fully animated, including the Prophet ﷺ's relatives who are not wives: Abd al-Muttalib, Abdullah, Amina, as well as Abraha, Qusayy, Jurhum, Khuza'a, Quraysh, soldiers and townspeople.
- **Modesty**: every woman shown has her hair covered and sleeves to the wrist, with only the hands uncovered.
- **No implied depiction**: no figure may appear on screen in a way that suggests it is a prophet, for example under a prophet's name or in a prophet's place in the story.

## Files

- `v01/shotlist.json`: progress per episode, plus `scene_reference`, the scenes used by the still series (useful as composition ideas).
- `v01/source/`: each episode's narration audio, paragraph timings and text.
- `v01/beats/`: the beat plan for each episode.
- `v01/keyframes/`, `v01/clips/`: generated output.
