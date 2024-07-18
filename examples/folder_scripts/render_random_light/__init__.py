import bpy
from .scripts import random_light, render
import os
import math

def main(blend_file, output_directory, num_images):
    bpy.ops.wm.open_mainfile(filepath=blend_file)
    
    obj = bpy.data.objects[0]
    step = 360 / num_images
    
    for i in range(num_images):
        obj.rotation_euler[2] = math.radians(i * step)
        random_light.set_random_light()
        render.render_image(f"{output_directory}/image_{i}.png")

if __name__ == "__main__":
    blend_file = os.environ['EFS_BLENDER_FILE_PATH']
    output_directory = os.environ['EFS_BLENDER_OUTPUT_FOLDER_PATH']
    num_images = 36
    main(blend_file, output_directory, num_images)
