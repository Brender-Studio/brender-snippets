import bpy
import os
import logging
import sys

# Add the project directory to the sys.path before importing any modules
PROJECT_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
if PROJECT_DIR not in sys.path:
    sys.path.append(PROJECT_DIR)
    
from render_multi_environment.utils.scene_setup import setup_scene
from render_multi_environment.utils.render_handler import render_scene_with_environments
from render_multi_environment.utils.aws_batch_utils import get_aws_batch_info
from render_multi_environment.utils.environment_handler import load_environments
from render_multi_environment.config.render_config import RenderConfig

logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

def main():
    # Get AWS Batch job info
    output_path, render_type = get_aws_batch_info()
    
    # Create Render Settings
    config = RenderConfig(output_path, render_type)
    
    # Load environments from assets folder
    environments = load_environments(os.path.join(PROJECT_DIR, 'render_multi_environment/assets'))
    
    # Setup the scene
    scene_config = setup_scene(config)
    
    # Render the scene with all environments
    render_scene_with_environments(scene_config, config, environments)

if __name__ == "__main__":
    main()