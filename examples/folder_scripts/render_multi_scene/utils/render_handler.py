import bpy
import os
import logging

def render_scenes(scenes, config):
    for scene in scenes:
        if scene['is_animation']:
            render_animation(scene, config)
        else:
            render_frame(scene, config)

def render_animation(scene, config):
    start, end, step = calculate_frame_chunk(config.array_size, config.job_index, 
                                             scene['start_frame'], scene['end_frame'], scene['frame_step'])
    
    for frame in range(start, end + 1, step):
        render_frame(scene, config, frame)

def render_frame(scene, config, frame=None):
    bpy.context.window.scene = bpy.data.scenes[scene['name']]
    if frame:
        bpy.context.scene.frame_set(frame)
    
    output_file = f"{scene['name']}_{frame if frame else 'single'}"
    output_path = os.path.join(config.output_path, output_file)
    
    bpy.context.scene.render.filepath = output_path
    bpy.ops.render.render(write_still=True)
    
    logging.info(f"Rendered {output_file}")

def calculate_frame_chunk(array_size, job_index, start_frame, end_frame, frame_step):
    total_frames = end_frame - start_frame + 1
    frames_per_job = total_frames // array_size
    extra_frames = total_frames % array_size
    
    job_start = start_frame + job_index * frames_per_job + min(job_index, extra_frames)
    job_end = job_start + frames_per_job - 1 + (1 if job_index < extra_frames else 0)
    
    return job_start, job_end, frame_step