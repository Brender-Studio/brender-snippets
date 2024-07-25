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
- [ ] Utility
- [x] Example

## Job type:
- [ ] Array
- [x] Single job

## Entry point:
`render_multi_material.py`

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



