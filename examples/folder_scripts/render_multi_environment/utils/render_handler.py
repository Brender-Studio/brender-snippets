import bpy
import os
import logging
from .environment_handler import apply_environment


def render_scene_with_environments(scene_config, config, environments):
    for env in environments:
        apply_environment(bpy.context.scene, env)
        env_name = os.path.splitext(os.path.basename(env))[0]
        if scene_config['is_animation']:
            logging.info(f"Rendering animation for environment: {env_name}")
            render_animation(scene_config, config, env_name)
        else:
            logging.info(f"Rendering single frame for environment: {env_name}")
            render_frame(scene_config, config, env_name)


def render_animation(scene_config, config, env_name):
    start_frame = scene_config['start_frame']
    end_frame = scene_config['end_frame']
    frame_step = scene_config['frame_step']

    bpy.context.scene.frame_start = start_frame
    bpy.context.scene.frame_end = end_frame
    bpy.context.scene.frame_step = frame_step
    
    total_frames = (end_frame - start_frame) // frame_step + 1

    # Loop for register custom progress and render each frame
    for frame in range(start_frame, end_frame + 1, frame_step):
        render_frame(scene_config, config, env_name, frame)
        log_render_progress(frame, start_frame, end_frame, frame_step, total_frames)
        
    # If You want use bpy.ops.render(animation=True) to render all frames at once use this code and comment the loop above
    # bpy.ops.render.render(animation=True)


def render_frame(scene_config, config, env_name, frame=None):
    if frame is not None:
        bpy.context.scene.frame_set(frame)

    output_file = generate_output_filename(scene_config['name'], env_name, frame)
    output_path = os.path.join(config.output_path, output_file)
    
    bpy.context.scene.render.filepath = output_path
    bpy.ops.render.render(write_still=True)
    
    logging.info(f"Rendered {output_file}")


def generate_output_filename(scene_name, env_name, frame):
    if frame is not None:
        return f"{scene_name}_{env_name}_{frame:04d}"
    return f"{scene_name}_{env_name}_single"


def log_render_progress(current_frame, start_frame, end_frame, frame_step, total_frames):
    frames_rendered = (current_frame - start_frame) // frame_step + 1
    progress = (frames_rendered / total_frames) * 100
    logging.info(f"Rendering progress: {progress:.2f}% (Frame {current_frame}/{end_frame})")