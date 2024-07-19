import bpy
import os
import logging

# Configure logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')
logger = logging.getLogger(__name__)


def render_multi_camera(cameras, output_directory):
    # Get the active frame from the scene context
    active_frame = bpy.context.scene.frame_current
    
    # Loop through each camera name and render the images
    for camera_name in cameras:
        if camera_name not in bpy.data.objects:
            logger.warning(f"Camera '{camera_name}' not found. Skipping...")
            continue
        
        # Set the active camera
        bpy.context.scene.camera = bpy.data.objects[camera_name]
        
        # Set the output path to render according to the render type (still)
        render_file_path = os.path.join(output_directory, f"{camera_name}_{active_frame:05d}.png")
        
        # Render the image
        bpy.context.scene.render.filepath = render_file_path
        bpy.ops.render.render(write_still=True)
        logger.info(f"Render saved to {render_file_path}")

# Usage example
def main():

    # Cloud Usage:
    blend_file = os.environ.get('EFS_BLENDER_FILE_PATH')
    output_directory = os.environ.get('EFS_BLENDER_OUTPUT_FOLDER_PATH')
    logger.info(msg="Environment variables", extra={"EFS_BLENDER_FILE_PATH": blend_file, "EFS_BLENDER_OUTPUT_FOLDER_PATH": output_directory})
    
    # Local Usage:
    # blend_file = "/home/dave/Escritorio/BLENDER/blend_files/cameras.blend"
    # output_directory = "/home/dave/Escritorio/BLENDER/output_camera_TEST"

    if not blend_file:
        logger.error("EFS_BLENDER_FILE_PATH environment variable is not set")
        raise ValueError("EFS_BLENDER_FILE_PATH environment variable is not set")

    if not output_directory:
        logger.error("EFS_BLENDER_OUTPUT_FOLDER_PATH environment variable is not set")
        raise ValueError("EFS_BLENDER_OUTPUT_FOLDER_PATH environment variable is not set")

    # Extract the names of the cameras from the blend file
    cameras = [obj.name for obj in bpy.data.objects if obj.type == 'CAMERA']
    
    if not cameras:
        logger.info("No cameras found in the blend file.")
        return
    
    # Log the names of the cameras
    logger.info("Cameras found: %s", ", ".join(cameras))
    
    render_multi_camera(cameras, output_directory)

if __name__ == "__main__":
    main()
