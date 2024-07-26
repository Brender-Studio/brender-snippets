# Multi-Environment Blender Renderer for AWS Batch

## Author:
Brender Studio

## Blender Version:
Blender 4.2 (LTS)

## Description
This script facilitates distributed rendering of a single scene with multiple environments using AWS Batch Job Array. It's optimized for integration with Brender Studio, allowing for scalable and parallel processing across multiple compute resources.

The script is designed to render a scene with different HDR or EXR environment maps. It sets up the rendering parameters, applies each environment to the scene, and manages the rendering process across all jobs in the array.

## Key Features:
- **Multi-Environment Handling**: Processes the scene with all environment maps found in the assets folder.
- **Scene Configuration**: Sets up the scene's resolution and output format in Blender.
- **Environment Application**: Applies each environment map to the scene before rendering.
- **Rendering and Logging**: Executes the rendering of frames or animations for each environment and logs progress for monitoring job completion.

This script demonstrates how to utilize Brender Studio's capability to handle custom scripts for cloud-based rendering of Blender projects with multiple lighting environments.


## Entrypoint:
The entry point is the `main.py` file in the project root directory.

## Project Structure:
```
render_multi_environment/
  ├── assets
  │   ├── metro_vijzelgracht_4k.exr
  │   ├── README.md
  │   ├── rosendal_plains_2_4k.exr
  │   └── rural_asphalt_road_4k.exr
  ├── config
  │   ├── __init__.py
  │   └── render_config.py
  ├── main.py
  ├── README.md
  └── utils
      ├── aws_batch_utils.py
      ├── environment_handler.py
      ├── render_handler.py
      └── scene_setup.py
```


## Use Case:
- [x] Example
- [x] Utility

## Job Type:
- [x] Array
- [x] Single job



## Envs:

### Default ENVS
These are the default environment variables that Brender Studio provides for your jobs:
| **Key**                            | **Value**                 | **Env Type**   |
| ---------------------------------- | ------------------------- | -------------- |
| **EFS_BLENDER_OUTPUT_FOLDER_PATH** | /mnt/efs/projects//output | Brender Studio |



### Custom ENV
| **Key**                            | **Value**                 | **Env Type** |
| ---------------------------------- | ------------------------- | ------------ |
| **<RENDER_TYPE>**                  | **<CUSTOM_VALUE>**        | Custom       |

- **`RENDER_TYPE`**: Determines whether to render a single frame or an animation. Possible values are:
  - `'auto'` (default): Automatically determines based on the scene's frame range.
  - `'frame'`: Forces rendering of a single frame.
  - `'animation'`: Forces rendering as an animation.


> **Note**: This script is designed for CPU-based rendering, ensuring compatibility with a wide range of AWS instance types. If you wish to utilize GPU-based rendering, please create a custom function to enable GPU support. Refer to the example provided in the [example_gpu_render](/examples/single_scripts/example_gpu_render/render_gpu.py) file for guidance.


## Reference:
- [Poly Haven HDRI'S](https://polyhaven.com/hdris)
- [AWS Batch](https://docs.aws.amazon.com/batch/latest/userguide/job_env_vars.html)
- [Dev Container to Test](https://github.com/Brender-Studio/brender-studio-devcontainer)



