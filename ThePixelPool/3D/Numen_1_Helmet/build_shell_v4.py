"""Approved shell-only Numen helmet. Front -Y, Z up. Blender 5.2."""
import bpy, math, json
from pathlib import Path
from mathutils import Vector
OUT=Path(__file__).resolve().parent/'shell-v4'
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
def interp(z,table):
    # Shape-preserving cubic tangents remove the straight segments of v3.
    slopes=[(b[1]-a[1])/(b[0]-a[0]) for a,b in zip(table,table[1:])]
    tangent=[slopes[0]]
    for i in range(1,len(table)-1):
        d0,d1=slopes[i-1],slopes[i]
        tangent.append(0 if d0*d1<=0 else 2*d0*d1/(d0+d1))
    tangent.append(slopes[-1])
    for i,((a,x),(b,y)) in enumerate(zip(table,table[1:])):
        if z<=b:
            t=max(0,(z-a)/(b-a));h=b-a
            return (2*t**3-3*t*t+1)*x+(t**3-2*t*t+t)*h*tangent[i]+(-2*t**3+3*t*t)*y+(t**3-t*t)*h*tangent[i+1]
    return table[-1][1]
# Silhouette landmarks measured from the approved front/profile sheet.
widths=[(.9,.73),(1.4,.75),(1.65,.73),(1.9,.65),(2.15,.51),(2.4,.31),(2.6,.13),(2.75,0)]
fore=[(.9,-.93),(1.4,-.94),(1.65,-.88),(1.9,-.66),(2.15,-.35),(2.4,.07),(2.6,.36),(2.75,.55)]
rear=[(.9,1.20),(1.4,1.34),(1.65,1.38),(1.9,1.32),(2.15,1.17),(2.4,.91),(2.6,.71),(2.75,.55)]
N=128;R=56;v=[]
for j in range(R):
    t=j/R
    radial=(1-t**1.65)**.88
    for i in range(N):
        a=math.tau*i/N
        front=max(0,-math.sin(a));back=max(0,math.sin(a))
        base=(1.39+.23*abs(math.cos(a))) if math.sin(a)<0 else (1.00+.62*(1-back)**3)
        z=base+(2.75-base)*t
        x=interp(z,widths)*math.cos(a)
        yf=interp(z,fore);yb=interp(z,rear)
        y=(yf+yb)/2+(yb-yf)/2*math.sin(a)
        v.append((x,y,z))
f=[]
for j in range(R-1):
    for i in range(N):
        ni=(i+1)%N;f.append((j*N+i,j*N+ni,(j+1)*N+ni,(j+1)*N+i))
v.append((0,.55,2.75));tip=len(v)-1
for i in range(N):f.append(((R-1)*N+i,(R-1)*N+(i+1)%N,tip))
mesh('01 Cranial shell | extended rear, high rim',v,f)
# Broad pointed face shield. The gap above is a real open visor aperture.
v=[];NX=64;NZ=18
for j in range(NZ+1):
    t=j/NZ
    for i in range(NX+1):
        u=-1+2*i/NX;au=abs(u)
        x=u*(.51+(.79-.51)*t+.025*math.sin(math.pi*t)*au**2)
        top=1.21+.23*au+.30*au**8
        bottom=.04+.34*au
        z=bottom*(1-t)+top*t
        y=(-.78+.33*au**1.3)*(1-t)+(-.98+1.10*(1-math.sqrt(max(0,1-au*au))))*t-.12*math.sin(math.pi*t)*au**3
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
            x=s*((.53+.09*q)*(1-t)+(.76-.035*q)*t)
            y=(-.43+.58*q)*(1-t)+(.08+.12*q)*t-.24*math.sin(t*math.pi)*(1-q)
            z=(.37+.28*q)*(1-t)+(1.64-.26*q)*t
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
bpy.ops.export_scene.gltf(filepath=str(OUT/'Numen_1_helmet_shell_v4.glb'),use_selection=True,export_apply=True)
# Independent reusable parts retain their assembled coordinates.
for o in list(shell.objects):
    if o.type!='MESH':continue
    bpy.ops.object.select_all(action='DESELECT');o.select_set(True);bpy.context.view_layer.objects.active=o
    stem=o.name[:2]+'-'+('cranium' if o.name.startswith('01') else 'face' if o.name.startswith('02') else 'left-cheek' if o.name.startswith('03') else 'right-cheek')
    bpy.ops.export_scene.gltf(filepath=str(OUT/(stem+'.glb')),use_selection=True,export_apply=True)
    bpy.data.libraries.write(str(OUT/(stem+'.blend')),{o},fake_user=True)
# Crop the original sheet nondestructively using UV quadrants on reference boards.
boards=bpy.data.collections.new('BLUEPRINTS | aligned reference planes');scene.collection.children.link(boards)
im=bpy.data.images.load(str(OUT.parent/'references/numen-helmet-shell-four-views-v2.png'));im.pack()
board_objects={}
for name,uv0,center,axis in [('front',(0,.5),(0,1.7,1.25),'front'),('side',(.5,.5),(-1.4,.226,1.25),'side'),('back',(0,0),(0,-1.6,1.25),'back'),('three-quarter',(.5,0),(4,1.7,1.25),'front')]:
    half=1.614
    cx,cy,cz=center
    verts=[(cx+x,cy,cz+z) if axis=='front' else (cx-x,cy,cz+z) if axis=='back' else (cx,cy+x,cz+z) for x,z in [(-half,-half),(half,-half),(half,half),(-half,half)]]
    me=bpy.data.meshes.new('Reference '+name);me.from_pydata(verts,[],[(0,1,2,3)]);me.update()
    uv=me.uv_layers.new()
    for k,(u,vv) in enumerate([(0,0),(.5,0),(.5,.5),(0,.5)]):uv.data[k].uv=(uv0[0]+u,uv0[1]+vv)
    ob=bpy.data.objects.new('Blueprint '+name,me);boards.objects.link(ob);ob.hide_render=True;board_objects[name]=ob
    m=bpy.data.materials.new('Reference '+name);m.use_nodes=True;nodes=m.node_tree.nodes;nodes.clear()
    tex=nodes.new('ShaderNodeTexImage');tex.image=im;em=nodes.new('ShaderNodeEmission');out=nodes.new('ShaderNodeOutputMaterial')
    m.node_tree.links.new(tex.outputs['Color'],em.inputs[0]);m.node_tree.links.new(em.outputs[0],out.inputs[0]);me.materials.append(m)
    ob['reference']='UV-cropped quadrant of packed approved sheet; toggle collection to compare.'
boards.hide_viewport=True
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
bpy.ops.wm.save_as_mainfile(filepath=str(OUT/'Numen_1_helmet_shell_v4.blend'))
for name,loc in [('three-quarter',(4,-6,3)),('front',(0,-6,1.39)),('side',(6,.1,1.39)),('back',(0,6,1.39))]:
    cam.location=loc;aim(cam);scene.render.filepath=str(OUT/f'shell-{name}.png');bpy.ops.render.render(write_still=True)
# Actual orthographic wire comparisons against the aligned reference planes.
wire=bpy.data.materials.new('Comparison coral');wire.diffuse_color=(1,.10,.035,1);wire.use_nodes=True
p=wire.node_tree.nodes.get('Principled BSDF');p.inputs['Base Color'].default_value=(1,.10,.035,1);p.inputs['Emission Color'].default_value=(1,.10,.035,1);p.inputs['Emission Strength'].default_value=.6
for o in shell.objects:
    if o.type=='MESH':
        o.data.materials.clear();o.data.materials.append(wire)
        for mod in list(o.modifiers):o.modifiers.remove(mod)
        mod=o.modifiers.new('Comparison outline','WIREFRAME');mod.thickness=.002
boards.hide_viewport=False
for name,loc in [('front',(0,-6,1.39)),('side',(6,.1,1.39)),('back',(0,6,1.39))]:
    for ob in board_objects.values():ob.hide_render=True
    board_objects[name].hide_render=False;cam.location=loc;aim(cam)
    scene.render.filepath=str(OUT/f'blueprint-comparison-{name}.png');bpy.ops.render.render(write_still=True)
print('SHELL COMPLETE',counts,flush=True)
