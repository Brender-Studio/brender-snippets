import bpy
import os
import logging

# Configure logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')
logger = logging.getLogger(__name__)


def get_environment_variable(var_name):
    """Retrieve the environment variable or raise an error if not found."""
    value = os.environ.get(var_name)
    if value is None:
        logger.error(f"{var_name} environment variable is not set")
        raise ValueError(f"{var_name} environment variable is not set")
    return value


def get_cameras():
    """Retrieve the names of all cameras in the Blender scene."""
    cameras = [obj.name for obj in bpy.data.objects if obj.type == 'CAMERA']
    if not cameras:
        logger.info("No cameras found in the blend file.")
    else:
        logger.info("Cameras found: %s", ", ".join(cameras))
    return cameras


def render_image(camera_name, output_directory, frame):
    """Render an image from the specified camera and save to the output directory."""
    if camera_name not in bpy.data.objects:
        logger.warning(f"Camera '{camera_name}' not found. Skipping...")
        return

    # Set the active camera
    bpy.context.scene.camera = bpy.data.objects[camera_name]
    
    # Construct the output file path
    render_file_path = os.path.join(output_directory, f"{camera_name}_{frame:05d}.png")
    
    # Set the render file path and execute the render
    bpy.context.scene.render.filepath = render_file_path
    bpy.ops.render.render(write_still=True)
    
    logger.info(f"Render saved to {render_file_path}")

def render_multi_camera(cameras, output_directory):
    """Render images for multiple cameras."""
    active_frame = bpy.context.scene.frame_current
    for camera in cameras:
        render_image(camera, output_directory, active_frame)

def main():
    """Main function to execute the rendering process."""
    output_directory = get_environment_variable('EFS_BLENDER_OUTPUT_FOLDER_PATH')
    cameras = get_cameras()
    if cameras:
        render_multi_camera(cameras, output_directory)

if __name__ == "__main__":
    main()
