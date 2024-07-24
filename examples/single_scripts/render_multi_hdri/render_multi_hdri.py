import bpy 
import os
import logging


# Configure logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')
logger = logging.getLogger(__name__)

def render_multi_hdri(output_directory):
    logger.info(f"Starting render_multi_hdri with output directory: {output_directory}")
    
    # Get the active frame from the scene context
    active_frame = bpy.context.scene.frame_current
    logger.info(f"Active frame: {active_frame}")
    
    # Ensure the world has a node tree
    world = bpy.context.scene.world
    if world.node_tree is None:
        world.use_nodes = True
        logger.info("Created node tree for world")
    
    # Get the Environment Texture node
    env_tex_node = None
    for node in world.node_tree.nodes:
        if node.type == 'TEX_ENVIRONMENT':
            env_tex_node = node
            break
    
    if env_tex_node is None:
        logger.error("No Environment Texture node found in the World node tree")
        return
    else:
        logger.info("Found Environment Texture node")
    
    # Get all HDRI images
    hdri_images = [img for img in bpy.data.images if img.source == 'FILE']
    logger.info(f"Found {len(hdri_images)} HDRI images")
    
    if not hdri_images:
        logger.warning("No HDRI images found in the scene")
        return
    
    # Loop through each HDRI image and render
    for hdri_image in hdri_images:
        logger.info(f"Processing HDRI image: {hdri_image.name}")
        
        # Set the HDRI image
        env_tex_node.image = hdri_image
        logger.info(f"HDRI image set to {hdri_image.name}")
        
        # Set the output path to render
        render_file_path = os.path.join(output_directory, f"{hdri_image.name}_{active_frame:05d}.png")
        logger.info(f"Render file path set to: {render_file_path}")
        
        # Render the image
        bpy.context.scene.render.filepath = render_file_path
        logger.info("Starting render...")
        bpy.ops.render.render(write_still=True)
        logger.info(f"Render completed and saved to {render_file_path}")

if __name__ == "__main__":
    logger.info("Script started")
    
    # Get the environment variables
    blend_file = os.environ.get('EFS_BLENDER_FILE_PATH')
    output_directory = os.environ.get('EFS_BLENDER_OUTPUT_FOLDER_PATH')
    
    
    if not output_directory:
        logger.error("Output directory not specified")
        raise ValueError("Output directory not specified")
    
    
    render_multi_hdri(output_directory)
    
    logger.info("Script completed")