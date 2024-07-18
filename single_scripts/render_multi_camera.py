
# Este script configura múltiples cámaras y permite renderizar la escena desde cada una de ellas.

def render_multi_camera(blend_file, cameras, output_directory):
    """
    Render multiple images from different cameras in a blend file.
    
    Parameters:
    - blend_file (str): The path to the blend file.
    - cameras (list): A list of camera names to render.
    - output_directory (str): The path to the output directory.
    """
    # Open the blend file
    bpy.ops.wm.open_mainfile(filepath=blend_file)
    
    # Set the output directory
    bpy.context.scene.render.filepath = output_directory
    
    # Loop through each camera name and render the images
    for camera_name in cameras:
        # Set the active camera
        bpy.context.scene.camera = bpy.data.objects[camera_name]
        
        # Render the image
        bpy.ops.render.render(write_still=True)



# Usage example

blend_file = os.environ['EFS_BLENDER_FILE']
output_directory = os.environ['EFS_BLENDER_OUTPUT_PATH']

# Extract the names of the cameras from the blend file
cameras = [obj.name for obj in bpy.data.objects if obj.type == 'CAMERA']

# Print the names of the cameras
for camera_name in cameras:
    print(camera_name)

render_multi_camera(blend_file, cameras, output_directory)