import bpy
import os
import logging
import sys

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from job_array_animation.utils.setup_render_animation import calculate_frame_chunk, render_animation, setup_scene, log_render_progress


# Configurar logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

output_path = os.environ.get('EFS_BLENDER_OUTPUT_FOLDER_PATH')
array_size = os.environ.get('AWS_BATCH_JOB_ARRAY_SIZE')
job_index = os.environ.get('AWS_BATCH_JOB_ARRAY_INDEX')


def main():
    start_frame, end_frame, frame_step = setup_scene(1920,1080, 'PNG')
    
    start, end, step = calculate_frame_chunk(array_size, job_index, start_frame, end_frame, frame_step)
    
    render_animation(start, end, step, array_size, job_index, output_path)
    


if __name__ == "__main__":
    main()