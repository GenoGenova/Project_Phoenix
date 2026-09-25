# Numen helmet — blueprint comparison revision

Open `Numen_1_helmet_shell_v3.blend` for the complete editable assembly.

## Separate parts

Each part has its own GLB export and Blender library file: `01-cranium`, `02-face`, `03-left-cheek`, `04-right-cheek`. The individual Blender library files can be appended through File > Append > Object. Parts preserve assembled coordinates for alignment.

## Blueprint board

The collection `BLUEPRINTS | aligned reference planes` contains front, side, back and three-quarter reference boards. Enable its viewport visibility in the Outliner. Each board displays one quadrant of the approved sheet using UV cropping, with the original image packed inside the blend file. No external image paths are needed.

Front is -Y, side is viewed from +X, and Z is up. Use Blender front/right/back orthographic views and X-ray to compare. Boards are hidden from beauty renders. The comparison PNGs show actual mesh wireframes over the reference.

## Fit and limits

The crown, forehead, rear volume and chin were adjusted using measured image landmarks and rendered comparisons. The original generated views are not perfectly consistent orthographic drawings: the side view includes perspective and different feature projections. This remains an approximate reconstruction, not an exact match. Comparison images intentionally expose remaining differences for review.

The model contains only four plain shell pieces, with editable thickness and bevels. No internal mechanisms or decoration. This revision preserves the earlier models.
