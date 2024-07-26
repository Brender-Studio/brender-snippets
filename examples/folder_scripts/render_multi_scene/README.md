# Multi-Scene Blender Renderer for AWS Batch


## Author:
Brender Studio

## Blender Version:
Blender 4.2 (LTS)

## Script Description
This script facilitates distributed rendering of multiple scenes from a Blender file using AWS Batch Job Array. It's optimized for integration with Brender Studio, allowing for scalable and parallel processing across multiple compute resources.

The script is designed to handle both single frame and animation rendering for each scene in the Blender file. It sets up the rendering parameters, calculates frame ranges for animations, and manages the rendering process across all jobs in the array.

## Key features:
- **Multi-Scene Handling**: Processes all scenes within the Blender file.
- **Scene Configuration**: Sets up each scene's resolution and output format in Blender.
- **Rendering and Logging**: Executes the rendering of frames or animations and logs progress for monitoring job completion.

This script demonstrates how to utilize Brender Studio's capability to handle custom scripts for cloud-based rendering of complex Blender projects with multiple scenes.

## Entrypoint:
The entry point is the `main.py` file in the project root directory.

## Use Case:
- [x] Example
- [x] Utility

## Job Type:
- [x] Array
- [x] Single job


> **Note**: This script is designed for CPU-based rendering, ensuring compatibility with a wide range of AWS instance types. If you wish to utilize GPU-based rendering, please create a custom function to enable GPU support. Refer to the example provided in the [example_gpu_render](/examples/single_scripts/example_gpu_render/render_gpu.py) file for guidance.

## Envs:

### Default ENVS
These are the default environment variables that Brender Studio provides for your jobs:
| **Key**                            | **Value**                 | **Env Type**   |
| ---------------------------------- | ------------------------- | -------------- |
| **EFS_BLENDER_OUTPUT_FOLDER_PATH** | /mnt/efs/projects//output | Brender Studio |



### Custom ENV
| **Key**                            | **Value**                 | **Actions** |
| ---------------------------------- | ------------------------- | ----------- |
| **<RENDER_TYPE>**                  | **<CUSTOM_VALUE>**        | Custom      |

- **`RENDER_TYPE`**: Determines whether to render a single frame or an animation. Possible values are:
  - `'auto'` (default): Automatically determines based on the scene's frame range.
  - `'frame'`: Forces rendering of a single frame.
  - `'animation'`: Forces rendering as an animation.


>Note: Ensure that any custom environment variables you add are properly referenced and handled in your script. For instance, you can retrieve custom variables in your Python script using `os.environ.get('CUSTOM_VARIABLE_NAME')`.


## Project Structure (tree):
```
render_multi_scene/
  ├── config
  │   ├── __init__.py
  │   └── render_config.py
  ├── main.py
  ├── README.md
  └── utils
      ├── aws_batch_utils.py
      ├── __init__.py
      ├── render_handler.py
      └── scene_setup.py
```

## References:
- [Dev Container to Test](https://github.com/Brender-Studio/brender-studio-devcontainer)

