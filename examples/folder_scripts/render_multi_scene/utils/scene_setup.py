import bpy
import logging

def setup_multi_scene(config):
    scenes = []
    for scene in bpy.data.scenes:
        scene_config = setup_scene(scene, config)
        scenes.append(scene_config)
    return scenes

def setup_scene(scene, config):
    # Set render settings
    scene.render.resolution_x = config.resolution_x
    scene.render.resolution_y = config.resolution_y
    scene.render.image_settings.file_format = config.file_format

    # Get frame range
    start_frame = scene.frame_start
    end_frame = scene.frame_end
    frame_step = scene.frame_step

    logging.info(f"Scene '{scene.name}' setup complete. Frames: {start_frame} to {end_frame}, Step: {frame_step}")

    is_animation = start_frame != end_frame
    if config.render_type == 'frame':
        is_animation = False
    elif config.render_type == 'animation':
        is_animation = True
    # If render_type is 'auto', use the default is_animation value

    return {
        'name': scene.name,
        'start_frame': start_frame,
        'end_frame': end_frame,
        'frame_step': frame_step,
        'is_animation': is_animation
    }