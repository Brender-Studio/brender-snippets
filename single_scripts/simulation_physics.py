# Este script añade un dominio de humo y un emisor, y luego simula y renderiza el resultado


import bpy
import os

def simulation_physics(blend_file, output_directory):
    """
    Simulate physics in a blend file and render the result.
    
    Parameters:
    - blend_file (str): The path to the blend file.
    - output_directory (str): The path to the output directory.
    """
    # Open the blend file
    bpy.ops.wm.open_mainfile(filepath=blend_file)
    
    # Set the output directory
    bpy.context.scene.render.filepath = output_directory
    
    # Add a smoke domain
    bpy.ops.mesh.primitive_cube_add(size=2, location=(0, 0, 0))
    bpy.ops.object.modifier_add(type='FLUID_SIMULATION')
    bpy.context.object.modifiers['Fluid'].fluid_type = 'DOMAIN'
    
    # Add a smoke emitter
    bpy.ops.mesh.primitive_uv_sphere_add(radius=1, location=(0, 0, 1))
    bpy.ops.object.modifier_add(type='FLUID_SIMULATION')
    bpy.context.object.modifiers['Fluid'].fluid_type = 'FLOW'
    bpy.context.object.modifiers['Fluid'].flow_settings.flow_type = 'SMOKE'
    
    # Set the resolution
    bpy.context.scene.render.engine = "BLENDER_EEVEE_NEXT"
    bpy.context.scene.eevee.taa_render_samples = 1

    # Simulate the physics
    bpy.ops.fluid.bake_data()

    # Render the frames
    bpy.ops.render.render(write_still=True)


# Usage example
blend_file = os.environ['EFS_BLENDER_FILE_PATH']
output_directory = os.environ['EFS_BLENDER_OUTPUT_FOLDER_PATH']

simulation_physics(blend_file, output_directory)