# Este script rota un objeto en la escena y renderiza imágenes desde diferentes ángulos para generar un dataset.

import bpy
import math
import os
import logging

# Configure logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')
logger = logging.getLogger(__name__)


def generate_dataset(blend_file, output_directory, object_name, num_images):
    """
    Generate a dataset of images from different camera angles.
    
    Parameters:
    - blend_file (str): The path to the blend file.
    - output_directory (str): The path to the output directory.
    - object_name (str): The name of the object to rotate.
    - num_images (int): The number of images to generate.
    """
    
    # Get the object to rotate
    obj = bpy.data.objects[object_name]
    logger.info(f"Object '{object_name}' found.")
    
    # Set the rotation step
    step = 360 / num_images
    logger.info(f"Rotation step: {step}")
    
    # Get te active frame from the scene context
    active_frame = bpy.context.scene.frame_current
    logger.info(f"Active frame: {active_frame}")
    
    # Set the output directory
    render_file_path = os.path.join(output_directory, f"{object_name}_{active_frame:05d}.png")
    logger.info(f"Output directory: {output_directory}")
    
    # Loop through each angle and render the image
    for i in range(num_images):
        # Set the rotation angle
        obj.rotation_euler[2] = math.radians(i * step)
        
        # Render the image
        bpy.context.scene.render.filepath = render_file_path
        bpy.ops.render.render(write_still=True)
        logger.info(f"Render saved to {render_file_path}")


# Usage example
blend_file = os.environ['EFS_BLENDER_FILE_PATH']
output_directory = os.environ['EFS_BLENDER_OUTPUT_FOLDER_PATH']
object_name = bpy.data.objects[0].name
num_images = 36

generate_dataset(blend_file, output_directory, object_name, num_images)