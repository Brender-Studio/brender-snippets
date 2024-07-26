import bpy
import os
import sys

def enable_gpus(device_type='CUDA', use_cpus=False):
    preferences = bpy.context.preferences
    cycles_preferences = preferences.addons["cycles"].preferences
    cycles_preferences.refresh_devices()
    devices = cycles_preferences.devices

    if not devices:
        raise RuntimeError("Unsupported device type")

    activated_gpus = []
    for device in devices:
        if device.type == "CPU":
            device.use = use_cpus
            print('Activated CPU:', device.name)
        else:
            device.use = True
            activated_gpus.append(device.name)
            print('Activated GPU:', device.name)

    cycles_preferences.compute_device_type = device_type

    print("Activated GPUs:", activated_gpus)
    return activated_gpus

def get_cameras(scene):
    return [obj for obj in scene.objects if obj.type == 'CAMERA']

def render_camera_animation(scene, camera, output_path):
    scene.camera = camera
    
    # Configure rendering output
    scene.render.filepath = output_path
    scene.render.image_settings.file_format = 'PNG'
    
    # Render the animation
    bpy.ops.render.render(animation=True)

def main():
    # Get environment variables
    output_folder = os.environ.get('EFS_BLENDER_OUTPUT_FOLDER_PATH', r'C:\Users\dev-admin\Desktop\spx_output')
    job_index = int(os.environ.get('AWS_BATCH_JOB_ARRAY_INDEX', '0'))
    # job_size = int(os.environ.get('AWS_BATCH_JOB_ARRAY_SIZE', '1'))
    
    # Enable CUDA GPUs and CPUs
    device_type = 'CUDA'
    use_cpus = True

    activated_gpus = enable_gpus(device_type, use_cpus)
    print("Activated GPUs:", activated_gpus)
    
    scene = bpy.context.scene
    cameras = get_cameras(scene)
    
    if not cameras:
        print("No cameras found in the scene.")
        sys.exit(1)
    
    # Select the camera based on the job index
    camera_index = job_index % len(cameras)
    selected_camera = cameras[camera_index]
    
    # Get start frame, end frame, and frame step from the scene context
    start_frame = scene.frame_start
    end_frame = scene.frame_end
    frame_step = scene.frame_step
    
    # Create the output path for this specific camera
    camera_subfolder = os.path.join(output_folder, selected_camera.name)
    os.makedirs(camera_subfolder, exist_ok=True)
    camera_output_path = os.path.join(camera_subfolder, f"frame_")

    print(f"Rendering animation for camera: {selected_camera.name}")
    print(f"Frames: {start_frame} - {end_frame}, Step: {frame_step}")
    print(f"Output path: {camera_output_path}")
    
    # Render the animation
    render_camera_animation(scene, selected_camera, camera_output_path)

if __name__ == "__main__":
    main()