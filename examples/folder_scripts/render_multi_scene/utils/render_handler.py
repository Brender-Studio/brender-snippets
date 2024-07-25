import bpy
import os
import logging

def render_scenes(scenes, config):
    for scene in scenes:
        if scene['is_animation']:
            logging.info(f"Rendering animation for scene: {scene['name']}")
            render_animation(scene, config)
        else:
            logging.info(f"Rendering single frame for scene: {scene['name']}")
            render_frame(scene, config)



def render_animation(scene, config):
    start_frame = scene['start_frame']
    end_frame = scene['end_frame']
    frame_step = scene['frame_step']
    
    bpy.context.scene.frame_start = start_frame
    bpy.context.scene.frame_end = end_frame
    bpy.context.scene.frame_step = frame_step
    
    total_frames = (end_frame - start_frame) // frame_step + 1
    
    # Loop for register custom progress and render each frame
    for frame in range(start_frame, end_frame + 1, frame_step):
        render_frame(scene, config, frame)
        log_render_progress(frame, start_frame, end_frame, frame_step, total_frames)
        
    # If You want use bpy.ops.render(animation=True) to render all frames at once use this code and comment the loop above
    # bpy.ops.render.render(animation=True)


def render_frame(scene, config, frame=None):
    if frame is not None:
        bpy.context.scene.frame_set(frame)

    output_file = f"{scene['name']}_{frame:04d}" if frame else f"{scene['name']}_single"
    output_path = os.path.join(config.output_path, output_file)
    
    bpy.context.scene.render.filepath = output_path
    bpy.ops.render.render(write_still=True)
    
    logging.info(f"Rendered frame: {frame} - Scene: {scene['name']} - File Rendered: {output_path}")
    
    

def log_render_progress(current_frame, start_frame, end_frame, frame_step, total_frames):
    # Calculate the number of frames that have been rendered so far
    frames_rendered = (current_frame - start_frame) // frame_step + 1
    # Calculate the percentage of completion
    progress = (frames_rendered / total_frames) * 100
    logging.info(f"Rendering progress: {progress:.2f}% (Frame {current_frame}/{end_frame})")