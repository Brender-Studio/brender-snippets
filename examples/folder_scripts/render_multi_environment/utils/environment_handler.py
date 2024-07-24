import os
import bpy
import logging


def load_environments(assets_path):
    environments = []
    
    logging.info(f"Looking for environment files in: {assets_path}")
    
    if not os.path.exists(assets_path):
        logging.error(f"Assets directory not found: {assets_path}")
        return environments

    for file in os.listdir(assets_path):
        if file.endswith('.hdr') or file.endswith('.exr'):
            environment_path = os.path.join(assets_path, file)
            environments.append(environment_path)
            logging.info(f"Found environment file: {environment_path}")

    if not environments:
        logging.warning(f"No .hdr or .exr files found in {assets_path}")

    return environments

def apply_environment(scene, environment_path):
    world = scene.world
    world.use_nodes = True
    node_tree = world.node_tree
    
    # Clear existing nodes
    node_tree.nodes.clear()
    
    # Add Environment Texture node
    env_tex = node_tree.nodes.new(type='ShaderNodeTexEnvironment')
    env_tex.image = bpy.data.images.load(environment_path)
    
    # Add Background node
    background = node_tree.nodes.new(type='ShaderNodeBackground')
    
    # Add Output node
    output = node_tree.nodes.new(type='ShaderNodeOutputWorld')
    
    # Link nodes
    node_tree.links.new(env_tex.outputs['Color'], background.inputs['Color'])
    node_tree.links.new(background.outputs['Background'], output.inputs['Surface'])