# Render Multi-Material

## Name:
render_multi_material

## Blender version:
4.2.0 (LTS)

## Description:
Render multiple images of an object with different materials applied.

## Script parameters:
- `object_name`: The name of the object to render.
- `material_names`: A list of material names to apply to the object.

## Use case:
- [x] Utility
- [x] Example

## Job type:
- [ ] Array
- [x] Single job

## Envs:

### Default environment variables:
Use default environment variables by Brender Studio:
- EFS_BLENDER_OUTPUT_PATH
- EFS_BLENDER_FILE_PATH


### Custom environment variables:
- [x] EFS_BLENDER_OBJECT_NAME


## Code:
- [render_multi_material.py](./render_multi_material.py)

## Note:
This script renders multiple images of a specified object, each with a different material applied. It's useful for quickly visualizing how an object looks with various materials without manually changing materials and rendering each time.

To use this script:
1. Ensure your Blender scene has the object you want to render.
2. Create multiple materials in your Blender file.
3. Modify the `object_name` and `material_names` variables in the script to match your scene.
4. Set the `output_directory` to your desired output location.


### Use cases:
1. Product Design: Quickly visualize a product with different materials or finishes.
2. Architecture: See how different materials affect the look of architectural elements.
3. Character Design: Test various skin, clothing, or armor materials on a character model.

The script will apply each material to the object, render an image, and then move on to the next material. After all renders are complete, it will restore the original material to the object.
