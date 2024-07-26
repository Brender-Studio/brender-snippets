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

def get_object_by_name(name):
    """Retrieve an object by name from the Blender scene."""
    obj = bpy.data.objects.get(name)
    if obj is None:
        logger.error(f"Object '{name}' not found in the scene.")
    return obj

def render_with_material(obj, material, output_directory, base_material):
    """Apply a material to the object, render, and save the result."""
    obj.active_material = material
    logger.info(f"Applied material: {material.name}")
    
    output_path = os.path.join(output_directory, f"{obj.name}_{material.name}.png")
    bpy.context.scene.render.filepath = output_path
    
    logger.info(f"Starting render with material: {material.name}")
    bpy.ops.render.render(write_still=True)
    logger.info(f"Render saved to: {output_path}")

def render_multi_material(object_name, output_directory):
    """Main function to render images with different materials applied to an object."""
    obj = get_object_by_name(object_name)
    if obj is None:
        return
    
    original_material = obj.active_material
    
    all_materials = bpy.data.materials
    logger.info(f"Found {len(all_materials)} materials in the scene.")
    
    for material in all_materials:
        render_with_material(obj, material, output_directory, original_material)
    
    obj.active_material = original_material
    logger.info("Original material restored")

def main():
    """Main function to handle environment variables and execute rendering."""
    logger.info("Script started...")
    
    object_name = get_environment_variable('BLENDER_OBJECT_NAME')
    output_directory = get_environment_variable('EFS_BLENDER_OUTPUT_FOLDER_PATH')
    
    render_multi_material(object_name, output_directory)
    logger.info("Multi-material rendering completed.")

if __name__ == "__main__":
    main()
