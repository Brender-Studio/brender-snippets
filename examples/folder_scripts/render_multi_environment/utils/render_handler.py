import bpy
import os
import logging
from .environment_handler import apply_environment

def render_scene_with_environments(scene_config, config, environments):
    for env in environments:
        apply_environment(bpy.context.scene, env)
        env_name = os.path.splitext(os.path.basename(env))[0]
        if scene_config['is_animation']:
            render_animation(scene_config, config, env_name)
        else:
            render_frame(scene_config, config, env_name)
            

def render_animation(scene_config, config, env_name):
    start, end, step = calculate_frame_chunk(config.array_size, config.job_index, 
                                             scene_config['start_frame'], scene_config['end_frame'], scene_config['frame_step'])
    
    for frame in range(start, end + 1, step):
        render_frame(scene_config, config, env_name, frame)


def render_frame(scene_config, config, env_name, frame=None):
    if frame:
        bpy.context.scene.frame_set(frame)
    
    output_file = f"{scene_config['name']}_{env_name}_{frame:04d}" if frame else f"{scene_config['name']}_{env_name}_single"
    output_path = os.path.join(config.output_path, output_file)
    
    bpy.context.scene.render.filepath = output_path
    bpy.ops.render.render(write_still=True)
    
    logging.info(f"Rendered {output_file}")
    if frame:
        log_render_progress(frame, scene_config['start_frame'], scene_config['end_frame'], scene_config['frame_step'])


def calculate_frame_chunk(array_size, job_index, start_frame, end_frame, frame_step):
    total_frames = end_frame - start_frame + 1
    frames_per_job = total_frames // array_size
    extra_frames = total_frames % array_size
    
    job_start = start_frame + job_index * frames_per_job + min(job_index, extra_frames)
    job_end = job_start + frames_per_job - 1 + (1 if job_index < extra_frames else 0)
    
    return job_start, job_end, frame_step


def log_render_progress(current_frame, start_frame, end_frame, frame_step):
    total_frames = (end_frame - start_frame) // frame_step + 1
    frames_rendered = (current_frame - start_frame) // frame_step + 1
    progress = (frames_rendered / total_frames) * 100
    logging.info(f"Rendering progress: {progress:.2f}% (Frame {current_frame}/{end_frame})")