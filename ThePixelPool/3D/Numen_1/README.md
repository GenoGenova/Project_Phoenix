# Numen 1 — base model, first pass

Reference: `../../illustrations/numen-concept-01.png`.

Open `Numen_1_base_v1.blend` in Blender 5.2 or later. The model is an original procedural interpretation of the approved concept, not a scanned or exact reconstruction. Front faces toward -Y; Z is up.

## Contents

- Separate collections for helmet, torso armor, living spine, pelvis, left/right arms and legs, and upper-spine pilot capsule.
- Individually editable armor meshes, compute panels, articulated fingers, joint bearings, organic frame struts and neural channels.
- Ivory ceramic, champagne gold, graphite, titanium and cyan emission materials.
- Packed concept reference (hidden collection), studio lights, camera and plinth.
- `numen-1-front-v1.png` and `numen-1-rear-v1.png`: rendered review views.
- `geometry-report.json`: evaluated model counts including modifiers, excluding studio and reference. The build enforces fewer than 500,000 triangles, a stricter limit than polygon faces.
- `build_numen.py`: reproducible source; running it regenerates the model and renders in this directory.

## Current scope

This is an editable hard-surface concept model with overlapping parts, not a finished game asset. Organic struts intersect at joints instead of forming one continuous manifold surface. Unseen geometry is interpreted from the concept. No animation rig, UV unwrap, baked texture maps, collision mesh or LODs yet. The reference's sculptural armor shapes and fine weathering are simplified for this first pass. The rear capsule uses opaque smoked-blue material to indicate glazing.

Do not use total scene polygon counts as model counts: the report excludes the studio. Preserve this first pass before making sculpting refinements.
