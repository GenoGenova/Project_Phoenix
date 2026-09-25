# Numen 1 — shell-only model

Based on the approved `../references/numen-helmet-shell-four-views-v2.png` proposal.

- `Numen_1_helmet_shell_v2.blend`: editable Blender 5.2 scene, four shell pieces, neutral clay material, camera and studio lights.
- `Numen_1_helmet_shell_v2.glb`: portable export of only the helmet shells.
- `shell-front.png`, `shell-side.png`, `shell-back.png`, `shell-three-quarter.png`: actual renders of this model.
- `geometry-report.json`: evaluated counts with thickness and bevel modifiers.

The four pieces are the extended cranial cap, pointed face shield, and two cheek shells. The raised rear rim leaves the nape open; the visor is an actual opening. No neck, electronics, ornaments or internal frame are included. Front is -Y and Z is up in Blender. Scale is conceptual, not a fitted human helmet.

This is an initial editable reconstruction of the approved reference, with inferred depth. Thickness and edge rounding remain editable modifiers. No UV textures or animation rig. Separate shells are not a single watertight object for printing. The earlier detailed model is preserved separately.

Rebuild using `../build_shell_v2.py` with Blender in background mode.
