# Life of Prophet Muhammad ﷺ: Animated Series

An animated version of the Seerah, built a little at a time from the Higgsfield credits left over at the end of each month. The still-image Reels/Shorts stay the main series; this one grows alongside it and is put together episode by episode once enough clips exist.

## How each monthly run works

1. Check the Higgsfield balance. Keep **10%** back for the still-video series; the rest is this month's animation budget.
2. Open `v01/shotlist.json` and take the next shots with `"status": "todo"`, in order.
3. For each shot:
   - Generate a **keyframe** image in the series style (below), using the still reference and its paragraph as the brief.
   - Animate it into a **5–10 second clip** (image-to-video).
   - Check both against the depiction rules before keeping them. Anything that breaks a rule is regenerated or the shot is redesigned. It is never kept.
4. Save keyframes to `v01/keyframes/` and clips to `v01/clips/` as `<shot id>.png` / `<shot id>.mp4`. Each file must stay under 20 MB so the CDN can serve it.
5. Update each shot in `shotlist.json`: `status` (`done`, or `blocked` with a reason), file paths, `credits_spent`, `month`.
6. Stop when the budget is spent. Never dip into the 10% reserve.
7. Report: shots finished, credits spent, credits left, and the next shot in line.

When every shot in an episode is `done`, the episode is ready to assemble. That means the clips cut to the existing episode narration and recitation audio, with the same Arabic/English cards, logo, titles and layout as the still series. Arabic text is never drawn by an image or video model. It is always composited (Amiri font).

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

- `v01/shotlist.json`: one entry per shot (75 for Volume 1). Each shot links to its episode, scene, story paragraph and the still image used in the Reels.
- `v01/keyframes/`, `v01/clips/`: generated output.
- Audio and still references live in the main production workspace and the `seerah-reels` branch.
