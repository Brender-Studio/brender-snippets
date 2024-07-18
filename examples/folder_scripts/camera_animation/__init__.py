import bpy
import os
from . import create_camera_path, render_animation

def main(blend_file, output_directory):
    bpy.ops.wm.open_mainfile(filepath=blend_file)
    
    path_data = [
        (0, 0, 2), (2, 2, 2), (4, 0, 2), (6, -2, 2), (8, 0, 2)
    ]
    camera_path = create_camera_path(path_data)
    camera = bpy.data.objects['Camera']
    camera.constraints.new(type='FOLLOW_PATH').target = camera_path

    render_animation(output_directory)

if __name__ == "__main__":
    blend_file = os.environ['EFS_BLENDER_FILE']
    output_directory = os.environ['EFS_BLENDER_OUTPUT_PATH']
    main(blend_file, output_directory)
