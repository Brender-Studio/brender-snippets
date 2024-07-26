## Name:
render_multi_camera_animation

## Blender version:
4.2.0 (LTS)

## Description:
Render multiple animations from different cameras in a blend file, with each camera's output in its own subfolder.

## Use case:
- [x] Utility
- [x] Example

## Job type:
- [x] Array
- [ ] Single job

## Envs:
Use default environment variables by Brender Studio.
- EFS_BLENDER_OUTPUT_FOLDER_PATH
- AWS_BATCH_JOB_ARRAY_INDEX

## Entrypoint:
`render_multi_camera_animation.py`

## References (video, repo):
- [N/A]

## Screenshots:
- [N/A]

## Detailed Description:
This script renders animations from multiple cameras in a Blender scene, organizing the output into separate subfolders for each camera. It's designed for efficient rendering in cloud environments like AWS Batch, utilizing GPU acceleration.

Key features:
1. GPU Acceleration: Enables CUDA GPUs and optionally CPUs for rendering.
2. Multi-Camera Support: Automatically detects and renders from all cameras in the scene.
3. Distributed Rendering: Uses job array indexing for task distribution.
4. Organized Output: Creates a subfolder for each camera's renders.
5. Environment Variable Integration: Uses environment variables for output paths and job indexing.
6. Automatic Camera Selection: Selects cameras based on job array index.
7. Scene-Specific Settings: Respects the scene's frame range and step settings.

Process:
1. Enables CUDA GPUs and CPUs for rendering.
2. Retrieves all scene cameras.
3. Selects a camera based on the job array index.
4. Creates a subfolder for the selected camera's output.
5. Renders the full animation for the selected camera.

Output Structure:
```
/output
    /Camera_001
        frame_0001.png
        frame_0002.png
        ...
    /Camera_002
        frame_0001.png
        frame_0002.png
        ...
```

This script is ideal for projects requiring multiple camera angles or perspectives of the same animation, streamlining the rendering workflow in professional and high-volume production environments.


