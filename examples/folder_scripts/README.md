# Folder Scripts

## Purpose
In Brender Studio, you can upload either a single Python script or a complete project folder for custom Python jobs. The `folder_scripts` directory contains examples of complete Python projects structured for Blender rendering tasks. These projects demonstrate how to organize and import custom modules to ensure compatibility and functionality within Brender Studio.

## Project Structure
Each project folder within `folder_scripts` should be organized as follows:

```
project_name/
├── __init__.py
├── README.md
└── utils/
    ├── __init__.py
    └── script_module.py
```

### Explanation of Files
- **`__init__.py`**: This file serves as the main entry point for the project. It should include the necessary setup, configuration, and function calls to execute the rendering task.
- **`README.md`**: Provides a detailed description of the project, including its purpose, usage, and any specific requirements or dependencies.
- **`utils/`**: This directory contains utility modules and scripts that support the main functionality. The presence of `__init__.py` makes it a Python package, allowing for structured imports.

## Example Project: `job_array_animation`
The `job_array_animation` project demonstrates how to set up a distributed rendering job using AWS Batch and Blender.

```
job_array_animation/
├── __init__.py
├── README.md
└── utils/
    ├── __init__.py
    └── setup_render_animation.py
```

### Description
- **`__init__.py`**: Configures logging, retrieves environment variables, sets up the Blender scene, calculates frame chunks, and initiates the rendering process.
- **`README.md`**: Describes the project and provides instructions for configuring and running the script.
- **`setup_render_animation.py`**: Contains functions for setting up the scene, calculating frame chunks, rendering frames, and logging progress.

## Custom Module Imports
To import custom modules in your scripts, you need to add a specific line of code to handle the Python path. This ensures that all modules are correctly referenced and can be executed within Brender Studio. 


### Import Example

In `__init__.py`, before any custom imports, include the following lines:

```python
import bpy
import os
import logging
import sys

# Add the parent directory to the Python path
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from utils.setup_render_animation import setup_scene, calculate_frame_chunk, render_animation, log_render_progress
```

This configuration ensures that the AWS Batch container can locate the Python path and import the necessary modules and avoid conflicts. Contributions are welcome to improve this workflow.
Repository: [Brender Studio Docker Blender](https://github.com/Brender-Studio/brender-studio-cdk/blob/main/docker_blender/app/app.py).
