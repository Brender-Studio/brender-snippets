# Render Multi Camera

## Author:
Brender Studio

## Name:
`render_multi_camera`

## Blender Version:
4.2.0 (LTS)

## Description:
This script renders images from multiple cameras in a Blender scene. It sets the active camera for each render and saves the images to the specified output directory.


## Entrypoint:
`render_multi_camera.py`


## Use Case:
- [x] Utility
- [x] Example

## Job Type:
- [ ] Array
- [x] Single job

## Envs:

### Default ENVS
| **Key**                            | **Value**                 | **Env Type**    |
| ---------------------------------- | ------------------------- | --------------- |
| **EFS_BLENDER_OUTPUT_FOLDER_PATH** | /mnt/efs/projects//output | Brender Studio  |



## Note:
This script renders multiple images from different cameras in a Blender scene. It uses default environment variables provided by Brender Studio to set the output path and the file path.

To use the script, ensure that:
- You have set up multiple cameras in your Blender scene.



