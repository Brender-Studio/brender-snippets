# Multi-Environment Blender Renderer for AWS Batch

## Name:
Multi-Environment Blender Renderer

## Blender Version:
Blender 4.2 (LTS)

## Script Description
This script facilitates distributed rendering of a single scene with multiple environments using AWS Batch Job Array. It's optimized for integration with Brender Studio, allowing for scalable and parallel processing across multiple compute resources.

The script is designed to render a scene with different HDR or EXR environment maps. It sets up the rendering parameters, applies each environment to the scene, and manages the rendering process across all jobs in the array.

Key functionalities include:
- **Multi-Environment Handling**: Processes the scene with all environment maps found in the assets folder.
- **Scene Configuration**: Sets up the scene's resolution and output format in Blender.
- **Environment Application**: Applies each environment map to the scene before rendering.
- **Rendering and Logging**: Executes the rendering of frames or animations for each environment and logs progress for monitoring job completion.

This script demonstrates how to utilize Brender Studio's capability to handle custom scripts for cloud-based rendering of Blender projects with multiple lighting environments.

## Type:
- [x] Example
- [x] Utility

## Job Type:
- [x] Array

## Envs:

### Default Environment Variables from Brender Studio
These are the default environment variables that Brender Studio provides for your jobs:

- **`EFS_BLENDER_OUTPUT_FOLDER_PATH`**: Specifies the output path where the rendered frames will be saved.
- **`AWS_BATCH_JOB_ARRAY_SIZE`**: Indicates the total number of jobs in the array.
- **`AWS_BATCH_JOB_ARRAY_INDEX`**: Represents the index of the current job within the array.

### Custom Environment Variables
In addition to the default variables, this script uses a custom environment variable:

- **`RENDER_TYPE`**: Determines whether to render a single frame or an animation. Possible values are:
  - `'auto'` (default): Automatically determines based on the scene's frame range.
  - `'frame'`: Forces rendering of a single frame.
  - `'animation'`: Forces rendering as an animation.

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

## Entrypoint:
The entry point is the `main.py` file in the project root directory.


## Usage:

### Step 1: Download the Script
Download the script and place it in the appropriate directory on your local machine.

### Step 2: Prepare the Environment Maps
Change the environment maps in the `assets` folder to the desired HDR or EXR files.

### Step 3: Configure the Scene
Modify the `render_config.py` file in the `config` folder to set up the render settings for the scene.

### Step 4: Upload the Script to Brender Studio
Upload the script to Brender Studio and configure the job settings as needed to run the script on AWS Render Farm.

### Step 5: Execute the Job
Submit the job to Brender Studio to start the rendering process with multiple environment maps.

## Reference:
- [Poly Haven](https://polyhaven.com/hdris)

## Note:
This script is intended to be executed as part of an AWS Batch Job Array. Ensure that the necessary environment variables are properly set up and environment map files are placed in the `assets` folder before execution.

## Tags:
#blender #aws-batch #job-array #multi-environment-rendering #distributed-rendering
