# Este script aplica texturas aleatorias a un objeto seleccionado.

import bpy
import random
import os


def render_random_texture(blend_file, output_directory, object_name, num_images, textures):
    """
    Render images with random textures applied to an object.
    
    Parameters:
    - blend_file (str): The path to the blend file.
    - output_directory (str): The path to the output directory.
    - object_name (str): The name of the object to apply textures to.
    - num_images (int): The number of images to generate.
    - textures (list): A list of texture names to apply.
    """
    # Open the blend file
    bpy.ops.wm.open_mainfile(filepath=blend_file)
    
    # Set the output directory
    bpy.context.scene.render.filepath = output_directory
    
    # Get the object to apply textures to
    obj = bpy.data.objects[object_name]
    
    # Get the material of the object
    mat = obj.data.materials[0]
    
    # Loop through each image and apply a random texture
    for i in range(num_images):
        # Set the seed for the random texture
        bpy.data.textures['Texture'].noise_scale = i
        
        # Assign the texture to the material
        mat.texture_slots[0].texture = bpy.data.textures[textures[random.randint(0, len(textures) - 1)]]
        
        # Render the image
        bpy.ops.render.render(write_still=True)



# Usage example

blend_file = os.environ['EFS_BLENDER_FILE_PATH']
output_directory = os.environ['EFS_BLENDER_OUTPUT_FOLDER_PATH']

# Get the name of the object to apply textures to
object_name = bpy.data.objects[0].name


# Set the number of images to generate
num_images = 10

# Get the names of the textures from the blend file
textures = [tex.name for tex in bpy.data.textures]

# Print the names of the textures
for texture_name in textures:
    print(texture_name)


render_random_texture(blend_file, output_directory, object_name, num_images, textures)