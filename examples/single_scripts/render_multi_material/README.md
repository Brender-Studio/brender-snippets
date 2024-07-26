# Render Multi-Material

## Author:
© 2024 Brender Studio

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

### Default ENVS
| **Key**                            | **Value**                 | **Actions** |
| ---------------------------------- | ------------------------- | ----------- |
| **JOB_ACTION_TYPE**                | custom_render_python      | Default     |
| **EFS_MAIN_SCRIPT_PATH**           | /mnt/efs/projects/        | Default     |
| **EFS_BLENDER_FILE_PATH**          | /mnt/efs/projects/        | Default     |
| **EFS_BLENDER_OUTPUT_FOLDER_PATH** | /mnt/efs/projects//output | Default     |
| **BLENDER_EXECUTABLE**             | /usr/bin/blender          | Default     |
| **USE_EEVEE**                      | False                     | Default     |
| **USE_GPU**                        | False                     | Default     |
| **BUCKET_NAME**                    | brender-bucket-s3-<UUID>  | Default     |
| **BUCKET_KEY**                     | <PROJECT_NAME>            | Default     |

### Custom ENV
| **Key**                            | **Value**                 | **Actions** |
| ---------------------------------- | ------------------------- | ----------- |
| **BLENDER_OBJECT_NAME**            | <OBJECT_NAME>             | Custom     |


## Note:
This script renders multiple images of a specified object, each with a different material applied. It's useful for quickly visualizing how an object looks with various materials without manually changing materials and rendering each time.

To use this script:
1. Ensure your Blender scene has the object you want to render.
2. Create multiple materials in your Blender file.
3. Modify the `object_name` and `material_names` variables in the script to match your scene.
4. Run the script to render images with different materials applied to the object.



