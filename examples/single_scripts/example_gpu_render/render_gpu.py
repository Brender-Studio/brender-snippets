import bpy
import os

def enable_gpus(device_type, use_cpus):
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

    for scene in bpy.data.scenes:
        scene.cycles.device = "GPU"

    print("Activated GPUs:", activated_gpus)
    return activated_gpus

def render_frame(scene, output_path):
    active_frame = scene.frame_current
    output_path = scene.render.filepath
    scene.render.filepath = os.path.join(output_path, f"frame_{active_frame:04d}")
    bpy.ops.render.render(write_still=True)

def main():
    use_gpu = os.environ.get('USE_GPU')
    output_path = os.environ.get('EFS_BLENDER_OUTPUT_FOLDER_PATH')

    if use_gpu == True:
        enable_gpus("CUDA", True)
        print('Using GPU for rendering')
    else:
        print('Using CPU for rendering')
        
    render_frame(bpy.context.scene, output_path)

if __name__ == "__main__":
    main()