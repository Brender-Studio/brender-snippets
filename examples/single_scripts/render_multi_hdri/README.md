# Render Multi HDRI 

## Author:
Brender Studio

## Name:
`render_multi_hdri`

## Blender Version:
4.2.0 (LTS)

## Description:
This script renders images from multiple HDRI files in a Blender scene. It sets each HDRI file as the environment texture and saves the rendered images to the specified output directory.

## Use Case:
- [ ] Utility
- [x] Example

## Job Type:
- [ ] Array
- [x] Single job

## Entrypoint:
`render_multi_hdri.py`

## Envs:
Use the default environment variables provided by Brender Studio.
| **Key**                            | **Value**                 | **Env Type**     |
| ---------------------------------- | ------------------------- | ---------------  |
| **EFS_BLENDER_OUTPUT_FOLDER_PATH** | /mnt/efs/projects//output | Brender Studio   |


## Note:
To use this script:
1. Ensure that multiple HDRI files are set up in your Blender scene.
2. The script will render images for each HDRI file found and save them to the specified output directory.

You can customize environment variables to specify different HDRI file paths if needed.
