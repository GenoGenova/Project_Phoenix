# NUMEN — Seedance 2.5 shot prompts with audio

Version A uses the original CGI shots. Version B uses the new anime shots. Both are image-to-video animation prompts. Upload only the corresponding shot image for each generation.

Generate 5 seconds per clip (or the nearest supported duration in your app), then trim to the suggested edit lengths below; these total 40 seconds. Duration and 16:9 should also be selected in the app. The five-second timing is our production choice, not a claim about every provider's minimum. Enable generated audio if your interface has that setting.

## Simple audio description

AUDIO: Atmospheric sci-fi ambience, deep machinery, precise mechanical clicks, shimmering neural energy and powerful thrusters, synchronized to the action. No dialogue or voice-over.

For the individual clips below, music is omitted so one continuous soundtrack can be added across the final edit. Optional final-score direction: An original cinematic electronic score, starting with quiet wonder, building through a steady pulse into an uplifting finale; no vocals.

## Research and working method

ByteDance describes multimodal references with distinct roles for appearance, motion, camera and audio: [Seedance 2.5 official announcement](https://seed.bytedance.com/en/blog/one-take-creation-flexible-referencing-introducing-seedance-2-5).

Runware's provider guide separates subject action, camera, lighting and sound in a shot brief: [Seedance 2.5 prompting documentation](https://runware.ai/docs/models/bytedance-seedance-2-5/guides/prompting).

Our application: one reference image and one manageable action per clip; steady cameras for UI shots; explicit sounds tied to visible events; consistent design constraints. Exact UI lettering and identical audio continuity are not guaranteed by prompting. Keep clean interface overlays and a continuous music track in the final edit when exact consistency matters. AUDIO is a plain-language label, not a special command. If uploading a motion-reference clip too, assign it to movement only and keep the image as the design/style reference; use the reference labels shown by your app.

## 01 — Galaxy opening · keep 3s

### A — Original CGI

Reference: [01-pitch-01-galaxy-original-v4.png](../selected-shots-55s/01-pitch-01-galaxy-original-v4.png)

```text
Use the uploaded image as the starting composition and design reference. Preserve identities, proportions, colors and layout. 16:9, one continuous 5-second shot. Animate the subjects and environment, not just a still-image zoom. Complete the main action within the first 3 seconds, then hold naturally. Keep any existing UI text unchanged and screen-anchored; add no captions, cuts or new objects.

STYLE: Preserve the supplied image's premium stylized 3D CGI, soft shading, metal surfaces, lighting and palette.

ACTION AND CAMERA: The small spacecraft glides slowly toward the illuminated planet while its teal engines pulse. Camera drifts gently forward; retain the planet's horizon and distant scale.

AUDIO: A soft cinematic bass swell and faint electronic shimmer; no wind or atmospheric exterior noise. Synchronized effects and ambience only. No music, dialogue or voice-over.
```

### B — Anime

Reference: [01-pitch-01-galaxy-original-v4.png](../selected-shots-anime-v1/01-pitch-01-galaxy-original-v4-anime-v1.png)

```text
Use the uploaded image as the starting composition and design reference. Preserve identities, proportions, colors and layout. 16:9, one continuous 5-second shot. Animate the subjects and environment, not just a still-image zoom. Complete the main action within the first 3 seconds, then hold naturally. Keep any existing UI text unchanged and screen-anchored; add no captions, cuts or new objects.

STYLE: Preserve the supplied image's hand-drawn cyberpunk anime style, precise mechanical ink lines, two-to-three-tone cel shading and painted backgrounds. Animate characters and effects as coherent drawn forms; retain stable linework.

ACTION AND CAMERA: The small spacecraft glides slowly toward the illuminated planet while its teal engines pulse. Camera drifts gently forward; retain the planet's horizon and distant scale.

AUDIO: A soft cinematic bass swell and faint electronic shimmer; no wind or atmospheric exterior noise. Synchronized effects and ambience only. No music, dialogue or voice-over.
```

## 02 — First discovery · keep 4s

### A — Original CGI

Reference: [02-numen-first-discovery-v1.png](../selected-shots-55s/02-numen-first-discovery-v1.png)

```text
Use the uploaded image as the starting composition and design reference. Preserve identities, proportions, colors and layout. 16:9, one continuous 5-second shot. Animate the subjects and environment, not just a still-image zoom. Complete the main action within the first 3 seconds, then hold naturally. Keep any existing UI text unchanged and screen-anchored; add no captions, cuts or new objects.

STYLE: Preserve the supplied image's premium stylized 3D CGI, soft shading, metal surfaces, lighting and palette.

ACTION AND CAMERA: The pilot takes two measured steps toward the towering base Numen. Its visor illuminates and its head inclines slightly toward the pilot. Camera slowly pushes forward from behind the pilot; keep the whole Numen readable.

AUDIO: Bootsteps echo on metal, distant ventilation, heavy servo movement, then a soft neural activation tone. Synchronized effects and ambience only. No music, dialogue or voice-over.
```

### B — Anime

Reference: [02-numen-first-discovery-v1.png](../selected-shots-anime-v1/02-numen-first-discovery-v1-anime-v1.png)

```text
Use the uploaded image as the starting composition and design reference. Preserve identities, proportions, colors and layout. 16:9, one continuous 5-second shot. Animate the subjects and environment, not just a still-image zoom. Complete the main action within the first 3 seconds, then hold naturally. Keep any existing UI text unchanged and screen-anchored; add no captions, cuts or new objects.

STYLE: Preserve the supplied image's hand-drawn cyberpunk anime style, precise mechanical ink lines, two-to-three-tone cel shading and painted backgrounds. Animate characters and effects as coherent drawn forms; retain stable linework.

ACTION AND CAMERA: The pilot takes two measured steps toward the towering base Numen. Its visor illuminates and its head inclines slightly toward the pilot. Camera slowly pushes forward from behind the pilot; keep the whole Numen readable.

AUDIO: Bootsteps echo on metal, distant ventilation, heavy servo movement, then a soft neural activation tone. Synchronized effects and ambience only. No music, dialogue or voice-over.
```

## 03 — Mission preview · keep 2s

### A — Original CGI

Reference: [03-pitch-05-mission-concept-v1.png](../selected-shots-55s/03-pitch-05-mission-concept-v1.png)

```text
Use the uploaded image as the starting composition and design reference. Preserve identities, proportions, colors and layout. 16:9, one continuous 5-second shot. Animate the subjects and environment, not just a still-image zoom. Complete the main action within the first 3 seconds, then hold naturally. Keep any existing UI text unchanged and screen-anchored; add no captions, cuts or new objects.

STYLE: Preserve the supplied image's premium stylized 3D CGI, soft shading, metal surfaces, lighting and palette.

ACTION AND CAMERA: Hold the elevated tactical camera fixed. The ivory Numen at the terminal places its hand against the console; the circular selection marker pulses once and the archive core rotates gently. The other three Numens hold position.

AUDIO: Low machinery ambience, one tactile console click and a short confirmation chime. Synchronized effects and ambience only. No music, dialogue or voice-over.
```

### B — Anime

Reference: [03-pitch-05-mission-concept-v1.png](../selected-shots-anime-v1/03-pitch-05-mission-concept-v1-anime-v1.png)

```text
Use the uploaded image as the starting composition and design reference. Preserve identities, proportions, colors and layout. 16:9, one continuous 5-second shot. Animate the subjects and environment, not just a still-image zoom. Complete the main action within the first 3 seconds, then hold naturally. Keep any existing UI text unchanged and screen-anchored; add no captions, cuts or new objects.

STYLE: Preserve the supplied image's hand-drawn cyberpunk anime style, precise mechanical ink lines, two-to-three-tone cel shading and painted backgrounds. Animate characters and effects as coherent drawn forms; retain stable linework.

ACTION AND CAMERA: Hold the elevated tactical camera fixed. The ivory Numen at the terminal places its hand against the console; the circular selection marker pulses once and the archive core rotates gently. The other three Numens hold position.

AUDIO: Low machinery ambience, one tactile console click and a short confirmation chime. Synchronized effects and ambience only. No music, dialogue or voice-over.
```

## 04 — Squad selection · keep 3s

### A — Original CGI

Reference: [04-squad-selection-concept-v1.png](../selected-shots-55s/04-squad-selection-concept-v1.png)

```text
Use the uploaded image as the starting composition and design reference. Preserve identities, proportions, colors and layout. 16:9, one continuous 5-second shot. Animate the subjects and environment, not just a still-image zoom. Complete the main action within the first 3 seconds, then hold naturally. Keep any existing UI text unchanged and screen-anchored; add no captions, cuts or new objects.

STYLE: Preserve the supplied image's premium stylized 3D CGI, soft shading, metal surfaces, lighting and palette.

ACTION AND CAMERA: Hold the frontal camera fixed on all four Numens. Each makes a subtle idle weight shift while the selected base Numen's teal outline brightens once. Preserve the blue sniper, orange unfinished unit and crowned gold knight; no new equipment.

AUDIO: Hangar ventilation, restrained joint servos and one clean squad-selection beep. Synchronized effects and ambience only. No music, dialogue or voice-over.
```

### B — Anime

Reference: [04-squad-selection-concept-v1.png](../selected-shots-anime-v1/04-squad-selection-concept-v1-anime-v1.png)

```text
Use the uploaded image as the starting composition and design reference. Preserve identities, proportions, colors and layout. 16:9, one continuous 5-second shot. Animate the subjects and environment, not just a still-image zoom. Complete the main action within the first 3 seconds, then hold naturally. Keep any existing UI text unchanged and screen-anchored; add no captions, cuts or new objects.

STYLE: Preserve the supplied image's hand-drawn cyberpunk anime style, precise mechanical ink lines, two-to-three-tone cel shading and painted backgrounds. Animate characters and effects as coherent drawn forms; retain stable linework.

ACTION AND CAMERA: Hold the frontal camera fixed on all four Numens. Each makes a subtle idle weight shift while the selected base Numen's teal outline brightens once. Preserve the blue sniper, orange unfinished unit and crowned gold knight; no new equipment.

AUDIO: Hangar ventilation, restrained joint servos and one clean squad-selection beep. Synchronized effects and ambience only. No music, dialogue or voice-over.
```

## 05 — Cockpit departure · keep 3s

### A — Original CGI

Reference: [05-numen-cockpit-space-carrier-v3.png](../selected-shots-55s/05-numen-cockpit-space-carrier-v3.png)

```text
Use the uploaded image as the starting composition and design reference. Preserve identities, proportions, colors and layout. 16:9, one continuous 5-second shot. Animate the subjects and environment, not just a still-image zoom. Complete the main action within the first 3 seconds, then hold naturally. Keep any existing UI text unchanged and screen-anchored; add no captions, cuts or new objects.

STYLE: Preserve the supplied image's premium stylized 3D CGI, soft shading, metal surfaces, lighting and palette.

ACTION AND CAMERA: Camera advances gently with the Numen toward the wide hexagonal carrier exit. Red alert lights pulse across the cockpit; the planet's horizon stays visible beyond the bay. Preserve the cockpit structure and HUD placement.

AUDIO: Muffled cockpit ventilation, two subdued alert pulses, mounting engine rumble and light mechanical vibration. Synchronized effects and ambience only. No music, dialogue or voice-over.
```

### B — Anime

Reference: [05-numen-cockpit-space-carrier-v3.png](../selected-shots-anime-v1/05-numen-cockpit-space-carrier-v3-anime-v1.png)

```text
Use the uploaded image as the starting composition and design reference. Preserve identities, proportions, colors and layout. 16:9, one continuous 5-second shot. Animate the subjects and environment, not just a still-image zoom. Complete the main action within the first 3 seconds, then hold naturally. Keep any existing UI text unchanged and screen-anchored; add no captions, cuts or new objects.

STYLE: Preserve the supplied image's hand-drawn cyberpunk anime style, precise mechanical ink lines, two-to-three-tone cel shading and painted backgrounds. Animate characters and effects as coherent drawn forms; retain stable linework.

ACTION AND CAMERA: Camera advances gently with the Numen toward the wide hexagonal carrier exit. Red alert lights pulse across the cockpit; the planet's horizon stays visible beyond the bay. Preserve the cockpit structure and HUD placement.

AUDIO: Muffled cockpit ventilation, two subdued alert pulses, mounting engine rumble and light mechanical vibration. Synchronized effects and ambience only. No music, dialogue or voice-over.
```

## 06 — Tactical battle · keep 4s

### A — Original CGI

Reference: [06-pitch-05b-tactical-battle-v1.png](../selected-shots-55s/06-pitch-05b-tactical-battle-v1.png)

```text
Use the uploaded image as the starting composition and design reference. Preserve identities, proportions, colors and layout. 16:9, one continuous 5-second shot. Animate the subjects and environment, not just a still-image zoom. Complete the main action within the first 3 seconds, then hold naturally. Keep any existing UI text unchanged and screen-anchored; add no captions, cuts or new objects.

STYLE: Preserve the supplied image's premium stylized 3D CGI, soft shading, metal surfaces, lighting and palette.

ACTION AND CAMERA: Lock the isometric gameplay camera. The blue sniper releases one brief energy pulse at the central enemy's red shield; the weapon recoils and returns to its starting position. The shield ripples and stabilizes. Keep exactly four allied Numens and two black-red enemies in their existing positions.

AUDIO: A short energy discharge, a sharp electronic shield impact, a fading shield hum and distant machinery; no screams. Synchronized effects and ambience only. No music, dialogue or voice-over.
```

### B — Anime

Reference: [06-pitch-05b-tactical-battle-v1.png](../selected-shots-anime-v1/06-pitch-05b-tactical-battle-v1-anime-v1.png)

```text
Use the uploaded image as the starting composition and design reference. Preserve identities, proportions, colors and layout. 16:9, one continuous 5-second shot. Animate the subjects and environment, not just a still-image zoom. Complete the main action within the first 3 seconds, then hold naturally. Keep any existing UI text unchanged and screen-anchored; add no captions, cuts or new objects.

STYLE: Preserve the supplied image's hand-drawn cyberpunk anime style, precise mechanical ink lines, two-to-three-tone cel shading and painted backgrounds. Animate characters and effects as coherent drawn forms; retain stable linework.

ACTION AND CAMERA: Lock the isometric gameplay camera. The blue sniper releases one brief energy pulse at the central enemy's red shield; the weapon recoils and returns to its starting position. The shield ripples and stabilizes. Keep exactly four allied Numens and two black-red enemies in their existing positions.

AUDIO: A short energy discharge, a sharp electronic shield impact, a fading shield hum and distant machinery; no screams. Synchronized effects and ambience only. No music, dialogue or voice-over.
```

## 07 — Artefact collection · keep 2s

### A — Original CGI

Reference: [07-pitch-06-artefact-collection-v2.png](../selected-shots-55s/07-pitch-06-artefact-collection-v2.png)

```text
Use the uploaded image as the starting composition and design reference. Preserve identities, proportions, colors and layout. 16:9, one continuous 5-second shot. Animate the subjects and environment, not just a still-image zoom. Complete the main action within the first 3 seconds, then hold naturally. Keep any existing UI text unchanged and screen-anchored; add no captions, cuts or new objects.

STYLE: Preserve the supplied image's premium stylized 3D CGI, soft shading, metal surfaces, lighting and palette.

ACTION AND CAMERA: Lock the same tactical camera and cleared arena. The cursor selects the levitating green artefact once; its selection ring expands gently and its orbital data trails accelerate. The four Numens hold position; the artefact stays visible for the following close-up.

AUDIO: A mouse-selection click, a delicate crystalline confirmation chime and a rising digital hum. Synchronized effects and ambience only. No music, dialogue or voice-over.
```

### B — Anime

Reference: [07-pitch-06-artefact-collection-v2.png](../selected-shots-anime-v1/07-pitch-06-artefact-collection-v2-anime-v1.png)

```text
Use the uploaded image as the starting composition and design reference. Preserve identities, proportions, colors and layout. 16:9, one continuous 5-second shot. Animate the subjects and environment, not just a still-image zoom. Complete the main action within the first 3 seconds, then hold naturally. Keep any existing UI text unchanged and screen-anchored; add no captions, cuts or new objects.

STYLE: Preserve the supplied image's hand-drawn cyberpunk anime style, precise mechanical ink lines, two-to-three-tone cel shading and painted backgrounds. Animate characters and effects as coherent drawn forms; retain stable linework.

ACTION AND CAMERA: Lock the same tactical camera and cleared arena. The cursor selects the levitating green artefact once; its selection ring expands gently and its orbital data trails accelerate. The four Numens hold position; the artefact stays visible for the following close-up.

AUDIO: A mouse-selection click, a delicate crystalline confirmation chime and a rising digital hum. Synchronized effects and ambience only. No music, dialogue or voice-over.
```

## 08 — Artefact recovery · keep 3s

### A — Original CGI

Reference: [08-pitch-06-artefact-recovery-v1.png](../selected-shots-55s/08-pitch-06-artefact-recovery-v1.png)

```text
Use the uploaded image as the starting composition and design reference. Preserve identities, proportions, colors and layout. 16:9, one continuous 5-second shot. Animate the subjects and environment, not just a still-image zoom. Complete the main action within the first 3 seconds, then hold naturally. Keep any existing UI text unchanged and screen-anchored; add no captions, cuts or new objects.

STYLE: Preserve the supplied image's premium stylized 3D CGI, soft shading, metal surfaces, lighting and palette.

ACTION AND CAMERA: Camera slowly pushes toward the spinner-shaped green artefact. It rotates a few degrees as data streams travel continuously around its atomic-shaped orbital paths. The Numen's articulated hand reaches slightly closer without touching or obscuring the core.

AUDIO: An airy electronic hum, delicate data ticks and a soft crystalline resonance that rises as the hand approaches. Synchronized effects and ambience only. No music, dialogue or voice-over.
```

### B — Anime

Reference: [08-pitch-06-artefact-recovery-v1.png](../selected-shots-anime-v1/08-pitch-06-artefact-recovery-v1-anime-v1.png)

```text
Use the uploaded image as the starting composition and design reference. Preserve identities, proportions, colors and layout. 16:9, one continuous 5-second shot. Animate the subjects and environment, not just a still-image zoom. Complete the main action within the first 3 seconds, then hold naturally. Keep any existing UI text unchanged and screen-anchored; add no captions, cuts or new objects.

STYLE: Preserve the supplied image's hand-drawn cyberpunk anime style, precise mechanical ink lines, two-to-three-tone cel shading and painted backgrounds. Animate characters and effects as coherent drawn forms; retain stable linework.

ACTION AND CAMERA: Camera slowly pushes toward the spinner-shaped green artefact. It rotates a few degrees as data streams travel continuously around its atomic-shaped orbital paths. The Numen's articulated hand reaches slightly closer without touching or obscuring the core.

AUDIO: An airy electronic hum, delicate data ticks and a soft crystalline resonance that rises as the hand approaches. Synchronized effects and ambience only. No music, dialogue or voice-over.
```

## 09 — Upgrade selection · keep 2s

### A — Original CGI

Reference: [09-upgrade-selection-v1.png](../selected-shots-55s/09-upgrade-selection-v1.png)

```text
Use the uploaded image as the starting composition and design reference. Preserve identities, proportions, colors and layout. 16:9, one continuous 5-second shot. Animate the subjects and environment, not just a still-image zoom. Complete the main action within the first 3 seconds, then hold naturally. Keep any existing UI text unchanged and screen-anchored; add no captions, cuts or new objects.

STYLE: Preserve the supplied image's premium stylized 3D CGI, soft shading, metal surfaces, lighting and palette.

ACTION AND CAMERA: Keep the base Numen on the left and the artefact on the right with a fixed camera. A single bright packet of data travels along their connecting line into the Numen's chest, briefly illuminating its circuitry. Preserve its un-upgraded silhouette.

AUDIO: One interface click, a traveling electronic pulse and a low resonant connection tone. Synchronized effects and ambience only. No music, dialogue or voice-over.
```

### B — Anime

Reference: [09-upgrade-selection-v1.png](../selected-shots-anime-v1/09-upgrade-selection-v1-anime-v1.png)

```text
Use the uploaded image as the starting composition and design reference. Preserve identities, proportions, colors and layout. 16:9, one continuous 5-second shot. Animate the subjects and environment, not just a still-image zoom. Complete the main action within the first 3 seconds, then hold naturally. Keep any existing UI text unchanged and screen-anchored; add no captions, cuts or new objects.

STYLE: Preserve the supplied image's hand-drawn cyberpunk anime style, precise mechanical ink lines, two-to-three-tone cel shading and painted backgrounds. Animate characters and effects as coherent drawn forms; retain stable linework.

ACTION AND CAMERA: Keep the base Numen on the left and the artefact on the right with a fixed camera. A single bright packet of data travels along their connecting line into the Numen's chest, briefly illuminating its circuitry. Preserve its un-upgraded silhouette.

AUDIO: One interface click, a traveling electronic pulse and a low resonant connection tone. Synchronized effects and ambience only. No music, dialogue or voice-over.
```

## 10 — Extreme upgrade · keep 4s

### A — Original CGI

Reference: [10-upgrade-result-extreme-v1.png](../selected-shots-55s/10-upgrade-result-extreme-v1.png)

```text
Use the uploaded image as the starting composition and design reference. Preserve identities, proportions, colors and layout. 16:9, one continuous 5-second shot. Animate the subjects and environment, not just a still-image zoom. Complete the main action within the first 3 seconds, then hold naturally. Keep any existing UI text unchanged and screen-anchored; add no captions, cuts or new objects.

STYLE: Preserve the supplied image's premium stylized 3D CGI, soft shading, metal surfaces, lighting and palette.

ACTION AND CAMERA: Begin with the already-upgraded Numen shown in the reference. Its six articulated wings settle slightly outward and iridescent data feathers illuminate from roots to tips. Camera makes a subtle forward push; preserve all six wings, the helmet and the symmetrical launcher. Finish in a confident hold.

AUDIO: Layered mechanical locks, a rising neural charge, a powerful activation pulse and a soft sustained energy hum. Synchronized effects and ambience only. No music, dialogue or voice-over.
```

### B — Anime

Reference: [10-upgrade-result-extreme-v1.png](../selected-shots-anime-v1/10-upgrade-result-extreme-v1-anime-v1.png)

```text
Use the uploaded image as the starting composition and design reference. Preserve identities, proportions, colors and layout. 16:9, one continuous 5-second shot. Animate the subjects and environment, not just a still-image zoom. Complete the main action within the first 3 seconds, then hold naturally. Keep any existing UI text unchanged and screen-anchored; add no captions, cuts or new objects.

STYLE: Preserve the supplied image's hand-drawn cyberpunk anime style, precise mechanical ink lines, two-to-three-tone cel shading and painted backgrounds. Animate characters and effects as coherent drawn forms; retain stable linework.

ACTION AND CAMERA: Begin with the already-upgraded Numen shown in the reference. Its six articulated wings settle slightly outward and iridescent data feathers illuminate from roots to tips. Camera makes a subtle forward push; preserve all six wings, the helmet and the symmetrical launcher. Finish in a confident hold.

AUDIO: Layered mechanical locks, a rising neural charge, a powerful activation pulse and a soft sustained energy hum. Synchronized effects and ambience only. No music, dialogue or voice-over.
```

## 11 — Carrier expansion · keep 3s

### A — Original CGI

Reference: [11-pitch-08-carrier-isometric-v2.png](../selected-shots-55s/11-pitch-08-carrier-isometric-v2.png)

```text
Use the uploaded image as the starting composition and design reference. Preserve identities, proportions, colors and layout. 16:9, one continuous 5-second shot. Animate the subjects and environment, not just a still-image zoom. Complete the main action within the first 3 seconds, then hold naturally. Keep any existing UI text unchanged and screen-anchored; add no captions, cuts or new objects.

STYLE: Preserve the supplied image's premium stylized 3D CGI, soft shading, metal surfaces, lighting and palette.

ACTION AND CAMERA: Keep the isometric carrier camera fixed. Inside the outlined Neural Lab, one crane lowers a small wall panel into place while the holographic module boundary pulses. Nearby crew walk a few steps. Preserve room positions and the carrier silhouette.

AUDIO: Distant workshop activity, a short crane servo whine, a soft panel-lock clunk and a construction confirmation chime. Synchronized effects and ambience only. No music, dialogue or voice-over.
```

### B — Anime

Reference: [11-pitch-08-carrier-isometric-v2.png](../selected-shots-anime-v1/11-pitch-08-carrier-isometric-v2-anime-v1.png)

```text
Use the uploaded image as the starting composition and design reference. Preserve identities, proportions, colors and layout. 16:9, one continuous 5-second shot. Animate the subjects and environment, not just a still-image zoom. Complete the main action within the first 3 seconds, then hold naturally. Keep any existing UI text unchanged and screen-anchored; add no captions, cuts or new objects.

STYLE: Preserve the supplied image's hand-drawn cyberpunk anime style, precise mechanical ink lines, two-to-three-tone cel shading and painted backgrounds. Animate characters and effects as coherent drawn forms; retain stable linework.

ACTION AND CAMERA: Keep the isometric carrier camera fixed. Inside the outlined Neural Lab, one crane lowers a small wall panel into place while the holographic module boundary pulses. Nearby crew walk a few steps. Preserve room positions and the carrier silhouette.

AUDIO: Distant workshop activity, a short crane servo whine, a soft panel-lock clunk and a construction confirmation chime. Synchronized effects and ambience only. No music, dialogue or voice-over.
```

## 12 — Pilot dialogue · keep 2s

### A — Original CGI

Reference: [12-pitch-09-pilot-dialogue-anime-v2.png](../selected-shots-55s/12-pitch-09-pilot-dialogue-anime-v2.png)

```text
Use the uploaded image as the starting composition and design reference. Preserve identities, proportions, colors and layout. 16:9, one continuous 5-second shot. Animate the subjects and environment, not just a still-image zoom. Complete the main action within the first 3 seconds, then hold naturally. Keep any existing UI text unchanged and screen-anchored; add no captions, cuts or new objects.

STYLE: Preserve the supplied image's premium stylized 3D CGI, soft shading, metal surfaces, lighting and palette.

ACTION AND CAMERA: Hold the over-the-shoulder composition. The seated woman blinks and gives the foreground pilot a small reassuring nod; her clasped hands move naturally and her lips stay closed. Preserve both characters, their outfits and the dialogue interface.

AUDIO: Quiet lounge ventilation, subtle clothing movement and distant hangar ambience; no spoken dialogue. Synchronized effects and ambience only. No music, dialogue or voice-over.
```

### B — Anime

Reference: [12-pitch-09-pilot-dialogue-anime-v2.png](../selected-shots-anime-v1/12-pitch-09-pilot-dialogue-anime-v2-anime-v1.png)

```text
Use the uploaded image as the starting composition and design reference. Preserve identities, proportions, colors and layout. 16:9, one continuous 5-second shot. Animate the subjects and environment, not just a still-image zoom. Complete the main action within the first 3 seconds, then hold naturally. Keep any existing UI text unchanged and screen-anchored; add no captions, cuts or new objects.

STYLE: Preserve the supplied image's hand-drawn cyberpunk anime style, precise mechanical ink lines, two-to-three-tone cel shading and painted backgrounds. Animate characters and effects as coherent drawn forms; retain stable linework.

ACTION AND CAMERA: Hold the over-the-shoulder composition. The seated woman blinks and gives the foreground pilot a small reassuring nod; her clasped hands move naturally and her lips stay closed. Preserve both characters, their outfits and the dialogue interface.

AUDIO: Quiet lounge ventilation, subtle clothing movement and distant hangar ambience; no spoken dialogue. Synchronized effects and ambience only. No music, dialogue or voice-over.
```

## 13 — Corporate factions · keep 2s

### A — Original CGI

Reference: [13-pitch-10-corporate-factions-v1.png](../selected-shots-55s/13-pitch-10-corporate-factions-v1.png)

```text
Use the uploaded image as the starting composition and design reference. Preserve identities, proportions, colors and layout. 16:9, one continuous 5-second shot. Animate the subjects and environment, not just a still-image zoom. Complete the main action within the first 3 seconds, then hold naturally. Keep any existing UI text unchanged and screen-anchored; add no captions, cuts or new objects.

STYLE: Preserve the supplied image's premium stylized 3D CGI, soft shading, metal surfaces, lighting and palette.

ACTION AND CAMERA: Hold the briefing-room camera fixed. The three faction panels remain anchored as illuminated routes sweep across the holographic globe. Ships within the panels drift very slightly and the observers make restrained head movements.

AUDIO: A restrained hologram hum, soft interface ticks and quiet briefing-room ventilation. Synchronized effects and ambience only. No music, dialogue or voice-over.
```

### B — Anime

Reference: [13-pitch-10-corporate-factions-v1.png](../selected-shots-anime-v1/13-pitch-10-corporate-factions-v1-anime-v1.png)

```text
Use the uploaded image as the starting composition and design reference. Preserve identities, proportions, colors and layout. 16:9, one continuous 5-second shot. Animate the subjects and environment, not just a still-image zoom. Complete the main action within the first 3 seconds, then hold naturally. Keep any existing UI text unchanged and screen-anchored; add no captions, cuts or new objects.

STYLE: Preserve the supplied image's hand-drawn cyberpunk anime style, precise mechanical ink lines, two-to-three-tone cel shading and painted backgrounds. Animate characters and effects as coherent drawn forms; retain stable linework.

ACTION AND CAMERA: Hold the briefing-room camera fixed. The three faction panels remain anchored as illuminated routes sweep across the holographic globe. Ships within the panels drift very slightly and the observers make restrained head movements.

AUDIO: A restrained hologram hum, soft interface ticks and quiet briefing-room ventilation. Synchronized effects and ambience only. No music, dialogue or voice-over.
```

## 14 — Final squad flight · keep 3s

### A — Original CGI

Reference: [14-pitch-12-squad-red-planet-v2.png](../selected-shots-55s/14-pitch-12-squad-red-planet-v2.png)

```text
Use the uploaded image as the starting composition and design reference. Preserve identities, proportions, colors and layout. 16:9, one continuous 5-second shot. Animate the subjects and environment, not just a still-image zoom. Complete the main action within the first 3 seconds, then hold naturally. Keep any existing UI text unchanged and screen-anchored; add no captions, cuts or new objects.

STYLE: Preserve the supplied image's premium stylized 3D CGI, soft shading, metal surfaces, lighting and palette.

ACTION AND CAMERA: Track smoothly behind the extreme upgraded Numen, closest to camera, as all four Numens accelerate above the red planet in formation. Thrusters brighten, orbital data ribbons trail behind the six wings and the planet scrolls slowly below. Preserve the other three Numens ahead at distinct distances.

AUDIO: A cinematic thruster surge, shimmering neural energy and a deep rising electronic swell; no wind, dialogue or voice-over. Synchronized effects and ambience only. No music, dialogue or voice-over.
```

### B — Anime

Reference: [14-pitch-12-squad-red-planet-v2.png](../selected-shots-anime-v1/14-pitch-12-squad-red-planet-v2-anime-v1.png)

```text
Use the uploaded image as the starting composition and design reference. Preserve identities, proportions, colors and layout. 16:9, one continuous 5-second shot. Animate the subjects and environment, not just a still-image zoom. Complete the main action within the first 3 seconds, then hold naturally. Keep any existing UI text unchanged and screen-anchored; add no captions, cuts or new objects.

STYLE: Preserve the supplied image's hand-drawn cyberpunk anime style, precise mechanical ink lines, two-to-three-tone cel shading and painted backgrounds. Animate characters and effects as coherent drawn forms; retain stable linework.

ACTION AND CAMERA: Track smoothly behind the extreme upgraded Numen, closest to camera, as all four Numens accelerate above the red planet in formation. Thrusters brighten, orbital data ribbons trail behind the six wings and the planet scrolls slowly below. Preserve the other three Numens ahead at distinct distances.

AUDIO: A cinematic thruster surge, shimmering neural energy and a deep rising electronic swell; no wind, dialogue or voice-over. Synchronized effects and ambience only. No music, dialogue or voice-over.
```
