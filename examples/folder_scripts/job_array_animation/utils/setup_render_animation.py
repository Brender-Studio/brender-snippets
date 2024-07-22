import bpy
import os
import logging



def setup_scene(resolution_x, resolution_y, file_format='PNG'):
    # Set the render resolution
    bpy.context.scene.render.resolution_x = resolution_x
    bpy.context.scene.render.resolution_y = resolution_y
    
    # Set the output file format
    bpy.context.scene.render.image_settings.file_format = file_format
    
    # Get the animation frame range and step from the Blender scene
    start_frame = bpy.context.scene.frame_start
    end_frame = bpy.context.scene.frame_end
    frame_step = bpy.context.scene.frame_step
    
    # Log the scene setup information
    logging.info(f"Scene setup complete. Rendering frames {start_frame} to {end_frame} with step {frame_step}")
    
    # Return the frame range and step
    return start_frame, end_frame, frame_step


def calculate_frame_chunk(array_size, job_index, start_frame, end_frame, frame_step):
    # Convert all inputs to integers
    start_frame = int(start_frame)
    end_frame = int(end_frame)
    frame_step = int(frame_step)
    array_size = int(array_size)
    job_index = int(job_index)
    
    # Calculate the total number of frames
    total_frames = end_frame - start_frame + 1  
    
    # Calculate the number of frames per chunk
    frames_per_chunk = total_frames // array_size
    
    # Calculate the number of extra frames that don't fit evenly into chunks
    extra_frames = total_frames % array_size
    
    # Calculate the start frame for this specific job
    start_frame = start_frame + job_index * frames_per_chunk + min(job_index, extra_frames)
    
    # Calculate the end frame for this specific job
    end_frame = start_frame + frames_per_chunk + (1 if job_index < extra_frames else 0) - 1  
    
    return start_frame, end_frame, frame_step


def render_animation(start_frame, end_frame, frame_step, array_size, job_index, output_path):
    # Recalculate the frame chunk for this specific job
    start_frame, end_frame, frame_step = calculate_frame_chunk(array_size, job_index, start_frame, end_frame, frame_step)
    
    # Iterate through each frame in the calculated chunk
    for frame in range(int(start_frame), int(end_frame) + 1, int(frame_step)):  
        # Set the current frame in Blender's scene
        bpy.context.scene.frame_set(frame)
        
        # Construct the output file path for the current frame
        # The frame number is formatted as a 5-digit number (e.g., 00001.png)
        render_file_path = os.path.join(output_path, f"{frame:05d}")
        
        # Set the render output path in Blender
        bpy.context.scene.render.filepath = render_file_path
        
        # Render the current frame and save it
        bpy.ops.render.render(write_still=True)
        
        # Log the progress of the rendering
        log_render_progress(frame, start_frame, end_frame, frame_step)

        
        
def log_render_progress(current_frame, start_frame, end_frame, frame_step):
    """
    Log the progress of the rendering process.

    Parameters:
    current_frame (int): The frame currently being rendered.
    start_frame (int): The starting frame of the render job.
    end_frame (int): The ending frame of the render job.
    frame_step (int): The step between frames to be rendered.

    This function calculates the progress of the rendering in percentage and logs it.
    The percentage is based on the number of frames that have been rendered out of the total number of frames to be rendered.
    """
    # Calculate the total number of frames to be rendered
    total_frames = (end_frame - start_frame) // frame_step + 1

    # Calculate the number of frames that have been rendered so far
    frames_rendered = (current_frame - start_frame) // frame_step + 1

    # Calculate the percentage of completion
    progress = (frames_rendered / total_frames) * 100

    # Log the progress with the percentage and the current frame details
    logging.info(f"Rendering progress: {progress:.2f}% (Frame {current_frame}/{end_frame})")
