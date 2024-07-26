# Enable GPUs for Rendering in AWS Batch

## Author:
© 2024 Brender Studio

## Name:
Enable GPUs for Rendering

## Blender Version:
4.2 (LTS)

## Description:
This script enables the use of GPUs for rendering in Blender using Brender Studio. It checks for available devices (CPU and GPU), activates them, and configures Blender's Cycles rendering engine to use the GPUs. Additionally, it renders the current frame and saves the output to a specified path.

## Entrypoint:
- The entry point for this script is the `render_gpu.py` function.

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

### Set Default ENV GPU
- `USE_GPU` : Set to `True` to enable GPU rendering.


> Refer to the [Brender Studio Documentation](https://www.brenderstudio.com/docs/ui-user-guides/rendering-modes) for more information on setting up and using Brender Studio.