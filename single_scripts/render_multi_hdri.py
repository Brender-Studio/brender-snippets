
# Este script cambia el HDRI del entorno y renderiza la escena para cada HDRI.


import bpy 
import os


def render_multi_hdri(blend_file, output_directory, hdri_names):
    """
    Render multiple HDRI images from a blend file.
    
    Parameters:
    - blend_file (str): The path to the blend file.
    - output_directory (str): The path to the output directory.
    - hdri_names (list): A list of HDRI names to render.
    """
    # Open the blend file
    bpy.ops.wm.open_mainfile(filepath=blend_file)
    
    # Set the output directory
    bpy.context.scene.render.filepath = output_directory
    
    # Loop through each HDRI name and render the frames
    for hdri_name in hdri_names:
        # Set the HDRI image
        bpy.data.worlds['World'].node_tree.nodes['Environment Texture'].image = bpy.data.images[hdri_name]
        
        # Render the frames
        bpy.ops.render.render(write_still=True)


# Usage example
blend_file = os.environ['EFS_BLENDER_FILE_PATH']
output_directory = os.environ['EFS_BLENDER_OUTPUT_FOLDER_PATH']

# Extact the names of the HDRI images from the blend file
hdri_names = [img.name for img in bpy.data.images if img.source == 'FILE']

# Print the names of the HDRI images
for hdri_name in hdri_names:
    print(hdri_name)

render_multi_hdri(blend_file, output_directory, hdri_names)