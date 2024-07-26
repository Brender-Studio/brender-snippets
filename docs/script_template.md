# Script Template

Please fill out the following basic template for any scripts being added to the brender-snippets repository.

You can copy this template and paste it into the new script's README.md file or reference it in the example script's README.md file.

## Name:
<!-- Enter the name of the script -->

## Blender Version:
<!-- Specify the Blender version compatible with the script -->

## Purpose:
<!-- Briefly describe the purpose of the script -->


## Script Description:
<!-- Briefly describe what the script does -->

## Detailed Description:
<!-- Provide a detailed description of the script's functionality -->

## Type:
<!-- Indicate whether it's a utility or an example -->
- [ ] Utility
- [ ] Example

## Job Type:
<!-- Indicate the type of job the script performs -->
- [ ] Array
- [ ] Single job

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
| **<KEY_CUSTOM_ENV>**               | **<CUSTOM_VALUE>**        | Custom      |

## Note:
<!-- Any additional notes about the script -->

## Project Structure (tree):
<!-- Provide the project structure (a single script or project folder) -->

## Entrypoint:
<!-- Define the entry point of the script -->

## References (video, repo):
<!-- Provide references like videos or related repositories -->

## Screenshots:
<!-- Include relevant screenshots -->
