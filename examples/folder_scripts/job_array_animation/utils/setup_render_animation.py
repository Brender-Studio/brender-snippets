import bpy
import os
import logging



def setup_scene(resolution_x, resolution_y, file_format='PNG'):
    bpy.context.scene.render.resolution_x = resolution_x
    bpy.context.scene.render.resolution_y = resolution_y
    bpy.context.scene.render.image_settings.file_format = file_format
    
    start_frame = bpy.context.scene.frame_start
    end_frame = bpy.context.scene.frame_end
    frame_step = bpy.context.scene.frame_step
    
    logging.info(f"Scene setup complete. Rendering frames {start_frame} to {end_frame} with step {frame_step}")
    
    return start_frame, end_frame, frame_step



def calculate_frame_chunk(array_size, job_index, start_frame, end_frame, frame_step):
    start_frame = int(start_frame)
    end_frame = int(end_frame)
    frame_step = int(frame_step)
    array_size = int(array_size)
    job_index = int(job_index)
    total_frames = end_frame - start_frame + 1  
    frames_per_chunk = total_frames // array_size
    extra_frames = total_frames % array_size
    
    start_frame = start_frame + job_index * frames_per_chunk + min(job_index, extra_frames)
    end_frame = start_frame + frames_per_chunk + (1 if job_index < extra_frames else 0) - 1  
    
    return start_frame, end_frame, frame_step


def render_animation(start_frame, end_frame, frame_step, array_size, job_index, output_path):
    start_frame, end_frame, frame_step = calculate_frame_chunk(array_size, job_index, start_frame, end_frame, frame_step)
    for frame in range(int(start_frame), int(end_frame) + 1, int(frame_step)):  
        bpy.context.scene.frame_set(frame)
        render_file_path = os.path.join(output_path, f"{frame:05d}")
        bpy.context.scene.render.filepath = render_file_path
        bpy.ops.render.render(write_still=True)
        
        log_render_progress(frame, start_frame, end_frame, frame_step)


        
        
def log_render_progress(current_frame, start_frame, end_frame, frame_step):
    total_frames = (end_frame - start_frame) // frame_step + 1
    frames_rendered = (current_frame - start_frame) // frame_step + 1
    progress = (frames_rendered / total_frames) * 100
    logging.info(f"Rendering progress: {progress:.2f}% (Frame {current_frame}/{end_frame})")