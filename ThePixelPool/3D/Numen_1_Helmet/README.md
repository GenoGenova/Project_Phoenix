# Numen 1 — standalone helmet

Editable concept-model first pass, derived from the helmet in `../Numen_1/Numen_1_base_v1.blend`, with a corrected solid crest and fitted brow inlays. The full-body original is unchanged.

- `Numen_1_helmet_v1.blend`: separate armor, visor, trim and neck-interface parts; materials, studio lights and camera. Open in Blender 5.2 or later.
- `Numen_1_helmet_v1.glb`: portable model with materials, excluding studio and camera.
- `helmet-three-quarter-v1.png`, `helmet-front-v1.png`, `helmet-rear-v1.png`: rendered review views.
- `geometry-report.json`: evaluated mesh counts including modifiers: 8,600 polygons / 16,756 triangles across 115 mesh parts.

Front faces -Y and Z is up in Blender. The root sits at the neck attachment; the small neck interface can be hidden or removed separately. Scale follows the original Numen model, not wearable human dimensions.

This is a simplified 3D interpretation of `../../illustrations/numen-concept-01.png`, not an exact reconstruction. It has no UV unwrap, baked textures, animation rig or production retopology. Overlapping mechanical parts are intentional; it is not a watertight print-ready model.

`build_helmet.py` reproduces the files using Blender in background mode. It requires the original base-model file at the relative path above.
