# Enable GPUs for Rendering in AWS Batch

## Name:
Enable GPUs for Rendering

## Blender Version:
4.2 (LTS)

## Script Description:
This script enables the use of GPUs for rendering in Blender using Brender Studio. It checks for available devices (CPU and GPU), activates them, and configures Blender's Cycles rendering engine to use the GPUs. Additionally, it renders the current frame and saves the output to a specified path.

## Type:
- [ ] Utility
- [x] Example

## Job Type:
- [ ] Array
- [x] Single job

## Envs:
Use default environment variables by Brender Studio:
- `USE_GPU` : Set to `True` to enable GPU rendering, otherwise set to `False`.
- `EFS_BLENDER_OUTPUT_FOLDER_PATH` : Specifies the output folder path where the rendered frames will be saved.


## Code:
- [render_gpu.py](./render_gpu.py)


## Entrypoint:
- The entry point for this script is the `render_gpu.py` function.


