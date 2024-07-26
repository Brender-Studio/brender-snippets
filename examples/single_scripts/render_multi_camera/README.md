# Render Multi Camera

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


## References (video, repo):
- [N/A]

## Screenshots:
- [N/A]

## Note:
This script renders multiple images from different cameras in a Blender scene. It uses default environment variables provided by Brender Studio to set the output path and the file path.

To use the script, ensure that:
- You have set up multiple cameras in your Blender scene.



