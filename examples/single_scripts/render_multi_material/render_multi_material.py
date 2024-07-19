import bpy
import os
import logging

# Configure logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')
logger = logging.getLogger(__name__)

def render_multi_material(object_name, output_directory):
    
    # Get the object
    obj = bpy.data.objects.get(object_name)
    if obj is None:
        logger.error(f"Object '{object_name}' not found in the scene.")
        return
    
    # Get the original material
    original_material = obj.active_material
    
    # Get all materials in the scene
    all_materials = bpy.data.materials
    logger.info(f"Found {len(all_materials)} materials in the scene.")
    
    # Loop through each material and render
    for material in all_materials:
        # Apply the material to the object
        obj.active_material = material
        logger.info(f"Applied material: {material.name}")
        
        # Set the output path
        output_path = os.path.join(output_directory, f"{object_name}_{material.name}.png")
        bpy.context.scene.render.filepath = output_path
        
        # Render
        logger.info(f"Starting render with material: {material.name}")
        bpy.ops.render.render(write_still=True)
        logger.info(f"Render saved to: {output_path}")
    
    # Restore the original material
    obj.active_material = original_material
    logger.info("Original material restored")

if __name__ == "__main__":
    logger.info("Script started...")
    
    # Cloud Usage
    # object_name = os.environ['EFS_BLENDER_OBJECT_NAME']
    # output_directory = os.environ['EFS_BLENDER_OUTPUT_FOLDER_PATH']
    
    # Local Usage
    object_name = "your_object_name"
    output_directory = "/path/to/output/directory"  
    
    if not output_directory:
        logger.error("Output directory not specified.")
        exit()
    
    render_multi_material(object_name, output_directory)
    logger.info("Multi-material rendering completed.")
