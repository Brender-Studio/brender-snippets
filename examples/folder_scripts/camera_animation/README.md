# Render Script for Camera Animation in Blender

## Name:
Camera Animation Render Script

## Blender Version:
4.2

## Script Description:
This script creates a camera animation path in Blender, sets up the camera to follow this path, and renders the animation. It's designed to work with AWS Batch for cloud rendering, allowing for distributed rendering of frame ranges.

## Type:
- [x] Example

## Job Type:
- [x] Array

## Envs:
- EFS_BLENDER_FILE: Path to the Blender file
- EFS_BLENDER_OUTPUT_PATH: Output directory for rendered frames
- AWS_BATCH_JOB_ARRAY_INDEX: Index of the current job in the array (for distributed rendering)
- AWS_BATCH_JOB_ARRAY_SIZE: Total number of jobs in the array (for distributed rendering)


## Job Configuration:

When setting up the job in AWS Batch, you need to specify the array size. This determines how many parallel jobs will be created to render your animation.

The optimal array size depends on several factors:
1. Total number of frames in your animation
2. Rendering time per frame
3. Available computational resources
4. Cost considerations

In this script, the total number of frames is calculated as:
`total_frames = len(path_data) * 50`

For example, if you have 5 points in your path_data, you'll have 250 frames.

A general guideline for choosing the array size:
- For short animations (< 100 frames): Consider an array size of 5-10
- For medium animations (100-500 frames): Consider an array size of 10-25
- For long animations (> 500 frames): Consider an array size of 25-50 or more

Remember, each job in the array will render a subset of frames:
`frames_per_job = total_frames // job_array_size`

Example:
If you have 250 frames and set the array size to 10:
- Each job will render 25 frames
- Job 0 will render frames 1-25, Job 1 will render frames 26-50, and so on

Adjust the array size based on your specific needs, rendering time, and available resources.


## Code:
The project consists of multiple Python files:

1. `__init__.py`: Main script that sets up the camera path and initiates rendering.
2. `scripts/camera_path.py`: Creates the camera path.
3. `scripts/render.py`: Handles the rendering process, including frame range calculations for distributed rendering.

(Full code can be found in the project files) [camera_animation](./)

## Note:
This script is designed to work with AWS Batch for cloud rendering. It automatically adjusts the animation length based on the number of points in the camera path.

## Project Structure (tree):

```plaintext
camera_animation/
 ├── __init__.py
 ├── README.md
 └── scripts
    ├── camera_path.py
    ├── __init__.py
    └── render.py
```

## Entrypoint:
The main entry point is the `main()` function in `__init__.py`.

## References (video, repo):
N/A

## Screenshots:
N/A

## Tags:
#blender #animation #camera #rendering #aws-batch #cloud-rendering