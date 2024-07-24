# Multi-Scene Blender Renderer for AWS Batch

## Name:
Multi-Scene Blender Renderer

## Blender Version:
Blender 4.2 (LTS)

## Script Description
This script facilitates distributed rendering of multiple scenes from a Blender file using AWS Batch Job Array. It's optimized for integration with Brender Studio, allowing for scalable and parallel processing across multiple compute resources.

The script is designed to handle both single frame and animation rendering for each scene in the Blender file. It sets up the rendering parameters, calculates frame ranges for animations, and manages the rendering process across all jobs in the array.

Key functionalities include:
- **Multi-Scene Handling**: Processes all scenes within the Blender file.
- **Scene Configuration**: Sets up each scene's resolution and output format in Blender.
- **Frame Chunk Calculation**: For animations, computes the frame ranges for each job based on the total animation length and job array size.
- **Rendering and Logging**: Executes the rendering of frames or animations and logs progress for monitoring job completion.

This script demonstrates how to utilize Brender Studio's capability to handle custom scripts for cloud-based rendering of complex Blender projects with multiple scenes.

## Type:
- [x] Example
- [x] Utility

## Job Type:
- [x] Array

## Envs:

### Default Environment Variables from Brender Studio
These are the default environment variables that Brender Studio provides for your jobs:

- **`EFS_BLENDER_OUTPUT_FOLDER_PATH`**: Specifies the output path where the rendered frames will be saved. Ensure this path is accessible to all jobs in the array.
  
- **`AWS_BATCH_JOB_ARRAY_SIZE`**: Indicates the total number of jobs in the array. This helps in dividing animations into chunks for each job.
  
- **`AWS_BATCH_JOB_ARRAY_INDEX`**: Represents the index of the current job within the array. Each job uses this index to process its designated chunk of frames.

### Custom Environment Variables
In addition to the default variables, this script uses a custom environment variable to control the rendering behavior:

- **`RENDER_TYPE`**: Determines whether to render a single frame or an animation. Possible values are:
  - `'auto'` (default): Automatically determines whether to render a single frame or animation based on the scene's frame range.
  - `'frame'`: Forces rendering of a single frame, even if the scene has multiple frames defined.
  - `'animation'`: Forces rendering as an animation, even if the scene has only one frame defined.

If you need to use additional custom environment variables for your specific use case, you can add them in the `envs` section of the Job Settings in Brender Studio. Click on `Add Custom env` and provide the variable name and value.

**Example:**
```plaintext
RENDER_TYPE: auto
CUSTOM_VARIABLE_NAME: custom_value
ANOTHER_VARIABLE: another_value
**Example:**
```plaintext
CUSTOM_VARIABLE_NAME: custom_value
ANOTHER_VARIABLE: another_value
```

>Note: Ensure that any custom environment variables you add are properly referenced and handled in your script. For instance, you can retrieve custom variables in your Python script using `os.environ.get('CUSTOM_VARIABLE_NAME')`.

## Code:
The code is distributed across multiple files:

1. `__init__.py` in the project root
2. `scene_setup.py` in the `utils` folder
3. `render_handler.py` in the `utils` folder
4. `aws_batch_utils.py` in the `utils` folder
5. `render_config.py` in the `config` folder

## Project Structure (tree):
```
render_multi_scene/
├── __init__.py
├── README.md
├── utils/
│   ├── __init__.py
│   ├── scene_setup.py
│   ├── render_handler.py
│   └── aws_batch_utils.py
└── config/
    └── render_config.py
```

## Entrypoint:
The entry point is the `__init__.py` file in the project root directory.

## Code Description

### `scene_setup.py`
This file contains functions for setting up multiple scenes from the Blender file.

- **`setup_multi_scene(config)`**: Configures all scenes in the Blender file with the specified settings.
- **`setup_scene(scene, config)`**: Sets up an individual scene with render settings and frame range.

### `render_handler.py`
This file manages the rendering process for both single frames and animations.

- **`render_scenes(scenes, config)`**: Handles rendering for all scenes, determining if each is a single frame or animation.
- **`render_animation(scene, config)`**: Renders animation frames in chunks based on the job array configuration.
- **`render_frame(scene, config, frame)`**: Renders a single frame from a scene.
- **`calculate_frame_chunk(array_size, job_index, start_frame, end_frame, frame_step)`**: Computes the frame range for a specific job in the array.

### `aws_batch_utils.py`
This file provides utility functions for working with AWS Batch.

- **`get_aws_batch_info()`**: Retrieves and processes AWS Batch environment variables.

### `render_config.py`
This file defines the configuration class for render settings.

- **`RenderConfig`**: A class that holds render configuration settings.

### `__init__.py`
This file serves as the main entry point, orchestrating the entire rendering process.

## Note:
This script is intended to be executed as part of an AWS Batch Job Array. Ensure that the necessary environment variables are properly set up before execution, otherwise the job will fail.

## References (video, repo):
N/A

## Screenshots:
N/A

## Tags:
#blender #aws-batch #job-array #multi-scene-rendering #distributed-rendering
