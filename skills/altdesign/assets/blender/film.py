"""altdesign film template: a scripted, headless Blender scene for a hero film or a backdrop still.

    blender -b --factory-startup -P film.py -- --beats beats.json --out frames/ [--preview] [--still 120]

beats.json drives both the film and the page's chapter buttons:
    {"fps": 24, "size": [1280, 720],
     "palette": {"ground": "#0E2219", "ink": "#F4EFE6", "pop": "#C9A96E"},
     "beats": [{"name": "Model", "seconds": 3, "camera": [9, -9, 6], "target": [0, 0, 1]}, ...]}

Replace build_subject() with the product's real subject, built from its real data where possible
(the AREZ film built a 7,000 sf wood frame house procedurally and coloured members by utilisation).
Keep everything in code so the film can be re-rendered after any change. Text stays out of the frames:
captions go in the HTML next to the video.
"""
import json
import math
import os
import sys

import bpy
from mathutils import Vector


def args():
    a = sys.argv[sys.argv.index("--") + 1:] if "--" in sys.argv else []
    o = {"beats": "beats.json", "out": "frames", "preview": False, "still": None}
    i = 0
    while i < len(a):
        k = a[i].lstrip("-")
        if k == "preview":
            o["preview"] = True
        else:
            o[k] = a[i + 1]
            i += 1
        i += 1
    return o


def hex_rgba(h, a=1.0):
    h = h.lstrip("#")
    srgb = [int(h[i:i + 2], 16) / 255 for i in (0, 2, 4)]
    lin = [c / 12.92 if c <= 0.04045 else ((c + 0.055) / 1.055) ** 2.4 for c in srgb]
    return (*lin, a)


def material(name, color, rough=0.6, emit=0.0):
    m = bpy.data.materials.new(name)
    m.use_nodes = True
    b = m.node_tree.nodes["Principled BSDF"]
    b.inputs["Base Color"].default_value = color
    b.inputs["Roughness"].default_value = rough
    if emit:
        b.inputs["Emission Color"].default_value = color
        b.inputs["Emission Strength"].default_value = emit
    return m


def build_subject(pal):
    """Placeholder subject: a frame of members with one 'hero' member in the pop colour.
    Replace with the product's own subject."""
    ink, pop = material("ink", hex_rgba(pal["ink"]), 0.5), material("pop", hex_rgba(pal["pop"]), 0.35, 0.6)
    for i in range(9):
        x = (i - 4) * 0.6
        bpy.ops.mesh.primitive_cube_add(size=1, location=(x, 0, 1.2))
        o = bpy.context.object
        o.scale = (0.08, 0.08, 1.2)
        o.data.materials.append(pop if i == 4 else ink)
    bpy.ops.mesh.primitive_cube_add(size=1, location=(0, 0, 2.45))
    beam = bpy.context.object
    beam.scale = (5.6, 0.12, 0.12)
    beam.data.materials.append(ink)


def scene(cfg):
    for o in list(bpy.data.objects):
        bpy.data.objects.remove(o, do_unlink=True)
    sc = bpy.context.scene
    pal = cfg["palette"]
    sc.render.engine = "BLENDER_EEVEE"
    sc.render.resolution_x, sc.render.resolution_y = cfg.get("size", [1280, 720])
    sc.render.fps = cfg.get("fps", 24)
    sc.render.image_settings.file_format = "PNG"
    sc.view_settings.view_transform = "AgX"
    world = sc.world or bpy.data.worlds.new("w")
    sc.world = world
    world.use_nodes = True
    world.node_tree.nodes["Background"].inputs["Color"].default_value = hex_rgba(pal["ground"])
    world.node_tree.nodes["Background"].inputs["Strength"].default_value = 1.0

    bpy.ops.mesh.primitive_plane_add(size=60)
    bpy.context.object.data.materials.append(material("ground", hex_rgba(pal["ground"]), 0.9))
    build_subject(pal)

    # One key light from above left, a soft fill, a rim: one light source direction, like the page's shadows.
    for name, loc, energy, size in (("key", (-6, -6, 10), 900, 6), ("fill", (8, -4, 4), 180, 10), ("rim", (0, 8, 6), 400, 4)):
        bpy.ops.object.light_add(type="AREA", location=loc)
        l = bpy.context.object
        l.data.energy, l.data.size = energy, size
        l.rotation_euler = (Vector((0, 0, 1)) - Vector(loc)).to_track_quat("-Z", "Y").to_euler()

    bpy.ops.object.empty_add(location=(0, 0, 1))
    target = bpy.context.object
    bpy.ops.object.camera_add()
    cam = bpy.context.object
    cam.data.lens = 40
    sc.camera = cam
    c = cam.constraints.new("TRACK_TO")
    c.target, c.track_axis, c.up_axis = target, "TRACK_NEGATIVE_Z", "UP_Y"

    # One move per beat, eased (Bezier, never linear), matching the page's base curve feel.
    f, fps = 1, sc.render.fps
    for b in cfg["beats"]:
        cam.location, target.location = b["camera"], b.get("target", (0, 0, 1))
        cam.keyframe_insert("location", frame=f)
        target.keyframe_insert("location", frame=f)
        b["start"] = round((f - 1) / fps, 2)
        f += int(b["seconds"] * fps)
    # Hold the last beat: key it again at the end so the film rests on its final frame.
    cam.keyframe_insert("location", frame=f - 1)
    target.keyframe_insert("location", frame=f - 1)
    sc.frame_start, sc.frame_end = 1, f - 1
    # New keys are Bezier with auto clamped handles by default, which eases in and out of each beat.
    return sc


def main():
    o = args()
    cfg = json.load(open(o["beats"]))
    sc = scene(cfg)
    os.makedirs(o["out"], exist_ok=True)
    # Chapters for the page: the same start times the film uses.
    json.dump([{"name": b["name"], "start": b["start"]} for b in cfg["beats"]],
              open(os.path.join(o["out"], "chapters.json"), "w"), indent=1)
    if o["still"]:
        sc.frame_set(int(o["still"]))
        sc.render.filepath = os.path.join(o["out"], "still.png")
        bpy.ops.render.render(write_still=True)
        return
    if o["preview"]:  # every 4th frame at half size: check the story before a full render
        sc.render.resolution_percentage, sc.frame_step = 50, 4
    sc.render.filepath = os.path.join(o["out"], "f")
    bpy.ops.render.render(animation=True)


main()
