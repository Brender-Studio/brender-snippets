import bpy
import random

def apply_random_texture(obj, textures):
    mat = obj.data.materials[0]
    tex = bpy.data.textures[random.choice(textures)]
    mat.texture_slots[0].texture = tex
