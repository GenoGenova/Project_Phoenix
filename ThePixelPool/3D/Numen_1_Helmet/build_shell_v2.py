"""Approved shell-only Numen helmet. Front -Y, Z up. Blender 5.2."""
import bpy, math, json
from pathlib import Path
from mathutils import Vector
OUT=Path(__file__).resolve().parent/'shell-v2'
OUT.mkdir(exist_ok=True)
bpy.ops.object.select_all(action='SELECT');bpy.ops.object.delete(use_global=False)
scene=bpy.context.scene
shell=bpy.data.collections.new('NUMEN | shell only');scene.collection.children.link(shell)
mat=bpy.data.materials.new('Neutral clay');mat.diffuse_color=(.66,.68,.70,1);mat.use_nodes=True
bs=mat.node_tree.nodes.get('Principled BSDF');bs.inputs['Base Color'].default_value=(.66,.68,.70,1);bs.inputs['Roughness'].default_value=.48
def mesh(name,v,f):
    me=bpy.data.meshes.new(name);me.from_pydata(v,[],f);me.update()
    o=bpy.data.objects.new(name,me);shell.objects.link(o);me.materials.append(mat)
    for p in me.polygons:p.use_smooth=True
    s=o.modifiers.new('Shell thickness','SOLIDIFY');s.thickness=.045;s.offset=-1;s.use_even_offset=True
    b=o.modifiers.new('Soft shell edges','BEVEL');b.width=.012;b.segments=3
    return o
# A continuous skull cap: raised horizontal rear rim and a longer occipital volume.
N=96;R=32;v=[]
for j in range(R):
    t=j/R
    radial=(1-t**1.65)**.88
    for i in range(N):
        a=math.tau*i/N
        front=max(0,-math.sin(a));back=max(0,math.sin(a))
        base=(1.54+.22*abs(math.cos(a))+.06*abs(math.cos(a))**8) if math.sin(a)<0 else (1.11+.71*(1-back)**5)
        x=.79*math.cos(a)*radial
        y=.08+(.79 if math.sin(a)<0 else 1.13)*math.sin(a)*radial
        z=base+(2.75-base)*t
        v.append((x,y,z))
f=[]
for j in range(R-1):
    for i in range(N):
        ni=(i+1)%N;f.append((j*N+i,j*N+ni,(j+1)*N+ni,(j+1)*N+i))
v.append((0,.08,2.75));tip=len(v)-1
for i in range(N):f.append(((R-1)*N+i,(R-1)*N+(i+1)%N,tip))
mesh('01 Cranial shell | extended rear, high rim',v,f)
# Broad pointed face shield. The gap above is a real open visor aperture.
v=[];NX=64;NZ=18
for j in range(NZ+1):
    t=j/NZ
    for i in range(NX+1):
        u=-1+2*i/NX;au=abs(u)
        x=u*(.57+(.79-.57)*t)
        top=1.36+.22*au+.28*au**12
        bottom=.04+.36*au
        z=bottom*(1-t)+top*t
        y=-.89+.39*au**1.35+.035*(1-t)
        v.append((x,y,z))
f=[]
for j in range(NZ):
    for i in range(NX):
        k=j*(NX+1)+i;f.append((k,k+1,k+NX+2,k+NX+1))
mesh('02 Face shield | pointed chin and swept temples',v,f)
# Simple side cheek shells stop independently of the cranial cap.
for s in [-1,1]:
    v=[];NX=16;NZ=20
    for j in range(NZ+1):
        t=j/NZ
        for i in range(NX+1):
            q=i/NX
            x=s*((.54+.12*q)*(1-t)+(.75+.03*math.sin(q*math.pi))*t)
            y=(-.48+.73*q)*(1-t)+(-.35+.62*q)*t
            z=(.28+.30*q)*(1-t)+(1.58-.22*q)*t
            v.append((x,y,z))
    f=[]
    for j in range(NZ):
        for i in range(NX):
            k=j*(NX+1)+i;face=(k,k+1,k+NX+2,k+NX+1);f.append(face if s<0 else face[::-1])
    mesh(('03 Left' if s<0 else '04 Right')+' cheek shell',v,f)
root=bpy.data.objects.new('NUMEN_HELMET_SHELL',None);shell.objects.link(root)
for o in shell.objects:
    if o!=root:o.parent=root
bpy.context.view_layer.update()
counts={'mesh_parts':4,'polygons':0,'triangles':0}
dg=bpy.context.evaluated_depsgraph_get()
for o in shell.objects:
    if o.type=='MESH':
        ev=o.evaluated_get(dg);me=ev.to_mesh();me.calc_loop_triangles();counts['polygons']+=len(me.polygons);counts['triangles']+=len(me.loop_triangles);ev.to_mesh_clear()
assert counts['triangles']<500000
(OUT/'geometry-report.json').write_text(json.dumps(counts,indent=2))
bpy.ops.object.select_all(action='DESELECT')
for o in shell.objects:o.select_set(True)
bpy.context.view_layer.objects.active=root
bpy.ops.export_scene.gltf(filepath=str(OUT/'Numen_1_helmet_shell_v2.glb'),use_selection=True,export_apply=True)
target=Vector((0,.1,1.39))
def aim(o):o.rotation_euler=(target-o.location).to_track_quat('-Z','Y').to_euler()
for loc,power,size in [((3,-4,6),650,4),((-4,-2,3),350,4),((1,4,5),700,3)]:
    bpy.ops.object.light_add(type='AREA',location=loc);o=bpy.context.object;o.data.energy=power;o.data.size=size;aim(o)
bpy.ops.object.camera_add(location=(4,-6,3));cam=bpy.context.object;cam.data.type='ORTHO';cam.data.ortho_scale=3.5;aim(cam);scene.camera=cam
scene.world.use_nodes=True;bg=scene.world.node_tree.nodes.get('Background');bg.inputs[0].default_value=(.075,.08,.09,1);bg.inputs[1].default_value=.6
scene.render.engine='CYCLES';scene.cycles.samples=24;scene.cycles.use_denoising=True
scene.render.resolution_x=1000;scene.render.resolution_y=1000;scene.render.resolution_percentage=100
scene.render.image_settings.file_format='PNG';scene.view_settings.view_transform='AgX'
for scr in bpy.data.screens:
    for a in scr.areas:
        if a.type=='VIEW_3D':
            a.spaces.active.region_3d.view_location=target;a.spaces.active.region_3d.view_distance=4.5
bpy.ops.object.select_all(action='DESELECT');root.select_set(True);bpy.context.view_layer.objects.active=root
bpy.ops.wm.save_as_mainfile(filepath=str(OUT/'Numen_1_helmet_shell_v2.blend'))
for name,loc in [('three-quarter',(4,-6,3)),('front',(0,-6,1.39)),('side',(6,.1,1.39)),('back',(0,6,1.39))]:
    cam.location=loc;aim(cam);scene.render.filepath=str(OUT/f'shell-{name}.png');bpy.ops.render.render(write_still=True)
print('SHELL COMPLETE',counts,flush=True)
