# Render Multi HDRI 

## Author:
© 2024 Brender Studio

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
- [N/A]


## Entrypoint:
`render_multi_hdri.py`

## References:
- [N/A]

## Screenshots:
- [N/A]

## Note:
To use this script:
1. Ensure that multiple HDRI files are set up in your Blender scene.
2. The script will render images for each HDRI file found and save them to the specified output directory.

You can customize environment variables to specify different HDRI file paths if needed.
