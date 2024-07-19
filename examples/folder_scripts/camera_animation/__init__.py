import bpy
import os
import sys

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from camera_animation.scripts.camera_path import create_camera_path
from camera_animation.scripts.render import render_animation

def main(output_directory):
    
    # Create a camera path and set the camera to follow it
    path_data = [
        (0, 0, 2), (2, 2, 2), (4, 0, 2), (6, -2, 2), (8, 0, 2)
    ]
    camera_path = create_camera_path(path_data)
    camera = bpy.data.objects['Camera']
    camera.constraints.new(type='FOLLOW_PATH').target = camera_path

    # Set the scene frame range based on the path data length
    bpy.context.scene.frame_end = len(path_data) * 50  # 50 frames per point

    render_animation(output_directory)

if __name__ == "__main__":
    blend_file = os.environ['EFS_BLENDER_FILE_PATH']
    output_directory = os.environ['EFS_BLENDER_OUTPUT_FOLDER_PATH']
    main(output_directory)