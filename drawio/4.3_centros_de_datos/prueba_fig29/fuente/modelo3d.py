"""Modelo 3D del recinto técnico del CD Talca para Blender (se ejecuta con
blender -b -P modelo3d.py -- <salida.png> [muestras]). Usa la misma geometría del plano."""
import math
import os
import sys

import bpy

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from geom import ROOMS, NUM, DOORS, EQUIP, FM200, EXTERIOR, T_EXT, T_INT, FACADE_Y  # noqa: E402

argv = sys.argv[sys.argv.index('--') + 1:] if '--' in sys.argv else []
OUT = argv[0] if argv else os.path.join(os.path.dirname(__file__), 'vista3d.png')
SAMPLES = int(argv[1]) if len(argv) > 1 else 64
H = 1.20          # altura del corte de muros para la vista (maqueta en corte)
DOOR_H = 2.10

bpy.ops.wm.read_factory_settings(use_empty=True)
scene = bpy.context.scene


def mat(name, rgb, rough=0.6, metal=0.0):
    m = bpy.data.materials.get(name) or bpy.data.materials.new(name)
    m.use_nodes = True
    b = m.node_tree.nodes.get('Principled BSDF')
    b.inputs['Base Color'].default_value = (*rgb, 1)
    b.inputs['Roughness'].default_value = rough
    b.inputs['Metallic'].default_value = metal
    return m


def srgb(h):
    h = h.lstrip('#')
    c = [int(h[i:i + 2], 16) / 255 for i in (0, 2, 4)]
    return tuple(((v + 0.055) / 1.055) ** 2.4 if v > 0.04045 else v / 12.92 for v in c)


M = {
    'muro': mat('muro', srgb('#E9E6E0'), 0.85), 'corte': mat('corte', srgb('#4A4A4A'), 0.9),
    'piso_S': mat('piso_S', srgb('#D7DCE2'), 0.5), 'piso': mat('piso', srgb('#CFC9BE'), 0.8),
    'bodega': mat('bodega', srgb('#B9B6B0'), 0.9), 'ext': mat('ext', srgb('#9FB08A'), 1.0),
    'losa': mat('losa', srgb('#A8A49C'), 0.9),
    'rack': mat('rack', srgb('#24272B'), 0.4, 0.3), 'clima': mat('clima', srgb('#F2F2EE'), 0.5),
    'energia': mat('energia', srgb('#5A5F66'), 0.5, 0.2), 'tablero': mat('tablero', srgb('#BFC3C7'), 0.5, 0.2),
    'incendio': mat('incendio', srgb('#C0262D'), 0.4), 'mueble': mat('mueble', srgb('#B5B9BE'), 0.6, 0.1),
    'madera': mat('madera', srgb('#A57A4F'), 0.6), 'puerta': mat('puerta', srgb('#8A9097'), 0.4, 0.4),
    'gen': mat('gen', srgb('#E0B83A'), 0.5), 'texto': mat('texto', srgb('#1B3A5C'), 0.5),
    'fondo_num': mat('fondo_num', srgb('#FFFFFF'), 0.5), 'ducto': mat('ducto', srgb('#4F78A8'), 0.5),
    'perforado': mat('perforado', srgb('#3A3F45'), 0.7, 0.4), 'led': mat('led', srgb('#38C172'), 0.3),
    'rejilla': mat('rejilla', srgb('#9AA0A6'), 0.5, 0.3), 'panel': mat('panel', srgb('#7A8089'), 0.45, 0.2),
    'pantalla': mat('pantalla', srgb('#1E5A8C'), 0.2),
}


def box(name, x0, y0, z0, x1, y1, z1, m):
    bpy.ops.mesh.primitive_cube_add(size=1, location=((x0 + x1) / 2, (y0 + y1) / 2, (z0 + z1) / 2))
    o = bpy.context.active_object
    o.name = name
    o.scale = (x1 - x0, y1 - y0, z1 - z0)
    bpy.ops.object.transform_apply(scale=True)
    o.data.materials.append(m)
    return o


def boolean(target, cutter, op='DIFFERENCE'):
    md = target.modifiers.new('b', 'BOOLEAN')
    md.operation = op
    md.solver = 'EXACT'
    md.object = cutter
    bpy.context.view_layer.objects.active = target
    bpy.ops.object.modifier_apply(modifier=md.name)
    bpy.data.objects.remove(cutter, do_unlink=True)


# --- Suelo de la bodega y exterior ------------------------------------------
box('bodega', -1.0, -1.0, -0.06, 7.9, 5.65, -0.01, M['bodega'])
box('exterior', -1.0, FACADE_Y, -0.08, 7.9, 8.6, -0.03, M['ext'])

# --- Pisos de recintos ----------------------------------------------------------
for k, (x0, y0, x1, y1, _) in ROOMS.items():
    box(f'piso_{k}', x0, y0, -0.01, x1, y1, 0.0 if k != 'S' else 0.05, M['piso_S' if k == 'S' else 'piso'])
# juntas del piso técnico
x0, y0, x1, y1, _ = ROOMS['S']
for i in range(1, 6):
    box(f'junta_x{i}', x0 + 0.6 * i - 0.004, y0, 0.05, x0 + 0.6 * i + 0.004, y1, 0.052, M['corte'])
j = 1
while y0 + 0.6 * j < y1:
    box(f'junta_y{j}', x0, y0 + 0.6 * j - 0.004, 0.05, x1, y0 + 0.6 * j + 0.004, 0.052, M['corte'])
    j += 1

# --- Muros: masa de los recintos ampliados menos interiores y vanos ---------------
muros = None
for k, (x0, y0, x1, y1, _) in ROOMS.items():
    b = box(f'm_{k}', x0 - T_EXT, y0 - T_EXT, 0, x1 + T_EXT, y1 + T_EXT, H, M['muro'])
    if muros is None:
        muros = b
        muros.name = 'muros'
    else:
        boolean(muros, b, 'UNION')
for k, (x0, y0, x1, y1, _) in ROOMS.items():
    boolean(muros, box(f'i_{k}', x0, y0, -0.5, x1, y1, H + 0.5, M['muro']))
for did, wall, c, a, b_, swing, hinge in DOORS:
    if wall == 'h':
        boolean(muros, box(f'v_{did}', a, c - 0.4, -0.1, b_, c + 0.4, DOOR_H, M['muro']))
    else:
        boolean(muros, box(f'v_{did}', c - 0.4, a, -0.1, c + 0.4, b_, DOOR_H, M['muro']))
# tapa oscura del corte superior de los muros
muros.data.materials.append(M['corte'])
for poly in muros.data.polygons:
    if poly.normal.z > 0.9 and poly.center.z > H - 0.01:
        poly.material_index = 1
# fachada del edificio, cortada a la misma altura
f = box('fachada', -0.2, 5.65, 0, 3.70, FACADE_Y, H, M['muro'])
f.data.materials.append(M['corte'])
for poly in f.data.polygons:
    if poly.normal.z > 0.9:
        poly.material_index = 1

# --- Hojas de puertas, abiertas a 90° -----------------------------------------
for did, wall, c, a, b_, swing, hinge in DOORS:
    d, t = b_ - a, 0.04
    if wall == 'h':
        hx = a if hinge == 'W' else b_
        sgn = 1 if swing == 'N' else -1
        box(f'hoja_{did}', hx - t / 2, min(c, c + sgn * d), 0.02, hx + t / 2, max(c, c + sgn * d), H, M['puerta'])
    else:
        hy = b_ if hinge == 'N' else a
        sgn = 1 if swing == 'E' else -1
        box(f'hoja_{did}', min(c, c + sgn * d), hy - t / 2, 0.02, max(c, c + sgn * d), hy + t / 2, H, M['puerta'])

# --- Equipos -------------------------------------------------------------------
MAT_EQ = {'R01': 'rack', 'R02': 'rack', 'CL1': 'clima', 'CL2': 'clima', 'ASD': 'incendio', 'UPS': 'energia',
          'BAT1': 'energia', 'BAT2': 'energia', 'TAB': 'tablero', 'SPL': 'clima', 'DESK': 'madera',
          'ARM': 'mueble', 'EST': 'mueble', 'ENR': 'madera'}
Z0 = {'ASD': 0.9, 'SPL': 2.0, 'TAB': 0.6}
GAP = 0.006   # junta visible entre gabinetes contiguos
for eid, x0, y0, x1, y1, lab, fam, h in EQUIP:
    if eid == 'SPL':
        continue   # split mural sobre la altura de corte
    if fam in ('rack', 'clima', 'energia') and eid != 'TAB':
        x0, x1 = x0 + GAP, x1 - GAP
    z0 = Z0.get(eid, 0.05 if eid in ('R01', 'R02', 'CL1', 'CL2') else 0.0)
    zt = h if eid not in Z0 else (z0 + (0.35 if eid == 'SPL' else 0.6 if eid == 'ASD' else 1.2))
    box(eid, x0, y0, z0, x1, y1, zt, M[MAT_EQ[eid]])
# frentes (cara sur): puertas perforadas de racks, rejillas de climatización y paneles de UPS
def frente(eid, m, z0, z1, inset=0.04):
    e = [q for q in EQUIP if q[0] == eid][0]
    box(f'{eid}_frente', e[1] + inset, e[2] - 0.008, z0, e[3] - inset, e[2], z1, m)
for eid in ('R01', 'R02'):
    frente(eid, M['perforado'], 0.15, 1.95)
    e = [q for q in EQUIP if q[0] == eid][0]
    for k in range(6):
        box(f'{eid}_led{k}', e[1] + 0.12 + k * 0.06, e[2] - 0.012, 1.70, e[1] + 0.14 + k * 0.06, e[2] - 0.008, 1.72, M['led'])
for eid in ('CL1', 'CL2'):
    for k in range(12):
        z = 0.30 + k * 0.12
        frente(eid, M['rejilla'], z, z + 0.05, 0.03)
for eid in ('UPS', 'BAT1', 'BAT2'):
    frente(eid, M['panel'], 0.08, 1.82, 0.03)
e = [q for q in EQUIP if q[0] == 'UPS'][0]
box('UPS_pantalla', e[1] + 0.18, e[2] - 0.014, 1.45, e[3] - 0.18, e[2] - 0.008, 1.62, M['pantalla'])
cx, cy, r = FM200
bpy.ops.mesh.primitive_cylinder_add(radius=r, depth=1.3, location=(cx, cy, 0.65))
bpy.context.active_object.data.materials.append(M['incendio'])
# silla
bpy.ops.mesh.primitive_cylinder_add(radius=0.25, depth=0.08, location=(0.60, 1.55, 0.48))
bpy.context.active_object.data.materials.append(M['rack'])
box('respaldo', 0.40, 1.28, 0.48, 0.80, 1.33, 1.05, M['rack'])

# --- Exterior --------------------------------------------------------------------
MAT_EX = {'GEN': 'gen', 'ATS': 'tablero', 'CD1': 'clima', 'CD2': 'clima', 'CD3': 'clima'}
for eid, x0, y0, x1, y1, lab, fam, h in EXTERIOR:
    if eid == 'GEN':
        box('losa', x0, y0, -0.03, x1, y1, 0.15, M['losa'])
        box('GEN', x0 + 0.25, y0 + 0.35, 0.15, x1 - 0.25, y1 - 0.35, 1.75, M['gen'])
    else:
        box(eid, x0, y0, 0, x1, y1, h, M[MAT_EX[eid]])
for x, ytop in ((5.45, 7.45), (7.25, 7.00)):
    box(f'ducto_{x}', x - 0.04, FACADE_Y, 0.0, x + 0.04, ytop, 0.08, M['ducto'])

# --- Números de recinto sobre el piso ----------------------------------------------
POS = {'W': (1.80, 1.50), 'P': (3.15, 2.30), 'E': (3.35, 3.85), 'U': (6.95, 0.95), 'S': (4.40, 3.00)}
for k, (px, py) in POS.items():
    bpy.ops.mesh.primitive_cylinder_add(radius=0.28, depth=0.02, location=(px, py, 0.07), vertices=64)
    bpy.context.active_object.data.materials.append(M['texto'])
    bpy.ops.mesh.primitive_cylinder_add(radius=0.24, depth=0.02, location=(px, py, 0.08), vertices=64)
    bpy.context.active_object.data.materials.append(M['fondo_num'])
    bpy.ops.object.text_add(location=(px, py, 0.091))
    t = bpy.context.active_object
    t.data.body = str(NUM[k])
    t.data.size = 0.36
    t.data.align_x = 'CENTER'
    t.data.align_y = 'CENTER'
    t.data.extrude = 0.005
    t.data.materials.append(M['texto'])

# --- Luz, cámara y render ------------------------------------------------------------
world = bpy.data.worlds.new('w')
scene.world = world
world.use_nodes = True
world.node_tree.nodes['Background'].inputs['Color'].default_value = (1, 1, 1, 1)
world.node_tree.nodes['Background'].inputs['Strength'].default_value = 0.55
bpy.ops.object.light_add(type='SUN', location=(0, 0, 10))
sun = bpy.context.active_object
sun.data.energy = 3.2
sun.data.angle = math.radians(8)
sun.rotation_euler = (math.radians(38), math.radians(-18), math.radians(-35))

cx, cy = 3.75, 3.6
bpy.ops.object.camera_add()
cam = bpy.context.active_object
scene.camera = cam
cam.data.type = 'ORTHO'
cam.data.ortho_scale = 10.6
az, el, dist = math.radians(-30), math.radians(58), 30
cam.location = (cx + dist * math.cos(el) * math.sin(az), cy - dist * math.cos(el) * math.cos(az), dist * math.sin(el))
dirv = (cx - cam.location[0], cy - cam.location[1], 0 - cam.location[2])
from mathutils import Vector  # noqa: E402
cam.rotation_euler = Vector(dirv).to_track_quat('-Z', 'Y').to_euler()

scene.render.engine = 'CYCLES'
scene.cycles.samples = SAMPLES
scene.cycles.use_denoising = True
scene.cycles.device = 'CPU'
scene.render.resolution_x = 2400
scene.render.resolution_y = 1800
scene.render.film_transparent = False
scene.view_settings.view_transform = 'Standard'
scene.render.filepath = OUT
bpy.ops.render.render(write_still=True)
bpy.ops.wm.save_as_mainfile(filepath=os.path.splitext(OUT)[0] + '.blend')
print('OK', OUT)
