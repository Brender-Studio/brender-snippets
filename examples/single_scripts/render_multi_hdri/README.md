# Render Multi HDRI 

## Name:
render_multi_hdri

## Blender version:
4.2.0 (LTS)

## Description:
Render multiple images from different HDRI files in a blend file.

## Use case:
- [x] Utility
- [x] Example

## Job type:
- [ ] Array
- [x] Single job

## Envs:
Use default environment variables by Brender Studio.
- EFS_BLENDER_OUTPUT_PATH
- EFS_BLENDER_FILE_PATH


## Code:

- [render_multi_hdri.py](./render_multi_hdri.py)


## Note:
This script renders multiple images from different HDRI files in a blend file. The script uses the default environment variables provided by Brender Studio to set the output path and the file path. The script can be used as a utility script to render multiple images from different HDRI files in a single job.

If you want to use this script, remember to set up more than one HDRI file in your Blender scene.

You can use custom env variables to set the HDRI file path.

### Use Case:
This script is particularly useful in product visualization and architectural rendering workflows. For example:

1. Product Visualization: When showcasing a product (e.g., a car, furniture, or electronic device), rendering it under different lighting conditions can help potential customers see how it looks in various environments. By using multiple HDRIs, you can quickly generate renders of the product in different settings like indoor showroom, outdoor sunny day, cloudy environment, or night scene.

2. Architectural Rendering: For architectural projects, it's often beneficial to show how a building design looks at different times of the day or in different weather conditions. By using this script with various HDRIs representing different times of day or weather conditions, you can easily generate a series of renders that showcase the building in morning light, midday sun, sunset, overcast conditions, etc.

3. Material Showcasing: When developing materials for 3D assets, it's crucial to test how they react under different lighting conditions. This script allows material artists to quickly render their materials under various HDRIs, helping them ensure the material looks good in all lighting scenarios.

4. Animation Previews: For animated scenes, you might want to test how different lighting setups affect key frames of the animation. This script can be modified to render specific frames of an animation with different HDRIs, allowing for quick comparison of lighting options without having to render full animations.

By automating the process of rendering with multiple HDRIs, this script saves significant time and effort in these workflows, allowing artists and designers to focus on creative decisions rather than repetitive rendering tasks.


## Entrypoint:
render_multi_hdri.py


## Tags:

- Blender
- Render
- HDRI
- Multi-HDRI
- Utility
- Example