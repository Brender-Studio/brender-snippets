# Render Multi-Material

## Author:
Brender Studio

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
Use the default environment variables provided by Brender Studio.
| **Key**                            | **Value**                 | **Env Type**    |
| ---------------------------------- | ------------------------- | --------------- |
| **EFS_BLENDER_OUTPUT_FOLDER_PATH** | /mnt/efs/projects//output | Brender Studio  |

### Custom ENV
| **Key**                            | **Value**                 | **Env Type** |
| ---------------------------------- | ------------------------- | ------------ |
| **BLENDER_OBJECT_NAME**            | <OBJECT_NAME>             | Custom       |


## Note:
This script renders multiple images of a specified object, each with a different material applied. It's useful for quickly visualizing how an object looks with various materials without manually changing materials and rendering each time.




