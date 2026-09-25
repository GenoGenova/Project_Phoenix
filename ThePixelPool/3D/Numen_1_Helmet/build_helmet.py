"""Create a standalone editable helmet from the approved Numen first-pass model."""
import bpy, json, math
from pathlib import Path
from mathutils import Vector
OUT = Path(__file__).resolve().parent
bpy.ops.wm.open_mainfile(filepath=str(OUT.parent/'Numen_1/Numen_1_base_v1.blend'))
scene = bpy.context.scene
helmet = bpy.data.collections['01 Helmet']
keep = set(helmet.objects)
for o in list(bpy.data.objects):
    if o not in keep: bpy.data.objects.remove(o, do_unlink=True)
for c in list(bpy.data.collections):
    if c != helmet: bpy.data.collections.remove(c)
helmet.name = 'Numen 1 | Helmet and neck interface'
for o in helmet.objects: o.location.z -= 8.57
# Seat the decorative brow strips against the dome as shallow metal inlays.
bpy.context.view_layer.update()
dome=bpy.data.objects['Knight helmet dome']
for o in helmet.objects:
    if o.name.startswith('Helmet brow trim'):
        for v in o.data.vertices:
            local=dome.matrix_world.inverted() @ (o.matrix_world @ v.co)
            hit,pos,normal,_=dome.closest_point_on_mesh(local)
            if hit: v.co=o.matrix_world.inverted() @ (dome.matrix_world @ (pos+normal*.009))
# Replace the old flat crest with a properly closed solid, extruded across X.
for o in list(helmet.objects):
    if o.name.startswith('Sagittal crown ridge'): bpy.data.objects.remove(o, do_unlink=True)
outline = [(-.05,1.77),(.08,2.22),(.33,2.12),(.34,1.66)]
verts = [(x,y,z) for x in [-.043,.043] for y,z in outline]
faces = [(3,2,1,0),(4,5,6,7)]+[(i,(i+1)%4,(i+1)%4+4,i+4) for i in range(4)]
me=bpy.data.meshes.new('Solid crest');me.from_pydata(verts,[],faces);me.update()
crest=bpy.data.objects.new('Sagittal crest | solid gold',me);helmet.objects.link(crest)
me.materials.append(bpy.data.materials['Edges | champagne gold'])
bev=crest.modifiers.new('Crest edge radius','BEVEL');bev.width=.012;bev.segments=3
crest.modifiers.new('Crest normals','WEIGHTED_NORMAL')
# Keep parts editable, with a single root for placing the helmet on a body.
root=bpy.data.objects.new('NUMEN_1_HELMET',None);helmet.objects.link(root)
root['description']='Base Numen 1 helmet; front -Y, Z up; origin at neck attachment.'
for o in list(helmet.objects):
    if o != root: o.parent=root
dg=bpy.context.evaluated_depsgraph_get();counts={'objects':0,'polygons':0,'triangles':0}
for o in helmet.objects:
    if o.type != 'MESH': continue
    ev=o.evaluated_get(dg);m=ev.to_mesh();m.calc_loop_triangles()
    counts['objects']+=1;counts['polygons']+=len(m.polygons);counts['triangles']+=len(m.loop_triangles);ev.to_mesh_clear()
assert counts['triangles'] < 500000
(OUT/'geometry-report.json').write_text(json.dumps(counts,indent=2))
bpy.ops.object.select_all(action='DESELECT')
for o in helmet.objects:o.select_set(True)
bpy.context.view_layer.objects.active=root
bpy.ops.export_scene.gltf(filepath=str(OUT/'Numen_1_helmet_v1.glb'),use_selection=True,export_apply=True)
studio=bpy.data.collections.new('Studio | excluded from GLB');scene.collection.children.link(studio)
def put(o):
    for c in list(o.users_collection):c.objects.unlink(o)
    studio.objects.link(o)
    return o
target=Vector((0,0,1.13))
def aim(o):o.rotation_euler=(target-o.location).to_track_quat('-Z','Y').to_euler()
for name,loc,power,col,size in [('Warm key',(3,-4,5),500,(1,.87,.7),4),('Cool fill',(-3,-2,2),300,(.60,.8,1),3),('Rim',(2,3,4),700,(.6,.85,1),3)]:
    bpy.ops.object.light_add(type='AREA',location=loc);o=put(bpy.context.object);o.name=name;o.data.energy=power;o.data.color=col;o.data.size=size;aim(o)
bpy.ops.object.camera_add(location=(3,-5,2.6));cam=put(bpy.context.object);cam.name='Helmet review camera';cam.data.type='ORTHO';cam.data.ortho_scale=2.85;aim(cam);scene.camera=cam
scene.world.use_nodes=True
scene.world.node_tree.nodes.get('Background').inputs[0].default_value=(.022,.032,.047,1)
scene.world.node_tree.nodes.get('Background').inputs[1].default_value=.4
scene.render.engine='CYCLES';scene.cycles.samples=32;scene.cycles.use_denoising=True
scene.render.resolution_x=1200;scene.render.resolution_y=1200;scene.render.resolution_percentage=100
scene.render.image_settings.file_format='PNG';scene.render.film_transparent=False
for scr in bpy.data.screens:
    for area in scr.areas:
        if area.type=='VIEW_3D':
            area.spaces.active.region_3d.view_location=target
            area.spaces.active.region_3d.view_distance=3.5
            area.spaces.active.shading.color_type='MATERIAL'
bpy.ops.object.select_all(action='DESELECT');root.select_set(True);bpy.context.view_layer.objects.active=root
scene.render.filepath=str(OUT/'helmet-three-quarter-v1.png')
bpy.ops.wm.save_as_mainfile(filepath=str(OUT/'Numen_1_helmet_v1.blend'))
for name,loc in [('three-quarter',(3,-5,2.6)),('front',(0,-6,1.3)),('rear',(3,5,2.4))]:
    cam.location=loc;aim(cam);scene.render.filepath=str(OUT/f'helmet-{name}-v1.png');bpy.ops.render.render(write_still=True)
print('HELMET COMPLETE',counts,flush=True)
