import bpy
import os
import logging
import sys

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from utils.scene_setup import setup_multi_scene
from utils.render_handler import render_scenes
from utils.aws_batch_utils import get_aws_batch_info
from config.render_config import RenderConfig

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