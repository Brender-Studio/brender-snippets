# Este script rota un objeto en la escena y renderiza imágenes desde diferentes ángulos para generar un dataset.

import bpy
import math


def generate_dataset(blend_file, output_directory, object_name, num_images):
    """
    Generate a dataset of images from different camera angles.
    
    Parameters:
    - blend_file (str): The path to the blend file.
    - output_directory (str): The path to the output directory.
    - object_name (str): The name of the object to rotate.
    - num_images (int): The number of images to generate.
    """
    # Open the blend file
    bpy.ops.wm.open_mainfile(filepath=blend_file)
    
    # Set the output directory
    bpy.context.scene.render.filepath = output_directory
    
    # Get the object to rotate
    obj = bpy.data.objects[object_name]
    
    # Set the rotation step
    step = 360 / num_images
    
    # Loop through each angle and render the image
    for i in range(num_images):
        # Set the rotation angle
        obj.rotation_euler[2] = math.radians(i * step)
        
        # Render the image
        bpy.ops.render.render(write_still=True)


# Usage example
blend_file = os.environ['EFS_BLENDER_FILE']
output_directory = os.environ['EFS_BLENDER_OUTPUT_PATH']
object_name = bpy.data.objects[0].name
num_images = 36

generate_dataset(blend_file, output_directory, object_name, num_images)