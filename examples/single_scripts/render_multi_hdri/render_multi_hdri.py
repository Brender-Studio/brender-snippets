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

def ensure_world_node_tree():
    """Ensure the world has a node tree and return the environment texture node."""
    world = bpy.context.scene.world
    if world.node_tree is None:
        world.use_nodes = True
        logger.info("Created node tree for world")

    for node in world.node_tree.nodes:
        if node.type == 'TEX_ENVIRONMENT':
            return node

    logger.error("No Environment Texture node found in the World node tree")
    return None

def get_hdri_images():
    """Retrieve all HDRI images in the Blender scene."""
    hdri_images = [img for img in bpy.data.images if img.source == 'FILE']
    logger.info(f"Found {len(hdri_images)} HDRI images")
    return hdri_images

def render_hdri_image(hdri_image, output_directory, frame):
    """Render an image with the given HDRI and save to the output directory."""
    env_tex_node = ensure_world_node_tree()
    if env_tex_node is None:
        return

    logger.info(f"Processing HDRI image: {hdri_image.name}")
    env_tex_node.image = hdri_image

    render_file_path = os.path.join(output_directory, f"{hdri_image.name}_{frame:05d}.png")
    logger.info(f"Render file path set to: {render_file_path}")

    bpy.context.scene.render.filepath = render_file_path
    logger.info("Starting render...")
    bpy.ops.render.render(write_still=True)
    logger.info(f"Render completed and saved to {render_file_path}")

def main():
    """Main function to execute the HDRI rendering process."""
    output_directory = get_environment_variable('EFS_BLENDER_OUTPUT_FOLDER_PATH')
    hdri_images = get_hdri_images()

    if not hdri_images:
        logger.warning("No HDRI images found. Exiting...")
        return

    active_frame = bpy.context.scene.frame_current
    for hdri_image in hdri_images:
        render_hdri_image(hdri_image, output_directory, active_frame)

if __name__ == "__main__":
    logger.info("Script started")
    main()
    logger.info("Script completed")
