# Job Array Animation Renderer With AWS Batch

## Name:
Job Array Animation Renderer

## Blender Version:
Blender 4.2 (LTS)

## Script Description
This script facilitates distributed animation rendering using AWS Batch Job Array, optimized for integration with <a href="https://www.brenderstudio.com" target="_blank">Brender Studio</a>. It partitions the animation into manageable chunks and assigns each chunk to a separate job within the array, allowing for scalable and parallel processing across multiple compute resources.

Designed as a custom script for <a href="https://www.brenderstudio.com" target="_blank">Brender Studio</a>, this example demonstrates how to configure and execute a distributed rendering workflow. The script sets up the rendering parameters in Blender, calculates the frame ranges for each job, and manages the rendering process across all jobs in the array.


Key functionalities include:
- **Scene Configuration**: Sets up the scene’s resolution and output format in Blender.
- **Frame Chunk Calculation**: Computes the frame ranges for each job based on the total animation length and job array size.
- **Rendering and Logging**: Executes the rendering of frames in chunks and logs progress for monitoring job completion.

This script serves as an example of how to utilize Brender Studio’s capability to handle custom scripts for cloud-based animation rendering.

## Type:
- [x] Example
- [x] Utility

## Job Type:
- [x] Array

### Default Environment Variables from Brender Studio
These are the default environment variables that Brender Studio provides for your jobs:

- **`EFS_BLENDER_OUTPUT_FOLDER_PATH`**: Specifies the output path where the rendered frames will be saved. Ensure this path is accessible to all jobs in the array.
  
- **`AWS_BATCH_JOB_ARRAY_SIZE`**: Indicates the total number of jobs in the array. This helps in dividing the animation into chunks for each job.
  
- **`AWS_BATCH_JOB_ARRAY_INDEX`**: Represents the index of the current job within the array. Each job uses this index to process its designated chunk of frames.

### Custom Environment Variables
If you need to use additional or custom environment variables for your specific use case, you can add them in the `envs` section of the Job Settings in Brender Studio. Click `Add Custom env` and provide the variable name and value.

**Example:**
```plaintext
CUSTOM_VARIABLE_NAME: custom_value
ANOTHER_VARIABLE: another_value
```

>Note: Ensure that any custom environment variables you add are properly referenced and handled in your script. For instance, you can retrieve custom variables in your Python script using os.environ.get('CUSTOM_VARIABLE_NAME').

## Code:
The code is distributed across two main files:

1. `__init__.py` in the project root
2. `setup_render_animation.py` in the `utils` folder



## Project Structure (tree):
```
job_array_animation
├── __init__.py
├── README.md
└── utils
    ├── __init__.py
    └── setup_render_animation.py
```

## Entrypoint:
The entry point is the `__init__.py` file in the project root directory.

## Code Description

### `setup_render_animation.py`
This file contains functions for setting up the rendering scene, calculating frame chunks, and rendering the animation.

- **`setup_scene(resolution_x, resolution_y, file_format='PNG')`**: Configures the Blender scene with the specified resolution and file format. Logs and returns the frame range and step.

- **`calculate_frame_chunk(array_size, job_index, start_frame, end_frame, frame_step)`**: Computes the start and end frames for a specific job based on the job array size and index.

- **`render_animation(start_frame, end_frame, frame_step, array_size, job_index, output_path)`**: Renders frames in the specified range and logs the rendering progress.

- **`log_render_progress(current_frame, start_frame, end_frame, frame_step)`**: Logs the rendering progress percentage and the current frame details.

### `__init__.py`
This file serves as the main entry point and configures the logging. It also retrieves environment variables, sets up the scene, calculates the frame chunks, and initiates the rendering process.


## Note:
This script is intended to be executed as part of an AWS Batch Job Array. Ensure that the necessary environment variables are properly set up before execution, otherwise the job will fail.


## References (video, repo):
N/A

## Screenshots:
N/A

## Tags:
#blender #aws-batch #job-array #animation-rendering #distributed-rendering