"""Numen 1 / editable concept model. Run with Blender --background --python this_file."""
import bpy, bmesh, math, random, json
from pathlib import Path
from mathutils import Vector
random.seed(19)
OUT = Path(__file__).resolve().parent
OUT.mkdir(parents=True, exist_ok=True)
bpy.ops.object.select_all(action='SELECT'); bpy.ops.object.delete(use_global=False)
for c in list(bpy.data.collections):
    if c.name != 'Collection' and c.users == 0: bpy.data.collections.remove(c)
scene=bpy.context.scene
parts={}
def collection(name):
    c=bpy.data.collections.new(name); scene.collection.children.link(c); parts[name]=c; return c
for n in ['01 Helmet','02 Torso armor','03 Living spine','04 Pelvis','05 Left arm','06 Right arm','07 Left leg','08 Right leg','09 Pilot capsule','10 Reference','Studio']:
    collection(n)
active='02 Torso armor'
def put(o,name,mat):
    o.name=name
    for c in list(o.users_collection): c.objects.unlink(o)
    parts[active].objects.link(o)
    if mat: o.data.materials.append(mat)
    return o
def material(name,color,metal=0,rough=.4,emission=0):
    m=bpy.data.materials.new(name); m.diffuse_color=(*color,1); m.use_nodes=True
    p=m.node_tree.nodes.get('Principled BSDF'); p.inputs['Base Color'].default_value=(*color,1); p.inputs['Metallic'].default_value=metal; p.inputs['Roughness'].default_value=rough
    if emission: p.inputs['Emission Color'].default_value=(*color,1); p.inputs['Emission Strength'].default_value=emission
    return m
ivory=material('Ceramic | warm ivory',(.72,.70,.60),.38,.3)
bone=material('Living frame | pale titanium',(.44,.47,.42),.55,.36)
dark=material('Joint | graphite',(.025,.034,.040),.72,.32)
black=material('Recess | carbon',(.007,.012,.016),.3,.48)
gold=material('Edges | champagne gold',(.42,.30,.125),.78,.26)
steel=material('Actuator | polished titanium',(.30,.36,.38),.85,.22)
cyan=material('Neural channels | ice cyan',(.06,.65,.86),.45,.24,3)
glass=material('Capsule | smoked blue glass',(.025,.10,.13),.55,.2)
def bevel(o,w=.035,seg=2):
    m=o.modifiers.new('Machined edge radii','BEVEL'); m.width=w; m.segments=seg
    m=o.modifiers.new('Face weighted normals','WEIGHTED_NORMAL'); m.keep_sharp=True
    return o
def mesh(name,verts,faces,mat,bev=0):
    me=bpy.data.meshes.new(name); me.from_pydata(verts,[],faces); me.update(); o=bpy.data.objects.new(name,me); parts[active].objects.link(o); me.materials.append(mat)
    if bev: bevel(o,bev)
    return o
def box(name,loc,scale,mat,bev=.025):
    x,y,z=loc;w,d,h=[s/2 for s in scale]
    return mesh(name,[(x+sx*w,y+sy*d,z+sz*h) for sx,sy,sz in [(-1,-1,-1),(1,-1,-1),(1,1,-1),(-1,1,-1),(-1,-1,1),(1,-1,1),(1,1,1),(-1,1,1)]],[(0,3,2,1),(4,5,6,7),(0,1,5,4),(1,2,6,5),(2,3,7,6),(3,0,4,7)],mat,bev)
def sphere(name,loc,scale,mat,segments=24,rings=12):
    me=bpy.data.meshes.new(name); bm=bmesh.new();bmesh.ops.create_uvsphere(bm,u_segments=segments,v_segments=rings,radius=1);bm.to_mesh(me);bm.free()
    o=bpy.data.objects.new(name,me);parts[active].objects.link(o);me.materials.append(mat);o.location=loc;o.scale=scale
    for p in o.data.polygons:p.use_smooth=True
    return o
def rod(name,a,b,r,mat,vertices=12,r2=None):
    a,b=Vector(a),Vector(b); d=b-a
    q=d.to_track_quat('Z','Y');v=[]
    for z,rad in [(-d.length/2,r),(d.length/2,r if r2 is None else r2)]:
        for i in range(vertices):v.append(tuple((a+b)/2+q@Vector((rad*math.cos(i*math.tau/vertices),rad*math.sin(i*math.tau/vertices),z))))
    f=[tuple(range(vertices-1,-1,-1)),tuple(range(vertices,2*vertices))]+[(i,(i+1)%vertices,(i+1)%vertices+vertices,i+vertices) for i in range(vertices)]
    o=mesh(name,v,f,mat)
    for p in o.data.polygons:p.use_smooth=True
    return o
def tube(name,points,r,mat):
    cu=bpy.data.curves.new(name,'CURVE'); cu.dimensions='3D'; cu.resolution_u=4; cu.bevel_depth=r; cu.bevel_resolution=2
    sp=cu.splines.new('BEZIER'); sp.bezier_points.add(len(points)-1)
    for b,p in zip(sp.bezier_points,points): b.co=p;b.handle_left_type='AUTO';b.handle_right_type='AUTO'
    o=bpy.data.objects.new(name,cu);parts[active].objects.link(o);cu.materials.append(mat);return o
def plate(name,outline,depth=.13,mat=ivory):
    # Outline in world coordinates; armor projects toward the camera (-Y).
    v=[tuple(p) for p in outline]+[(x,y+depth,z) for x,y,z in outline]; n=len(outline)
    f=[tuple(range(n-1,-1,-1)),tuple(range(n,2*n))]+[(i,(i+1)%n,(i+1)%n+n,i+n) for i in range(n)]
    return mesh(name,v,f,mat,.026)
def panel(name,x,y,z,w,h):
    box(name+' substrate',(x,y,z),(w,.08,h),black)
    box(name+' gold rim',(x,y-.048,z),(w*.88,.025,h*.88),gold,.012)
    box(name+' PCB',(x,y-.07,z),(w*.82,.022,h*.82),dark,.008)
    box(name+' processor',(x,y-.095,z),(w*.42,.07,h*.43),steel,.01)
    box(name+' die',(x,y-.135,z),(w*.27,.018,h*.29),dark,.004)
    for i in range(7):
        t=(i-3)*h*.094
        for s in [-1,1]:box(name+' bus pin',(x+s*w*.31,y-.097,z+t),(w*.09,.02,.022),gold,.002)
    for i in range(4):
        box(name+' memory',(x-w*.28+i*w*.18,y-.10,z-h*.31),(w*.10,.035,h*.075),steel,.003)
def lattice(name,a,b,radius,rings=7):
    a,b=Vector(a),Vector(b); axis=(b-a).normalized(); u=axis.cross(Vector((0,1,0))).normalized();v=axis.cross(u)
    rod(name+' dark inner core',a,b,radius*.34,dark,20)
    nodes=[]; count=7
    for j in range(rings):
        t=j/(rings-1); rr=radius*(.77+.20*math.sin(t*math.pi)); row=[]
        for k in range(count):
            th=k*math.tau/count+(j%2)*.22; p=a.lerp(b,t)+rr*(u*math.cos(th)+v*math.sin(th));row.append(p)
            sphere(name+' grown node',p,(.071,.071,.09),bone,12,8)
        nodes.append(row)
    for j in range(rings-1):
        for k in range(count):
            a1=nodes[j][k]; b1=nodes[j+1][k]; mid=(a1+b1)*.5+(a1-a.lerp(b,(j+.5)/(rings-1)))*.06
            tube(name+' longitudinal trabecula',[a1,mid,b1],.043,bone)
            b2=nodes[j+1][(k+(1 if j%2 else -1))%count]
            tube(name+' oblique trabecula',[a1,(a1+b2)*.5,b2],.032,bone)
    tube(name+' neural filament',[a.lerp(b,j/8)+v*radius*.86+u*.035*math.sin(j*1.7) for j in range(9)],.018,cyan)
def joint(name,p,r):
    sphere(name+' knuckle',p,(r,r,r),dark)
    x,y,z=p;rod(name+' axial bearing',(x-r*1.02,y,z),(x+r*1.02,y,z),r*.77,steel,32)
    for s in [-1,1]:rod(name+' gold race',(x+s*r*.96,y,z),(x+s*r*1.08,y,z),r*.51,gold,32)
def seam(name,pts):tube(name,pts,.016,gold)

# Axial body: open waist, articulated vertebrae, rib-like frame.
active='03 Living spine'
lattice('Abdominal living frame',(0,.04,5.40),(0,.10,7.95),.48,11)
for i in range(15):
    z=5.42+i*.205
    box('Vertebra %02d'%i,(0,.37,z),(.27,.30,.14),bone,.055)
    sphere('Spinal neural node',(0,.56,z),(.055,.055,.07),cyan,12,8)
    for s in [-1,1]:
        tube('Spinal rib',[(0,.38,z),(s*.35,.44,z+.08),(s*.72,.20,z+.23)],.05,bone)
for s in [-1,1]:
    tube('Thoracic arch',[(s*.3,.1,6.8),(s*.98,.12,7.55),(s*1.0,.20,8.22),(s*.36,.30,8.65)],.12,bone)
    rod('Thorax support',(s*.63,.10,7.1),(s*1.15,.08,8.40),.16,dark)

active='02 Torso armor'
box('Chest carbon core',(0,.06,8.06),(1.95,.87,1.37),dark,.18)
for s in [-1,1]:
    def sym(points): return [(s*x,y,z) for x,y,z in points]
    plate('Pectoral ceramic '+str(s),sym([(.08,-.65,8.62),(.86,-.62,8.72),(1.35,-.40,8.35),(1.12,-.56,7.82),(.52,-.73,7.62),(.12,-.78,7.99)]))
    plate('Floating clavicle '+str(s),sym([(.14,-.48,8.75),(.7,-.26,9.00),(1.08,-.15,8.81),(.87,-.6,8.68)]),.11)
    plate('Lower rib armor '+str(s),sym([(.38,-.55,7.76),(1.05,-.42,7.87),(.85,-.37,7.31),(.39,-.60,6.95),(.13,-.65,7.35)]),.13)
    panel('Pectoral compute '+str(s),s*.78,-.75,8.17,.55,.53)
    seam('Chest panel trim',sym([(.1,-.80,8.04),(.52,-.75,7.68),(1.08,-.59,7.86)]))
    for i in range(3):box('Chest cooling slot',(s*(.23+i*.1),-.67,8.53),(.035,.035,.12),black,.006)
plate('Sternal keel',[(-.14,-.85,8.60),(.14,-.85,8.60),(.20,-.9,8.10),(0,-.94,7.86),(-.20,-.9,8.10)],.15,dark)
plate('Sternal blue aperture',[(-.085,-.96,8.43),(.085,-.96,8.43),(.055,-.96,8.13),(0,-.96,8.04),(-.055,-.96,8.13)],.02,cyan)

active='04 Pelvis'
box('Pelvic cradle',(0,.08,5.45),(1.42,.91,.69),dark,.16)
for s in [-1,1]:
    joint('Hip', (s*.61,.02,5.24),.36)
    plate('Iliac armor',[(s*.12,-.53,5.65),(s*.72,-.48,5.90),(s*1.07,-.20,5.56),(s*.77,-.49,5.11),(s*.25,-.63,5.2)])
    plate('Split hanging tasset',[(s*.2,-.58,5.34),(s*.66,-.60,5.36),(s*.7,-.57,4.54),(s*.39,-.68,4.08),(s*.20,-.66,4.40)],.10)
plate('Pelvis center crest',[(-.20,-.65,5.65),(.20,-.65,5.65),(.12,-.72,5.04),(0,-.75,4.85),(-.12,-.72,5.04)],.16)
box('Pelvic emitter',(0,-.83,5.40),(.11,.04,.17),cyan,.015)

# Legs: sloping stance, armor islands leave the frame visible.
for s,label in [(-1,'Left'),(1,'Right')]:
    active='07 Left leg' if s==-1 else '08 Right leg'
    hip=(s*.65,.04,5.18); knee=(s*.89,-.06,3.03); ankle=(s*1.06,.12,.86)
    lattice(label+' femur',hip,knee,.33,9);lattice(label+' tibia',knee,ankle,.29,10)
    joint(label+' knee',knee,.32);joint(label+' ankle',ankle,.27)
    x=s*.78
    plate(label+' thigh front',[(x-s*.32,-.36,5.05),(x+s*.25,-.37,5.12),(x+s*.40,-.39,4.71),(x+s*.23,-.44,3.68),(x,-.52,3.38),(x-s*.26,-.43,3.73)],.16)
    panel(label+' thigh compute',x,-.49,4.43,.39,.68)
    plate(label+' outer thigh blade',[(s*1.07,-.04,5.30),(s*1.40,.00,4.94),(s*1.38,-.03,4.02),(s*1.13,-.11,4.35)],.12)
    x=s*.89
    plate(label+' knee shield',[(x,-.53,3.44),(x+s*.32,-.44,3.13),(x+s*.22,-.51,2.85),(x,-.65,2.71),(x-s*.27,-.5,3.04)],.16)
    box(label+' knee cyan',(x,-.65,3.09),(.1,.03,.23),cyan,.015)
    x=s*1.01
    plate(label+' shin upper plate',[(x-s*.25,-.30,2.82),(x+s*.23,-.32,2.65),(x+s*.37,-.26,2.10),(x+s*.18,-.37,1.29),(x-s*.05,-.48,1.54),(x-s*.24,-.45,2.12)],.13)
    plate(label+' shin outer fin',[(s*1.31,.04,2.87),(s*1.62,.07,2.54),(s*1.65,.10,1.52),(s*1.40,-.02,1.85)],.10)
    seam(label+' shin gold',[(x-s*.22,-.46,2.67),(x-s*.20,-.48,2.17),(x-s*.04,-.51,1.58)])
    rod(label+' rear piston',(s*1.05,.39,1.0),(s*.94,.36,2.63),.09,steel)
    x=s*1.06
    box(label+' foot sole',(x,-.38,.18),(.75,1.62,.27),dark,.08)
    # boot wedge, long knight toe
    mesh(label+' sabaton',[(x-.35,-1.22,.25),(x+.35,-1.22,.25),(x+.38,.32,.25),(x-.38,.32,.25),(x-.26,-1.05,.42),(x+.26,-1.05,.42),(x+.25,.12,.88),(x-.25,.12,.88)],[(0,1,2,3),(0,4,5,1),(1,5,6,2),(2,6,7,3),(3,7,4,0),(4,7,6,5)],ivory,.035)
    for j in range(3):box(label+' toe articulation',(x,-.92+j*.23,.47+j*.083),(.61,.035,.028),gold,.006)
    plate(label+' ankle shield',[(x-.24,-.35,1.19),(x+.24,-.35,1.19),(x+.28,-.46,.75),(x,-.65,.58),(x-.28,-.46,.75)],.1)
    box(label+' boot intake',(x,-.49,.91),(.22,.04,.23),black,.015)

# Arms, separate hands and armored fingers.
for s,label in [(-1,'Left'),(1,'Right')]:
    active='05 Left arm' if s==-1 else '06 Right arm'
    shoulder=(s*1.40,.05,8.25);elbow=(s*1.88,-.02,6.77);wrist=(s*2.07,-.23,5.36)
    joint(label+' shoulder',shoulder,.42);lattice(label+' humerus',shoulder,elbow,.28,7)
    joint(label+' elbow',elbow,.27);lattice(label+' radius',elbow,wrist,.25,8)
    x=s*1.46
    plate(label+' great pauldron',[(s*.98,-.38,8.66),(s*1.46,-.46,9.01),(s*2.12,-.24,8.70),(s*2.26,-.14,8.24),(s*1.85,-.49,8.08),(s*1.45,-.58,8.44)],.49)
    plate(label+' layered shoulder rim',[(s*1.64,-.59,8.42),(s*2.14,-.35,8.39),(s*2.20,-.25,7.82),(s*1.94,-.43,7.99)],.13)
    seam(label+' pauldron gold',[(s*1.02,-.42,8.68),(s*1.47,-.50,8.97),(s*2.08,-.28,8.68)])
    plate(label+' upper arm plate',[(s*1.61,-.29,7.94),(s*1.91,-.26,7.79),(s*2.02,-.26,7.26),(s*1.76,-.34,7.43)],.12)
    plate(label+' forearm vambrace',[(s*1.79,-.31,6.73),(s*2.19,-.28,6.80),(s*2.42,-.14,6.41),(s*2.23,-.39,5.63),(s*1.99,-.51,5.51),(s*1.86,-.46,5.92)],.18)
    plate(label+' utility fin',[(s*2.32,-.10,6.69),(s*2.65,.04,6.29),(s*2.48,.04,5.23),(s*2.22,-.06,5.78)],.10)
    box(label+' forearm emitter',(s*2.09,-.50,6.03),(.065,.04,.43),cyan,.018)
    rod(label+' actuator',(s*1.94,.21,6.45),(s*2.10,.03,5.54),.065,steel)
    joint(label+' wrist',wrist,.17)
    box(label+' palm',(s*2.07,-.24,5.03),(.40,.27,.49),dark,.06)
    plate(label+' hand back',[(s*1.89,-.42,5.21),(s*2.25,-.42,5.21),(s*2.25,-.43,4.96),(s*2.09,-.47,4.85),(s*1.90,-.43,4.99)],.08)
    for f in range(4):
        x=s*(1.93+f*.10); z=4.87-abs(f-1.5)*.025
        pts=[(x,-.24,z),(x,-.28,z-.19),(x,-.38,z-.34),(x,-.48,z-.38)]
        for j in range(3):
            rod(label+' finger %d segment %d'%(f,j),pts[j],pts[j+1],.051,dark,12)
            sphere(label+' finger bearing',pts[j],(.061,.061,.061),steel,12,8)
    tube(label+' thumb',[(s*1.88,-.24,5.07),(s*1.71,-.35,4.95),(s*1.77,-.53,4.81)],.075,dark)

# Head, front is -Y. Closed medieval visor on an organic neck.
active='01 Helmet'
lattice('Neck',(0,.07,8.57),(0,.06,9.23),.24,5)
rod('Gorget collar',(0,.04,8.90),(0,.04,9.09),.43,dark,48)
# Ring loft gives helmet a peaked curved dome and projecting face.
N=32; verts=[]
for z,rx,ry,cy in [(9.15,.30,.30,-.10),(9.48,.43,.39,-.04),(9.88,.49,.43,.02),(10.16,.40,.38,.05),(10.37,.22,.25,.06),(10.45,.045,.08,.06)]:
    for i in range(N):
        t=i*math.tau/N; verts.append((rx*math.cos(t),cy+ry*math.sin(t),z))
faces=[]
for j in range(5):
    for i in range(N):faces.append((j*N+i,j*N+(i+1)%N,(j+1)*N+(i+1)%N,(j+1)*N+i))
faces+=[tuple(range(N-1,-1,-1)),tuple(range(5*N,6*N))]
o=mesh('Knight helmet dome',verts,faces,ivory,.016)
for p in o.data.polygons:p.use_smooth=True
plate('Dark visor band',[(-.45,-.43,9.85),(0,-.59,9.71),(.45,-.43,9.85),(.39,-.45,9.66),(0,-.61,9.58),(-.39,-.45,9.66)],.05,black)
tube('Cyan slit left',[(-.39,-.475,9.79),(-.18,-.56,9.73),(0,-.615,9.68)],.014,cyan)
tube('Cyan slit right',[(0,-.615,9.68),(.18,-.56,9.73),(.39,-.475,9.79)],.014,cyan)
for s in [-1,1]:
    plate('Visor face half',[(0,-.64,9.58),(s*.40,-.46,9.68),(s*.31,-.49,9.20),(0,-.66,9.04)],.09)
    plate('Swept temporal armor',[(s*.40,-.13,9.89),(s*.60,.29,9.60),(s*.43,.28,9.27),(s*.36,-.13,9.37)],.10)
    rod('Helmet ear bearing',(s*.40,.02,9.53),(s*.52,.02,9.53),.145,gold,32)
    rod('Helmet ear insert',(s*.51,.02,9.53),(s*.54,.02,9.53),.104,dark,32)
    for i in range(3):box('Breather slot',(s*(.14+i*.06),-.591+i*.027,9.25+i*.035),(.023,.045,.10),black,.006)
    seam('Helmet brow trim',[(0,-.60,9.85),(s*.29,-.43,10.12),(s*.20,-.18,10.39)])
plate('Sagittal crown ridge',[(-.045,-.05,10.34),(-.045,.08,10.79),(-.045,.33,10.69),(-.045,.34,10.23)],.09,gold)

# Upper spine cockpit: visible from rear, no wing upgrade equipment.
active='09 Pilot capsule'
box('Capsule protective cradle',(0,.60,8.39),(.90,.61,1.42),dark,.18)
box('Pilot capsule window',(0,.94,8.43),(.54,.11,1.05),glass,.16)
for s in [-1,1]:
    tube('Capsule frame rail',[(s*.32,.98,7.92),(s*.39,.99,8.20),(s*.37,.99,8.91),(s*.20,.97,9.06)],.042,steel)
    tube('Capsule status line',[(s*.26,1.01,8.03),(s*.28,1.01,8.74)],.014,cyan)
    plate('Rear spinal armor',[(s*.46,.64,8.91),(s*.99,.52,8.80),(s*.83,.68,7.72),(s*.42,.81,7.58)],.12)
    box('Upper utility mounting socket',(s*.89,.40,9.01),(.26,.27,.65),dark,.035)
    plate('Folded airbrake',[(s*.78,.30,8.91),(s*.86,.35,9.63),(s*1.11,.35,9.75),(s*1.12,.28,9.01)],.10)
active='03 Living spine'
for i in range(8):
    z=6.1+i*.20
    for s in [-1,1]:tube('Posterior growing lattice',[(s*.12,.54,z),(s*.46,.62,z+.10),(s*.15,.57,z+.25)],.048,bone)

# Small gold fasteners on major armor surfaces.
for cname in ['02 Torso armor','04 Pelvis','05 Left arm','06 Right arm','07 Left leg','08 Right leg']:
    active=cname
    armor=[o for o in parts[cname].objects if o.type=='MESH' and len(o.data.materials) and o.data.materials[0]==ivory and len(o.data.vertices)<30]
    for o in armor:
        for v in list(o.data.vertices)[:3]:
            p=o.matrix_world@v.co; p.y-=.03
            sphere('Flush gold armor rivet',p,(.028,.014,.028),gold,12,6)

# Convert all curved struts in a single operation, avoiding repeated scene updates.
bpy.context.view_layer.update()
bpy.ops.object.select_all(action='DESELECT')
curves=[]
for c in parts.values():
    for o in list(c.objects):
        if o.type=='CURVE':
            o.select_set(True);curves.append(o)
print('CONVERTING FRAME',len(curves),flush=True)
if curves:
    bpy.context.view_layer.objects.active=curves[0];bpy.ops.object.convert(target='MESH')
# Counts are evaluated, including bevels. Triangles are the stricter budget.
def stats():
    dg=bpy.context.evaluated_depsgraph_get();poly=tri=verts=0
    for name,c in parts.items():
        if name in ['Studio','10 Reference']:continue
        for o in c.objects:
            if o.type!='MESH':continue
            ev=o.evaluated_get(dg);me=ev.to_mesh();me.calc_loop_triangles();poly+=len(me.polygons);tri+=len(me.loop_triangles);verts+=len(me.vertices);ev.to_mesh_clear()
    return dict(vertices=verts,polygons=poly,triangles=tri)
counts=stats()
assert counts['triangles']<500000,counts
print('NUMEN GEOMETRY',counts,flush=True)
(OUT/'geometry-report.json').write_text(json.dumps(counts,indent=2))

active='10 Reference'
ref=OUT.parents[1]/'illustrations/numen-concept-01.png'
if ref.exists():
    im=bpy.data.images.load(str(ref));im.pack();o=bpy.data.objects.new('Approved concept | front and rear design guide',None);parts[active].objects.link(o);o.empty_display_type='IMAGE';o.data=im;o.empty_display_size=10;o.location=(-7,2,5);o.rotation_euler=(math.pi/2,0,0);o.hide_render=True;parts[active].hide_viewport=True

active='Studio'
ground=material('Studio floor',(.025,.037,.048),.2,.45)
box('Display plinth',(0,0,-.13),(5.8,4.5,.22),dark,.10)
box('Studio floor',(0,0,-.32),(200,200,.10),ground,0)
def area(name,loc,power,color,size):
    bpy.ops.object.light_add(type='AREA',location=loc);o=put(bpy.context.object,name,None);o.data.energy=power;o.data.color=color;o.data.shape='DISK';o.data.size=size;o.rotation_euler=(Vector((0,0,5))-o.location).to_track_quat('-Z','Y').to_euler()
area('Key softbox',(5,-8,13),2400,(1,.89,.72),7)
area('Cool fill',(-6,-4,7),1800,(.61,.79,1),6)
area('Rim',(3,5,11),3000,(.65,.82,1),5)
area('Front helmet',(0,-7,11),700,(1,1,1),4)
scene.world.color=(.14,.14,.14)
bpy.ops.object.camera_add(location=(13,-23,12));cam=put(bpy.context.object,'Camera | front three quarter',None);cam.rotation_euler=(Vector((0,0,5.3))-cam.location).to_track_quat('-Z','Y').to_euler();cam.data.type='ORTHO';cam.data.ortho_scale=12.5;scene.camera=cam
scene.render.engine='CYCLES';scene.cycles.samples=24;scene.cycles.use_denoising=True
scene.render.resolution_x=1100;scene.render.resolution_y=1300;scene.render.resolution_percentage=100
scene.view_settings.view_transform='AgX'
scene.render.image_settings.file_format='PNG';scene.render.filepath=str(OUT/'numen-1-front-v1.png')
# Nice default solid viewport with material colors.
for scr in bpy.data.screens:
    for a in scr.areas:
        if a.type=='VIEW_3D':
            a.spaces.active.shading.color_type='MATERIAL';a.spaces.active.region_3d.view_distance=17;a.spaces.active.region_3d.view_location=Vector((0,0,5))
bpy.ops.object.select_all(action='DESELECT')
bpy.ops.wm.save_as_mainfile(filepath=str(OUT/'Numen_1_base_v1.blend'))
bpy.ops.render.render(write_still=True)
cam.location=(-12,22,11);cam.rotation_euler=(Vector((0,0,5.4))-cam.location).to_track_quat('-Z','Y').to_euler();scene.render.filepath=str(OUT/'numen-1-rear-v1.png');bpy.ops.render.render(write_still=True)
print('BUILD COMPLETE',flush=True)
