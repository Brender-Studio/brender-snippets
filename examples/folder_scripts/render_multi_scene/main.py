import bpy
import os
import logging
import sys

# Add the project directory to the sys.path before importing any modules
PROJECT_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
if PROJECT_DIR not in sys.path:
    sys.path.append(PROJECT_DIR)

from render_multi_scene.utils.scene_setup import setup_multi_scene
from render_multi_scene.utils.render_handler import render_scenes
from render_multi_scene.utils.aws_batch_utils import get_aws_batch_info
from render_multi_scene.config.render_config import RenderConfig

# Set up logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

def main():
    # Get AWS Batch information
    output_path, array_size, job_index, render_type = get_aws_batch_info()

    # Create render configuration
    config = RenderConfig(output_path, array_size, job_index, render_type)

    # Setup multi-scene
    scenes = setup_multi_scene(config)

    # Render scenes
    render_scenes(scenes, config)

if __name__ == "__main__":
    main()