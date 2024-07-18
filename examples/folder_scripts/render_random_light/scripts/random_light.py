import bpy
import random

def set_random_light():
    light = bpy.data.objects['Light']
    light.data.energy = random.uniform(300, 500)
    light.location = (random.uniform(-5, 5), random.uniform(-5, 5), random.uniform(5, 10))
