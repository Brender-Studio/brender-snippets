import bpy
from scripts.fluid_simulation import setup_fluid_simulation
from scripts.render import render_frames
import os

def main(blend_file, output_directory):
    bpy.ops.wm.open_mainfile(filepath=blend_file)
    
    setup_fluid_simulation()
    bpy.ops.fluid.bake_data()
    render_frames(output_directory)

if __name__ == "__main__":
    blend_file = os.environ['EFS_BLENDER_FILE']
    output_directory = os.environ['EFS_BLENDER_OUTPUT_PATH']
    main(blend_file, output_directory)
