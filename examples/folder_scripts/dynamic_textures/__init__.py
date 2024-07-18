import bpy
from scripts.texture_manager import apply_random_texture
from scripts.render import render_image
import os

def main(blend_file, output_directory, num_images, textures):
    bpy.ops.wm.open_mainfile(filepath=blend_file)
    
    obj = bpy.data.objects[0]
    
    for i in range(num_images):
        apply_random_texture(obj, textures)
        render_image(f"{output_directory}/image_{i}.png")

if __name__ == "__main__":
    blend_file = os.environ['EFS_BLENDER_FILE']
    output_directory = os.environ['EFS_BLENDER_OUTPUT_PATH']
    num_images = 10
    textures = [tex.name for tex in bpy.data.textures]
    main(blend_file, output_directory, num_images, textures)
